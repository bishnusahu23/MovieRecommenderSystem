import streamlit as st
import pickle
import numpy as np
import requests
import gdown
import gzip

# Load Movies and Cosine Similarity from Google Drive
try:
    with open("Formatted_movies.pkl", 'rb') as file:
        movies = pickle.load(file)

    # Google Drive file ID extracted
    file_url = "https://drive.google.com/uc?export=download&id=1reqRIPB3oatkqCqzk5XpK13m88mq9jBE"
    
    # Download the file using gdown
    gdown.download(file_url, 'cosine_similarity.pkl', quiet=False)

    # Load the cosine similarity matrix
    with open('cosine_similarity.pkl', 'rb') as file:
        cosine_sim = pickle.load(file)

except Exception as e:
    st.write(f"Error loading data: {e}")

# Streamlit Title
st.title("Movie Recommender System")

# User Input Section
choice = st.selectbox("Pick a movie:", options=list(movies['title']))
num = int(st.number_input("Number of recommendations:", min_value=1, step=1))

# Fetch Movie Poster Function
def fetch_posters(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return None

# Movie Recommendation Function
def recommend(name, count):
    try:
        idx = movies[movies['title'] == name].index[0]
        indexes = list(np.argsort(cosine_sim[idx])[-count-1:-1])
        movies_df = movies.loc[indexes][['title', 'id']]
        
        recommended_movies = []
        posters = []
        for _, row in movies_df.iterrows():
            poster = fetch_posters(row['id'])
            if poster:
                posters.append(poster)
                recommended_movies.append(row['title'])
        return recommended_movies, posters
    except Exception as e:
        st.write(f"Error generating recommendations: {e}")
        return [], []

if st.button('Recommend'):
    recommended_movies, posters = recommend(choice, num)
    if recommended_movies:
        cols = st.columns(5)  # Adjust the number of columns based on your layout preference
        for index, (name, poster) in enumerate(zip(recommended_movies, posters)):
            with cols[index % 5]:  # This will wrap the items after every 5 movies
                st.write(name)
                st.image(poster, width=150)
    else:
        st.write("No recommendations available.")
