from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches


# -----------------------------
# Build similarity matrix
# -----------------------------
def build_similarity(movies):
    genre_cols = movies.columns[5:]
    genre_matrix = movies[genre_cols].values
    return cosine_similarity(genre_matrix)


# -----------------------------
# Create title index
# -----------------------------
def create_title_index(movies):
    title_to_index = {}
    for idx, title in enumerate(movies["title"]):
        title_to_index[title.lower()] = idx
    return title_to_index


# -----------------------------
# FINAL Search + Recommend
# -----------------------------
def recommend(movie_title, movies, similarity_matrix, title_to_index, top_n=5):
    movie_title = movie_title.lower().strip()
    all_titles = list(title_to_index.keys())

    partial_matches = [t for t in all_titles if movie_title in t]

    if partial_matches:
        best_match = partial_matches[0]
    else:
        matches = get_close_matches(movie_title, all_titles, n=3, cutoff=0.2)

        if not matches:
            print("Movie not found in dataset.")
            return

        print("\n Did you mean:")
        for i, m in enumerate(matches, 1):
            print(f"{i}. {m.title()}")

        best_match = matches[0]

    # -----------------------------
    # Generate recommendations
    # -----------------------------
    idx = title_to_index[best_match]

    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    print(f"\n Recommendations based on: {best_match.title()}\n")

    count = 0
    for i in similarity_scores[1:]:
        movie_idx = i[0]
        print("-", movies.iloc[movie_idx]["title"])
        count += 1
        if count == top_n:
            break
