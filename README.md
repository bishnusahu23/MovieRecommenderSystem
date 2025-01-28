# MovieRecommenderSystem using tmdb dataset
This project implements a Movie Recommendation System using machine learning techniques and natural language processing. The system provides personalized movie suggestions based on user input by analyzing movie metadata and employing cosine similarity.

## Project Overview
- The goal of this project is to recommend movies by analyzing metadata such as genres, keywords, cast, and crew. The recommendations are generated using a content-based filtering approach.

## Key Features
 - Content-Based Filtering: The system uses TF-IDF vectorization to process and analyze movie tags.
 - Cosine Similarity: To compute the similarity between movies based on their features.
 - Efficient Data Processing: Custom functions handle the preprocessing and feature extraction tasks.
 - Workflow
1. Data Processing
- Missing values in the dataset were handled by dropping incomplete rows.
- Textual data like genres and keywords were converted into lists and further preprocessed to create a unified "tags" column.
- Stop words were removed, and stemming was applied to reduce words to their root forms.

2. Feature Extraction
- TF-IDF vectorization was applied to the "tags" column to extract numerical features for similarity calculation.

3. Recommendation Engine
- Cosine Similarity: The similarity matrix was computed to identify the most similar movies.
- A recommendation function fetches top suggestions based on similarity scores.

4. Deployment Using Streamlit
- The recommendation system has been deployed as a web application using Streamlit. Users can input a movie name, and the app will provide personalized recommendations.

## Key Features of the Streamlit App:
- Input field for movie name.
- Input field to select the number of recommendations.
- Interactive user interface for a seamless experience.

## Libraries Used
-  Python: Core programming language.
-  Pandas: For data manipulation.
- NumPy: For numerical computations.
- NLTK: For text preprocessing.
-  Scikit-learn: For TF-IDF vectorization and similarity computation.
-  Streamlit: For deploying the application as a web app.
## How to Run
-  Clone this repository.
-  Install the required dependencies using pip install -r requirements.txt.
-  Run the app using streamlit run app.py

## Author
-  This project was developed as part of a data science practice initiative. It showcases the application of NLP and machine learning in building personalized recommendation systems.
