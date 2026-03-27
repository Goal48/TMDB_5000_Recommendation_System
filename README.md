# 🎬 TMDB 5000 Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red.svg)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/ML-Content%20Based-green.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 Overview

A sophisticated **Content-Based Movie Recommendation System** that leverages machine learning to discover films similar to your favorites. Built with Streamlit for an intuitive web interface, this system analyzes movie metadata and uses cosine similarity to provide intelligent recommendations from a dataset of 5,000+ TMDB movies.

---

## ✨ Key Features

- **🎯 Intelligent Recommendations**: Uses content-based filtering with cosine similarity to find the most relevant movies
- **📊 Advanced NLP Processing**: Leverages stemming and tokenization for better pattern matching
- **🖼️ Dynamic Poster Display**: Fetches and displays movie posters directly from TMDB API
- **⚡ Real-time Processing**: Instant recommendations with cached data for optimal performance
- **💼 Professional UI**: Clean, modern Streamlit interface with dark theme
- **🔧 Customizable Parameters**: Adjust the number of recommendations (5-20 movies)
- **🔐 Secure API Integration**: Optional TMDB API key integration for enhanced features

---

## 🛠️ Technical Architecture

### Recommendation Algorithm
The system employs a **Content-Based Filtering** approach:

1. **Data Preprocessing**:
   - Extracts genres, keywords, cast, and director information from JSON-structured data
   - Combines metadata with movie overviews to create rich feature vectors
   - Applies Porter Stemming for text normalization

2. **Feature Engineering**:
   - Creates composite "tags" from multiple sources (genres, keywords, cast, crew, overview)
   - Normalizes text to lowercase and removes spaces for consistency
   - Uses CountVectorizer to convert text to numerical features

3. **Similarity Calculation**:
   - Computes cosine similarity matrix between all movies
   - Ranks movies by similarity score to user's selected film
   - Returns top N recommendations with similarity percentages

### Technology Stack
- **Backend**: Python 3.8+
- **Web Framework**: Streamlit
- **ML Libraries**: scikit-learn, NLTK
- **Data Processing**: Pandas, NumPy
- **API Integration**: TMDB API

---

## 📋 Dataset

**TMDB 5000 Movies Dataset** containing:
- 5,000+ movies with comprehensive metadata
- **Files**:
  - `tmdb_5000_movies.csv`: Movie details (genres, keywords, overview, ratings)
  - `tmdb_5000_credits.csv`: Cast and crew information
- **Combined dataset**: 4,809 movies after preprocessing (after removing nulls and duplicates)

