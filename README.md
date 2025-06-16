# Movie-Recommender-System

A content-based movie recommendation system built using Python, Streamlit, and TMDB API. This project suggests similar movies based on user input using cosine similarity and movie metadata.

🔗 **Live Demo:** [Click here to use the app](https://movie-recommender-system-6abpgjf6uwrh2tvnvg5tx4.streamlit.app/)

## 📽️ Features

- 🔍 Search your favorite movie
- 🤖 Get 5 movie recommendations instantly
- 🖼️ Movie posters fetched using TMDB API
- 💡 Simple and user-friendly Streamlit interface

## 📺 Video Reference

This project is built by following the tutorial from the YouTube channel *CodeWithHarry*:

[Watch Tutorial on YouTube](https://youtu.be/1xtrIEwY_zY?si=LrLzeQPkRGTUvtl_)

## 🚀 Tech Stack

- **Frontend/UI:** Streamlit
- **Backend:** Python
- **Data Handling:** Pandas, Scikit-learn
- **API:** TMDB (The Movie Database)

## 📁 Project Structure

├── app.py # Main Streamlit application
├── movies.csv # Movie data
├── similarity.pkl # Precomputed similarity matrix
├── requirements.txt # Python dependencies

bash
Copy
Edit

## 🛠️ Setup Instructions

To run this project locally:

1. **Clone the repository:**

```bash
git clone https://github.com/pratikbarye/Movie-Recommender-System.git
cd Movie-Recommender-System
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
🌐 TMDB API Key Setup
Create a free account on TMDB.

Navigate to your API section and generate an API key.

Replace the API key directly in your app.py file where it's required.

📷 Screenshots
<img src="https://i.imgur.com/U9hYzNv.png" width="700"/>
📄 License
This project is open-source and available under the MIT License.
