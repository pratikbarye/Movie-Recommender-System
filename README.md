# Movie-Recommender-System

A content-based movie recommendation system built using Python, Streamlit, and TMDB API. This project suggests similar movies based on user input using cosine similarity and movie metadata.

🔗 **Live Demo:** [Click here to use the app](https://movie-recommender-system-6abpgjf6uwrh2tvnvg5tx4.streamlit.app/)

## 📽️ Features

- 🔍 Search your favorite movie
- 🤖 Get 5 movie recommendations instantly
- 🖼️ Movie posters fetched using TMDB API
- 💡 Simple and user-friendly Streamlit interface

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

## Project Demo screenshot
![project p1](https://github.com/user-attachments/assets/883948fe-f4d3-43f7-aff0-b52d68a1f7b7)

![project p2](https://github.com/user-attachments/assets/edd8ee2c-6bf6-4ebd-8b1c-a792c2b2d667)

![project P3](https://github.com/user-attachments/assets/8ebd06ea-9e98-4a9c-b837-07dfd77f24dd)





## 🛠️ Setup Instructions

To run this project locally:

1. **Clone the repository:**

```bash
git clone https://github.com/pratikbarye/Movie-Recommender-System.git
cd Movie-Recommender-System

2. **Install dependencies:**

bash
pip install -r requirements.txt

3. **Run the app:**

bash

streamlit run app.py


🌐 TMDB API Key Setup
1.Create a free account on TMDB.

2.Navigate to your API section and generate an API key.

3.Replace the API key directly in your app.py file where it's required.


📄 License
This project is open-source and available under the MIT License.
