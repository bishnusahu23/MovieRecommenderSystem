import streamlit as st
import pickle
import numpy as np
import requests
import gdown

try:
    with open("Formatted_movies.pkl",'rb') as file:
        movies=pickle.load(file)

    file_id = "1reqRIPB3oatkqCqzk5XpK13m88mq9jBE"  # Extract from the link
    output = "similarity.pkl"
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
    with open(output,'rb') as file:
        similarity=pickle.load(file)
except Exception as e:
    st.write(f"Error loading data: {e}")


st.title("Movie Recommeder System")
choice=st.selectbox("Pick one:",options= list(movies['title']))
num=int(st.number_input("Select number of recommendations",placeholder="Enter a digit", min_value=1, step=1))

def fetch_posters(id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(id)
    data= requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" +poster_path
    return full_path


def recommend(name, count):
    try:
        idx=movies[movies['title']==name].index[0]
        indexes=list(np.argsort(similarity[idx])[-count-1:-1])
        movies_df=movies.loc[indexes][['title','id']]
        recommended_movies=[]
        posters=[]
        for index,row in movies_df.iterrows():
            movie_id=row['id']
            posters.append(fetch_posters(movie_id))
            recommended_movies.append(row['title'])
        return recommended_movies,posters
        
    except:
        st.write('No recommendations available')
        
if st.button('Recommend'):
    recommended_movies, posters = recommend(choice, num)
    if recommended_movies:
        for name, poster in zip(recommended_movies, posters):
            with st.container():
                col1, col2 = st.columns([1,4])  
                with col1:
                    st.image(poster, width=100)   
                with col2:
                    st.write(name)                
                    st.markdown('---') 
    else:
        st.write("No recommendations available.")
    


    










