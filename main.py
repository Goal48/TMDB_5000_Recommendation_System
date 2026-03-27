import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
import nltk
import requests

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Set page config
st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# Initialize session state for API key
if 'tmdb_api_key' not in st.session_state:
    st.session_state.tmdb_api_key = ""

# TMDB API Configuration
TMDB_BASE_URL = "https://api.themoviedb.org/3"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"

@st.cache_data
def load_data():
    """Load and preprocess movie data"""
    try:
        movies = pd.read_csv('tmdb_5000_movies.csv')
        credits = pd.read_csv('tmdb_5000_credits.csv')
    except FileNotFoundError as e:
        st.error(f"❌ Error loading CSV files: {e}")
        st.stop()
    
    # Merge datasets
    movies = movies.merge(credits, on='title')
    
    # Select relevant columns (handle missing columns)
    cols_to_select = ['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']
    available_cols = [col for col in cols_to_select if col in movies.columns]
    movies = movies[available_cols]
    
    # Drop nulls
    movies.dropna(inplace=True)
    
    return movies

def preprocess_data(movies):
    """Preprocess movie data for recommendation"""
    import ast
    from ast import literal_eval
    
    def convert(obj):
        L = []
        try:
            for i in literal_eval(obj):
                L.append(i['name'])
        except:
            pass
        return L
    
    def convert_cast(obj):
        L = []
        count = 0
        try:
            for i in literal_eval(obj):
                if count != 3:
                    L.append(i['name'])
                    count += 1
        except:
            pass
        return L
    
    def convert_director(obj):
        L = []
        try:
            for i in literal_eval(obj):
                if i['job'] == 'Director':
                    L.append(i['name'])
                    break
        except:
            pass
        return L
    
    # Convert genres and keywords
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert_cast)
    movies['crew'] = movies['crew'].apply(convert_director)
    
    # Remove spaces
    for col in ['genres', 'keywords', 'cast', 'crew']:
        movies[col] = movies[col].apply(lambda x: [i.replace(" ", "") for i in x])
    
    # Create tags
    movies['tags'] = movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'] + movies['overview'].apply(lambda x: x.split() if isinstance(x, str) else [])
    
    # Join tags
    movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))
    
    # Convert to lowercase
    movies['tags'] = movies['tags'].apply(lambda x: x.lower())
    
    # Stemming
    port = PorterStemmer()
    def stem(text):
        y = []
        for i in text.split():
            y.append(port.stem(i))
        return " ".join(y)
    
    movies['tags'] = movies['tags'].apply(stem)
    
    return movies

@st.cache_data
def get_similarity_matrix(tags):
    """Generate cosine similarity matrix"""
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(tags).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

def get_poster_url(movie_id):
    """Fetch poster URL from TMDB API"""
    api_key = st.session_state.get('tmdb_api_key', '')
    if not api_key:
        return None
    
    try:
        url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={api_key}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f"{POSTER_BASE_URL}{poster_path}"
    except:
        pass
    return None

def recommend_movies(movie_title, movies, similarity, n_recommendations=10):
    """Get top N movie recommendations"""
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
    except IndexError:
        return None
    
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:n_recommendations+1]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append({
            'title': movies.iloc[i[0]]['title'],
            'score': round(i[1] * 100, 2),
            'movie_id': int(movies.iloc[i[0]]['movie_id']) if 'movie_id' in movies.columns else None
        })
    
    return recommended_movies

# Custom CSS for better styling
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
    }
    
    .movie-card {
        background-color: #161b22;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        transition: transform 0.3s;
    }
    
    .movie-title {
        font-weight: bold;
        font-size: 16px;
        margin-top: 10px;
    }
    
    .movie-score {
        color: #ffd700;
        font-size: 14px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Main UI
st.title("🎬 Movie Recommendation System")
st.write("Discover movies similar to your favorites using AI-powered recommendations")

# Load data
with st.spinner("Loading movie data..."):
    movies = load_data()
    movies = preprocess_data(movies)
    similarity = get_similarity_matrix(movies['tags'])

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    n_recommendations = st.slider("Number of recommendations", 5, 20, 10)
    
    st.divider()
    
    st.header("🔑 TMDB API Key")
    api_key = st.text_input(
        "Enter API Key (optional for posters)",
        type="password",
        help="Get free API key from https://www.themoviedb.org/settings/api",
        value=st.session_state.tmdb_api_key
    )
    if api_key:
        st.session_state.tmdb_api_key = api_key
    
    if st.session_state.tmdb_api_key:
        st.success("✅ API Key connected!")
    else:
        st.info("ℹ️ Add API key to see movie posters")

# Movie selection
st.divider()
st.subheader("🔍 Select a Movie")
movie_titles = sorted(movies['title'].unique())
selected_movie = st.selectbox("Choose a movie:", movie_titles, label_visibility="collapsed")

# Generate recommendations
if selected_movie:
    recommendations = recommend_movies(selected_movie, movies, similarity, n_recommendations)
    
    if recommendations:
        # Display selected movie info
        st.divider()
        st.markdown(f"### 📽️ Movies Similar to: **{selected_movie}**")
        
        # Get selected movie poster
        selected_movie_data = movies[movies['title'] == selected_movie].iloc[0]
        selected_movie_id = int(selected_movie_data['movie_id']) if 'movie_id' in movies.columns else None
        selected_poster = get_poster_url(selected_movie_id) if selected_movie_id else None
        
        if selected_poster:
            cols_selected = st.columns([1, 2])
            with cols_selected[0]:
                st.image(selected_poster, width=200)
            with cols_selected[1]:
                st.write(f"**Title:** {selected_movie}")
                if 'overview' in movies.columns:
                    overview = selected_movie_data['overview']
                    st.write(f"**Overview:** {overview[:200]}...")
        
        st.divider()
        
        # Display recommendations in a nice grid
        st.markdown(f"### 🎯 Top {len(recommendations)} Recommendations")
        
        # Create columns for poster display (5 movies per row)
        cols = st.columns(5)
        
        for idx, movie in enumerate(recommendations):
            col_idx = idx % 5
            with cols[col_idx]:
                movie_title = movie['title']
                similarity_score = movie['score']
                movie_id = movie.get('movie_id')
                
                # Container for each movie
                with st.container():
                    poster_url = get_poster_url(movie_id) if movie_id else None
                    
                    if poster_url:
                        st.image(poster_url, use_column_width=True)
                    else:
                        st.info("🖼️ No poster")
                    
                    st.markdown(f"<div class='movie-title'>{movie_title}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='movie-score'>⭐ {similarity_score}% Match</div>", unsafe_allow_html=True)
            
            # Add new row after every 5 movies
            if (idx + 1) % 5 == 0 and idx < len(recommendations) - 1:
                cols = st.columns(5)
    
    else:
        st.error("❌ No recommendations found")

else:
    st.info("👈 Select a movie from the dropdown to get started!")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #8b949e; font-size: 12px; margin-top: 20px;'>
    <p>🎬 Movie Recommendation Engine | Powered by Machine Learning</p>
    <p>TMDB API for Movie Data & Posters</p>
</div>
""", unsafe_allow_html=True)


