# 🎧 Smart Music Recommender
**ML-Powered Music Recommendation with Interactive Web UI**

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Recommender-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Model-Random%20Forest-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/UI-Gradio-orange?style=for-the-badge"/>
</p>

---

## 📌 Overview
**Smart Music Recommender** is an interactive machine learning system that suggests **similar songs** based on learned audio patterns and metadata.

The system analyzes features such as **danceability, energy, valence, tempo**, and artist information to generate recommendations. It runs entirely in **Google Colab** and exposes a clean, user-friendly interface using **Gradio**.

---

## 🚀 Key Features
- 🎵 **Song-Based Recommendations** using real audio features  
- 🔊 **Audio-Aware Modeling** (danceability, energy, tempo, valence, etc.)  
- 🧠 **ML-Driven Similarity** via Random Forest learning  
- 🌍 **English-Only Filtering** for linguistic consistency  
- 👨‍🎤 **Artist Attribution** for each recommendation  
- ▶️ **30-second Audio Previews** (where available)  
- 🖱️ **Interactive Web UI** powered by Gradio  

---

## 🛠 Tech Stack
<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="38"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="38"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg" width="38"/>
</p>

**Deployment & Tools**
- Gradio — interactive web interface  
- Hugging Face Datasets — Spotify dataset  
- Google Colab — execution & hosting  

---

## 📂 Project Structure

smart-music-recommender/
│
├── app.py                 # Gradio web app (UI + inference)
├── model_utils.py         # Model training & feature handling
├── preprocess.py          # Dataset filtering and preprocessing
├── sample_inputs.py       # Dropdown display inputs
├── requirements.txt
└── README.md

---

## 🧠 Machine Learning Approach

* **Model**: RandomForestClassifier
* **Input**: Audio feature vector of a selected track
* **Learning Objective**: Capture musical similarity via genre patterns
* **Output**: Top-N recommended tracks aligned with learned representations

This approach balances **performance, interpretability, and scalability** for recommendation tasks.

---

## 📊 Dataset

The project uses the **Spotify Tracks Dataset** hosted on Hugging Face:

* 114,000+ tracks
* Rich audio features (danceability, energy, tempo, valence, etc.)
* Metadata: artist, album, language, genre

---

## 🚀 Running the Project

### Option 1️⃣ Google Colab (Recommended)

1. Open the provided notebook in **Google Colab**
2. Run all cells
3. Launch the live Gradio interface via the generated link

---

### Option 2️⃣ Local Setup

git clone https://github.com/Fastian-afk/smart-music-recommender.git
cd smart-music-recommender
pip install -r requirements.txt
python app.py

---

## 🎯 Why This Project Matters

* Demonstrates **applied ML for recommender systems**
* Combines **data engineering + modeling + UI deployment**
* Shows end-to-end product thinking, not just model training
* Easily extensible to embeddings, deep learning, or collaborative filtering

---

## 👨‍💻 Author

**Imaad Fazal**

📧 Email: [imdufazal@gmail.com](mailto:imdufazal@gmail.com)
🌐 Portfolio: [https://imaad-fazal-portfolio-hub.vercel.app/](https://imaad-fazal-portfolio-hub.vercel.app/)

---

## 🙌 Acknowledgements

* Hugging Face — Spotify dataset
* Gradio — rapid ML app deployment
* scikit-learn — machine learning utilities

---

## 📜 License

This project is released under the **MIT License**.
```
