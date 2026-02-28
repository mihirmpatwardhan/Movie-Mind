# 🎬 Movie-Mind: Your Ultimate Cinematic Guide

A Content-Based Movie Recommendation System built using the TMDB 5000 Movies dataset from Kaggle.
**Movie-Mind** helps users discover movies similar to their favorites based on content such as genres, overview, keywords, cast, and crew.

This project is  deployed as an interactive web application using Streamlit.

🔗 **Live Demo (Streamlit):**
https://movie-mind-hfwnehouug8bfuqnoqyb4g.streamlit.app/

---

## 📌 Project Objective

The goal of **Movie-Mind** is to:

* Analyze movie metadata
* Understand content similarity between movies
* Recommend top 5 similar movies instantly

This system uses **Content-Based Filtering** instead of user rating-based recommendations.

---

## 📂 Dataset

Source: Kaggle – TMDB 5000 Movie Dataset

Files used:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

Total Movies: ~5000

---

## 🛠 Tech Stack

**Programming Language**

* Python

**Libraries**

* pandas – Data processing
* numpy – Numerical operations
* scikit-learn – Text vectorization & similarity calculation
* nltk – Text preprocessing and stemming
* ast – JSON string parsing
* pickle – Model serialization
* streamlit – Web application deployment

---

## 🌐 Deployment

**Movie-Mind** is deployed using **Streamlit Cloud**.

**Live App:**
https://movie-mind-hfwnehouug8bfuqnoqyb4g.streamlit.app/

### Features

* Search any movie from the dataset
* Get top 5 similar movie recommendations
* Fast response using precomputed similarity matrix
* Clean and interactive user interface

---

## ⚙️ End-to-End Workflow

### 1. Data Loading & Merging

* Loaded both datasets
* Merged movies and credits using movie title

---

### 2. Feature Selection

Selected key columns:

* movie_id
* title
* overview
* genres
* keywords
* cast
* crew

---

### 3. Data Preprocessing

* Removed missing values
* Converted JSON columns (genres, keywords, cast, crew) into list format
* Extracted:

  * Top 3 cast members
  * Director from crew
* Tokenized overview text
* Removed spaces between multi-word names (e.g., Sam Worthington → SamWorthington)
* Converted text to lowercase

---

### 4. Feature Engineering

Created a combined feature column:

**tags = overview + genres + keywords + cast + crew**

This represents the complete movie content profile.

---

### 5. Text Vectorization

Used:

* **CountVectorizer**
* Max features: 5000
* Stop words: English

This converts textual data into numerical vectors using the **Bag of Words** technique.

---

### 6. Stemming

Applied **Porter Stemmer** to reduce words to their root form.

Example:

* loved → love
* loving → love

This improves similarity matching.

---

### 7. Similarity Calculation

Used **Cosine Similarity** to measure similarity between movie vectors.

Higher cosine similarity → More similar movies.

---

### 8. Recommendation Logic

Process:

1. Identify the selected movie index
2. Retrieve similarity scores
3. Sort scores in descending order
4. Return top 5 most similar movies

---

### 9. Model Saving

Saved processed artifacts using pickle:

* movies.pkl
* similarity.pkl

These files enable fast loading and real-time recommendations in the deployed app.

---

## 🚀 How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Streamlit App

```
streamlit run app.py
```

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── movie_recommendation_system.ipynb
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── movies.pkl
├── similarity.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Concepts Used

* Content-Based Recommendation System
* Natural Language Processing (NLP)
* Bag of Words
* Cosine Similarity
* Feature Engineering
* Model Serialization
* Web App Deployment using Streamlit

---

## 👨‍💻 Author

**Mihir Patwardhan**
Machine Learning & Full Stack Enthusiast

---