**Key Features Used**:
- Movie Title
- Overview/Description
- Genres
- Keywords
- Top 3 Cast Members
- Director
- Movie ID (for poster fetching)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- TMDB API key (optional, for movie posters) - [Get it here](https://www.themoviedb.org/settings/api)

### Installation

1. **Clone or download the repository**
   ```bash
   cd TMDB_5000_Recommendation_System
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Required NLTK Data**
   ```bash
   python -c "import nltk; nltk.download('punkt')"
   ```

4. **Prepare Data Files**
   Ensure these CSV files are in the project directory:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`

### Running the Application

**Start the Streamlit app**:
```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 💡 How to Use

1. **Open the Application**: Navigate to the Streamlit interface in your browser
2. **Configure Settings** (Optional):
   - Adjust the number of recommendations (5-20 movies)
   - Enter your TMDB API key for movie posters
3. **Select a Movie**: Choose from the dropdown menu of 4,800+ movies
4. **View Recommendations**: Instantly see similar movies ranked by similarity score
5. **Explore Posters**: Click on recommendations to see movie details

---

## 📦 Requirements

```
numpy
pandas
nltk
streamlit
scikit-learn
requests
```

For detailed versions, see `requirements.txt`

---

## 🎓 How the Algorithm Works

### Step 1: Data Loading & Merging
- Loads movies and credits CSV files
- Merges on movie title to create a comprehensive dataset
- Handles missing values

### Step 2: Text Preprocessing
```
Raw Data (JSON format):
- genres: [{"id": 28, "name": "Action"}, ...]
- cast: [{"name": "Actor1", ...}, {"name": "Actor2", ...}, ...]
- keywords: [{"name": "keyword1"}, ...]

↓ (Parsed & Flattened)

Extracted Features:
- Action, Adventure, Sci-Fi (from genres)
- Actor1, Actor2, Actor3 (top 3 from cast)
- Director Name (from crew)
- keyword1, keyword2 (from keywords)
- Overview text

↓ (Normalized & Stemmed)

Final Tags:
"action adventur sci-fi actor1 actor2 actor3 director keyword1 overviewtext..."
```

### Step 3: Vectorization & Similarity
- CountVectorizer (max 5,000 features) converts text to TF vectors
- Cosine similarity calculates distance between all movie pairs
- Results ranked from highest to lowest similarity

---

## 📊 Performance Metrics

- **Dataset Size**: 4,809 movies (after cleaning)
- **Response Time**: <1 second for recommendations
- **Recommendation Quality**: Based on 7+ content features (genres, keywords, cast, director, overview)
- **Coverage**: 5,000+ movies available for recommendation

---

## 🔒 API Integration (Optional)

### Setting Up TMDB API
1. Visit [TMDB API Settings](https://www.themoviedb.org/settings/api)
2. Register for a free account
3. Generate an API key
4. Enter the key in the application's sidebar

### Benefits
- Display movie posters for recommendations
- Display movie overview and additional metadata
- Enhanced visual experience

---

## 📁 Project Structure

```
TMDB_5000_Recommendation_System/
├── main.py                      # Main Streamlit application
├── movie-recommendersystem.ipynb # Jupyter notebook with analysis
├── requirements.txt             # Python dependencies
├── tmdb_5000_movies.csv         # Movies dataset
├── tmdb_5000_credits.csv        # Credits dataset
└── README.md                    # This file
```

---

## 🔍 Example Workflow

```
User selects: "The Dark Knight"
    ↓
System finds similar movies based on:
- Action, Crime, Drama genres
- Christopher Nolan (director)
- Christian Bale, Heath Ledger (cast)
- Keywords: superhero, vigilante, etc.
- Plot themes in overview
    ↓
Returns Top 10 Movies:
1. The Dark Knight Rises (98.45% match)
2. Batman Begins (97.23% match)
3. Inception (95.67% match)
...and more!
```

---

## 🎯 Use Cases

- **Movie Enthusiasts**: Discover new films similar to your favorites
- **Streaming Platforms**: Power content discovery features
- **Film Recommendation Services**: Automate personalized suggestions
- **Movie Database Applications**: Enhance user engagement

---

## ⚙️ Customization Options

### In Streamlit App:
- Adjust number of recommendations (5-20 range)
- Add TMDB API key for posters
- Modify recommendation algorithm threshold

### In Code:
- Change `max_features` in CountVectorizer (currently 5,000)
- Adjust stemming algorithms
- Add additional metadata features
- Modify similarity threshold

---

## 🚧 Future Enhancements

- [ ] User rating-based collaborative filtering
- [ ] Hybrid recommendation system (combining content + collaborative)
- [ ] Movie review sentiment analysis
- [ ] Genre-specific filtering
- [ ] Runtime and release year preferences
- [ ] User watchlist feature
- [ ] Recommendation explanation feature

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Dataset Source**: [The Movie Database (TMDB)](https://www.themoviedb.org/)
- **Libraries**: Streamlit, scikit-learn, NLTK, Pandas
- **Inspiration**: Content-based recommendation systems in production

---

## 📞 Support & Contact

For questions, issues, or suggestions:
- Check the Jupyter notebook (`movie-recommendersystem.ipynb`) for detailed analysis
- Review code comments in `main.py`
- Ensure all CSV files are properly placed in the project directory

---

## 🎬 Enjoy Your Movie Recommendations!

*Discover your next favorite movie with AI-powered intelligence.*