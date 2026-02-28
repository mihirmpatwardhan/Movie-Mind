import pickle
import streamlit as st
import requests
import pandas as pd
import time

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

st.set_page_config(page_title="MovieMind", layout="wide")


def local_css():
    st.markdown("""
    <style>
        .main { background-color: #050505; }

        .top-left-logo {
            position: absolute;
            top: -50px;
            left: -20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo-text {
            color: #E50914;
            font-size: 28px;
            font-weight: 800;
            letter-spacing: -1px;
        }

        .main-header {
            color: #E50914;
            font-size: 70px;
            font-weight: 900;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 5px;
            text-shadow: 0px 10px 30px rgba(229, 9, 20, 0.5);
        }
        .sub-header {
            color: #babbbe;
            font-size: 18px;
            text-align: center;
            margin-bottom: 40px;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.stSelectbox) {
            background: rgba(255, 255, 255, 0.05);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        div.stButton > button:first-child {
            background-color: #E50914;
            color: white;
            font-size: 22px;
            font-weight: bold;
            width: 100%;
            border-radius: 12px;
            height: 60px;
            border: none;
            transition: 0.4s;
            text-transform: uppercase;
        }
        div.stButton > button:hover {
            background-color: #ff0a16;
            box-shadow: 0px 0px 35px rgba(229, 9, 20, 0.7);
            transform: translateY(-3px);
        }

        .movie-card {
            background: #111;
            border-radius: 15px;
            overflow: hidden;
            transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid #222;
        }
        .movie-card:hover {
            transform: scale(1.08);
            border: 1px solid #E50914;
            box-shadow: 0px 20px 40px rgba(229, 9, 20, 0.4);
        }
        .movie-poster { width: 100%; display: block; border-bottom: 2px solid #E50914; }
        .movie-info { padding: 15px; text-align: center; }
        .movie-title { font-size: 16px; font-weight: 700; color: #fff; }
    </style>
    """, unsafe_allow_html=True)


local_css()


@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    try:
        data = requests.get(url, timeout=5).json()
        return f"https://image.tmdb.org/t/p/w500/{data.get('poster_path')}"
    except:
        return "https://www.prokerala.com/movies/assets/img/no-poster-available.jpg"


def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    dist = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    names, posters = [], []
    for i in dist[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        names.append(movies.iloc[i[0]].title)
    return names, posters


st.markdown('<h1 class="main-header">🎬MovieMind</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your Ultimate Cinematic Guide</p>', unsafe_allow_html=True)

movies = pd.DataFrame(pickle.load(open('model/movie_list.pkl', 'rb')))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

_, col_input, _ = st.columns([1, 2, 1])
with col_input:
    selected = st.selectbox("What would you like to watch?", movies['title'].values)
    btn = st.button('Recommend')

st.write("---")

if btn:
    with st.status("🎥 Preparing something great to watch...", expanded=False) as status:
        names, posters = recommend(selected)
        time.sleep(1)
        status.update(label="🌟 Ready to Watch? Here You Go!", state="complete", expanded=False)

    st.balloons()

    cols = st.columns(5, gap="large")
    for i in range(5):
        with cols[i]:
            st.markdown(f'''
                <div class="movie-card">
                    <img class="movie-poster" src="{posters[i]}">
                    <div class="movie-info">
                        <div class="movie-title">{names[i]}</div>
                    </div>
                </div>
            ''', unsafe_allow_html=True)