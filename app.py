import streamlit as st
from src.load_data import load_movies
from src.recommender import build_similarity, create_title_index
from difflib import get_close_matches

# Page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Type a movie you like and get similar recommendations!")


# Load data (cached)
@st.cache_data
def load_engine():
    movies = load_movies()
    similarity_matrix = build_similarity(movies)
    title_to_index = create_title_index(movies)
    return movies, similarity_matrix, title_to_index


movies, similarity_matrix, title_to_index = load_engine()

# Input
user_movie = st.text_input("Enter a movie name:")

if st.button("Recommend", use_container_width=True):
    if user_movie.strip() == "":
        st.warning("Please enter a movie name.")
        st.stop()

    movie_title = user_movie.lower().strip()
    all_titles = list(title_to_index.keys())

    # Partial match
    partial_matches = [t for t in all_titles if movie_title in t]

    if partial_matches:
        best_match = partial_matches[0]
    else:
        matches = get_close_matches(movie_title, all_titles, n=3, cutoff=0.2)

        if not matches:
            st.error("Movie not found in dataset.")
            st.stop()

        st.info("Did you mean:")
        for m in matches:
            st.write("•", m.title())

        best_match = matches[0]

    # Get recommendations
    idx = title_to_index[best_match]
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    st.success(f"Recommendations based on: {best_match.title()}")

    # Display results
    for i in similarity_scores[1:6]:
        movie_idx = i[0]
        st.markdown(f" **{movies.iloc[movie_idx]['title']}**")
