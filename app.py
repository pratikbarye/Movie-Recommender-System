import streamlit as st
import pickle
import pandas as pd
import requests

# Load the pre-processed movie dictionary and convert it into a DataFrame
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Hardcoded user credentials (for login/signup)
USER_CREDENTIALS = {
    "Akshay": "akshay@1234",
    "Aryan": "aryan@5678",
    "Pratik": "pratik@1357"
}


# Function to fetch the poster image from the TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f5ba8dfd3bdc67fd825ffd0d16f1e1c1&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"


# Function to recommend movies based on the selected movie
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


# Main App UI after login
def main_app():
    # Add custom CSS for the logout button
    st.markdown("""
            <style>
            .logout-button {
                position: absolute;
                top: 20px;
                left: 20px;
                background-color: #ff4b4b;
                color: white;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
                font-weight: bold;
                border-radius: 5px;
            }
            .logout-button:hover {
                background-color: #ff0000;
            }
            </style>
        """, unsafe_allow_html=True)

    # Display logout button
    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button("Logout", key="logout", use_container_width=False):
            st.session_state.logged_in = False

    # App header and welcome message
    st.image("WatchWise Logo Design.png", width=120)
    st.title(f"Welcome, {st.session_state.username}!")
    st.subheader('Movie Recommendation System')

    # Dropdown to select a movie
    select_movie_name = st.selectbox(
        'Enter the Name of Movie',
        movies['title'].values
    )
    # Show recommendations when button is clicked
    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(select_movie_name)
        st.write("")  # Just for spacing
        cols = st.columns(5, gap="medium")  # 5 columns with medium gap
        for idx, col in enumerate(cols):
            with col:
                st.image(recommended_movie_posters[idx], use_container_width=True)
                st.markdown(f"<div style='text-align: center; font-weight: bold;'>{recommended_movie_names[idx]}</div>",
                            unsafe_allow_html=True)


# Login Page UI
def login_page():
    # Center align the login box
    col1, col2, col3 = st.columns([1.5, 1.2, 1])
    with col2:
        st.image("WatchWise Logo Design.png", width=120)

    st.title("Sign In")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Sign In and Sign Up buttons
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col2:
        if st.button("Sign In"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                # st.experimental_rerun()
            else:
                st.error("Invalid username or password.")

        if st.button("Sign Up"):
            st.session_state.page = 'signup'
            # st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# Signup Page UI
def signup_page():
    # Center align the signup box
    col1, col2, col3 = st.columns([1.5, 1.2, 1])
    with col2:
        st.image("WatchWise Logo Design.png", width=120)

    st.title("Sign Up")

    # Input fields for new username and password
    new_username = st.text_input("Create Username")
    new_password = st.text_input("Create Password", type="password")

    # Create Account and Back to Sign In buttons
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col2:
        if st.button("Create Account"):
            if new_username in USER_CREDENTIALS:
                st.error("Username already exists!")
            else:
                USER_CREDENTIALS[new_username] = new_password
                st.success("Account created successfully! Please sign in now.")
                st.session_state.page = 'login'

        if st.button("Back to Sign In"):
            st.session_state.page = 'login'


# --------- App Routing Section ---------

# Initialize session states if not already initialized
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Based on login status, show appropriate page
if st.session_state.logged_in:
    main_app()
else:
    if st.session_state.page == 'login':
        login_page()
    elif st.session_state.page == 'signup':
        signup_page()







#
# ######   2-below   #########
#
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
#
# def fetch_poste(movie_id):
#     responce = requests.get(
#         'https://api.themoviedb.org/3/movie/{}?api_key=f5ba8dfd3bdc67fd825ffd0d16f1e1c1&language=en-US'.format(
#             movie_id))
#     data = responce.json()
#     return ("https://image.tmdb.org/t/p/w500/") + data['poster_path']
#     # https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg
#
#
# # making recommend function
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]  # its function that find index value from table
#     distances = similarity[movie_index]  # measuring distance of array
#     # For next step we sort the list with emurate function so it convert with tuple
#     # Then it will reverse the list and then its will give 5 simmilar cordinate suggestion using lambda function
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movie = []
#     recommended_movie_posters = []
#     for i in movies_list:
#         # now we are try to fetch the poster of movie with movie id
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movie.append(movies.iloc[i[0]].title)
#         # fetch poster from API
#         recommended_movie_posters.append(fetch_poste(movie_id))
#     return recommended_movie, recommended_movie_posters
#
#
# # assign .pkl file to the frontend to show the list of titles of movies
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# # import statemnt for similarity
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # main heading for project
# st.title('Movie Recommender System')
#
# # creataing a search and selectbox two in one
# selected_movie_name = st.selectbox(
#     'How Would you like to be contacted?',
#     movies['title'].values)
#
# # adding button to the screen
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#     # Create 5 equal columns
#     col1, col2, col3, col4, col5 = st.columns(5)
#
#     with col1:
#         st.image(posters[0], width=150)  # Fixed width for all posters
#         st.markdown(f"**{names[0]}**", unsafe_allow_html=True)
#
#     with col2:
#         st.image(posters[1], width=150)
#         st.markdown(f"**{names[1]}**", unsafe_allow_html=True)
#
#     with col3:
#         st.image(posters[2], width=150)
#         st.markdown(f"**{names[2]}**", unsafe_allow_html=True)
#
#     with col4:
#         st.image(posters[3], width=150)
#         st.markdown(f"**{names[3]}**", unsafe_allow_html=True)
#
#     with col5:
#         st.image(posters[4], width=150)
#         st.markdown(f"**{names[4]}**", unsafe_allow_html=True)
#














######   1-below   #########


# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
#
# def fetch_poste(movie_id):
#     responce = requests.get(
#         'https://api.themoviedb.org/3/movie/{}?api_key=f5ba8dfd3bdc67fd825ffd0d16f1e1c1&language=en-US'.format(
#             movie_id))
#     data = responce.json()
#     return ("https://image.tmdb.org/t/p/w500/") + data['poster_path']
#     # https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg
#
#
# # making recommend function
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]  # its function that find index value from table
#     distances = similarity[movie_index]  # measuring distance of array
#     # For next step we sort the list with emurate function so it convert with tuple
#     # Then it will reverse the list and then its will give 5 simmilar cordinate suggestion using lambda function
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movie = []
#     recommended_movie_posters = []
#     for i in movies_list:
#         # now we are try to fetch the poster of movie with movie id
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movie.append(movies.iloc[i[0]].title)
#         # fetch poster from API
#         recommended_movie_posters.append(fetch_poste(movie_id))
#     return recommended_movie, recommended_movie_posters
#
#
# # assign .pkl file to the frontend to show the list of titles of movies
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# # import statemnt for similarity
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # main heading for project
# st.title('Movie Recommender System')
#
# # creataing a search and selectbox two in one
# selected_movie_name = st.selectbox(
#     'How Would you like to be contacted?',
#     movies['title'].values)
#
# # adding button to the screen
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])














######  2 - below #######







