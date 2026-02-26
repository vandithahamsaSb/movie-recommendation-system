# 🎬 Movie Recommendation System

An AI-powered movie recommendation system built using machine learning and deployed as an interactive Streamlit web application.

---

## 🚀 Features
- Content-based movie recommendation engine
- Cosine similarity for finding similar movies
- Fuzzy search to handle typos and partial names
- Streamlit web interface
- Clean modular Python structure

---

## 🧠 How It Works
Each movie is represented as a vector of genres.  
The system calculates similarity between movies using **cosine similarity** and recommends the most similar ones based on user input.

Fuzzy matching is used to handle spelling mistakes and partial movie names.

---

## 🌐 Run the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
🛠 Tech Stack

Python

Pandas

Scikit-learn

Streamlit

📂 Project Structure
movie-recommendation-system/
│
├── app.py
├── main.py
├── requirements.txt
├── src/
│   ├── load_data.py
│   └── recommender.py
└── data/
    └── movies.csv

📌 Future Improvements

Hybrid recommendation (content + ratings)

Movie posters integration

Online deployment


⭐ Built as part of my AI/ML learning journey.
