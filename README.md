🎬 TMDB 5000 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using the TMDB 5000 Movies Dataset. This project leverages Natural Language Processing (NLP) and similarity techniques to recommend movies based on user preferences.

🚀 Project Overview

With the massive growth of digital entertainment platforms, finding relevant movies has become challenging. This project solves that problem by building an intelligent recommendation system that suggests movies similar to a user's choice.

The system analyzes movie metadata such as genres, keywords, cast, and overview to generate accurate recommendations.

📂 Dataset
Source: TMDB 5000 Movie Dataset (Kaggle)
Contains:
Movie titles
Genres
Overview (plot summary)
Cast & crew
Keywords
Ratings & popularity

The dataset includes over 5000 movies, making it ideal for building recommendation systems .

⚙️ Tech Stack
Programming Language: Python
Libraries:
Pandas
NumPy
Scikit-learn
NLTK (if used)
Concepts Used:
Content-Based Filtering
Cosine Similarity
NLP (Text Vectorization)
Feature Engineering
🧠 Methodology
1. Data Preprocessing
Removed null values and duplicates
Selected relevant features (genres, keywords, cast, crew, overview)
2. Feature Engineering
Combined important text features into a single column
Applied text cleaning (lowercase, stemming, tokenization)
3. Vectorization
Converted text into numerical form using:
CountVectorizer / TF-IDF
4. Similarity Calculation
Used Cosine Similarity to compute similarity between movies
5. Recommendation System
Based on user input movie:
Finds similarity scores
Returns top N similar movies
🎯 Features

✅ Movie recommendation based on similarity
✅ Fast and efficient search
✅ Scalable approach for large datasets
✅ Clean and structured data pipeline

📊 Project Workflow
Data Collection → Data Cleaning → Feature Engineering → Vectorization → Similarity Matrix → Recommendation
🖥️ How to Run the Project
1. Clone the Repository
git clone https://github.com/Goal48/TMDB_5000_Recommendation_System.git
cd TMDB_5000_Recommendation_System
2. Install Dependencies
pip install -r requirements.txt
3. Run Notebook / Script
Open Jupyter Notebook:
jupyter notebook
Run the main notebook file step by step
📌 Example
recommend("Avatar")

Output:

Titanic
Guardians of the Galaxy
Star Trek
...
📈 Future Improvements
🔥 Add collaborative filtering (hybrid system)
🎨 Build UI using Streamlit / Flask
🎥 Fetch movie posters using TMDB API
⭐ Add user rating system
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a new branch (feature/your-feature)
Commit your changes
Push and create a Pull Request
📜 License

This project is licensed under the MIT License.

👤 Author

Pius Dutta

💼 Aspiring Data Scientist
🔗 GitHub: https://github.com/Goal48
