import pandas as pd


def load_movies():
    movies = pd.read_csv("data/movies.csv", sep="|", encoding="latin1", header=None)

    # FORCE column names
    movies.columns = [
        "movie_id",
        "title",
        "release_date",
        "video_release_date",
        "IMDb_URL",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
    ]

    print("DEBUG columns:", movies.columns[:5])  # <-- temporary debug
    return movies
