import streamlit as st
import pickle
import pandas as pd
import requests

st.markdown("""
    <style>
        .delete-user-button button {
            min-width: 120px;
            white-space: nowrap;
            padding: 6px 12px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)


# Load the movie data and similarity matrix
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f5ba8dfd3bdc67fd825ffd0d16f1e1c1&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Welcome Page
def welcome_page():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("WatchWise Logo Design.png", width=100)
    with col2:
        st.markdown("## Welcome to WatchWise!")
        st.write("Discover personalized movie recommendations based on your favorite movie.")

    st.markdown("### What is your name?")
    name_input = st.text_input("Enter your name")

    if st.button("Create Account"):
        if name_input.strip() == "":
            st.warning("Please enter your name.")
        else:
            st.session_state.username = name_input
            st.session_state.logged_in = True

# Main App Page
def main_app():
    # Top bar
    col1, col2 = st.columns([9, 1])
    with col1:
        st.title(f"Welcome, {st.session_state.username}!")
    with col2:
        st.markdown('<div class="delete-user-button">', unsafe_allow_html=True)  # START CSS DIV
        # if st.button("Delete User", key="delete_button_fixed"):  # Give it a key to avoid conflicts
        #     del st.session_state.username
        #     st.session_state.logged_in = False
        #     st.rerun()
        # st.markdown("</div>", unsafe_allow_html=True)  # END CSS DIV

    st.image("WatchWise Logo Design.png", width=120)
    st.subheader("Movie Recommendation System")

    selected_movie = st.selectbox("Select a movie", movies['title'].values)

    if st.button("Show Recommendation"):
        names, posters = recommend(selected_movie)
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(posters[i])
                st.markdown(f"**{names[i]}**", unsafe_allow_html=True)

# Session logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    main_app()
else:
    welcome_page()
