from src.load_data import load_movies
from src.recommender import build_similarity, create_title_index, recommend


def main():
    print("Loading movie dataset...")
    movies = load_movies()

    print("Building similarity matrix...")
    similarity_matrix = build_similarity(movies)

    print("Preparing title index...")
    title_to_index = create_title_index(movies)

    print("\n Movie Recommender Ready!")

    while True:
        user_movie = input("\nEnter a movie you like (or type 'exit'): ").strip()

        if user_movie.lower() == "exit":
            print("Goodbye! Visit again for more recommendations.")
            break

        recommend(user_movie, movies, similarity_matrix, title_to_index)


if __name__ == "__main__":
    main()
