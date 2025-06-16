# 🎧 Smart Music Recommender

An intelligent music recommendation system that suggests similar tracks based on learned audio patterns, artist data, and user-selected input. Built with Python, scikit-learn, and Gradio — and runs entirely in Google Colab!

## 🚀 Features

- 🎵 **Song-Based Recommendations**: Select any song (e.g., *Believer*, *Shape of You*) to get personalized suggestions.
- 🔊 **Audio-Aware Modeling**: Uses features like *danceability*, *energy*, *valence*, and *tempo*.
- 🧠 **ML-Powered**: Trained a `RandomForestClassifier` to learn musical patterns.
- 🗣️ **English-Only Filter**: Ensures recommendations remain linguistically relevant.
- 👨‍🎤 **Artist Name Display**: Shows artist alongside track name.
- ▶️ **Live Audio Previews**: Play 30-second previews of recommended tracks (where available).
- 🖱️ **Interactive UI**: Powered by Gradio with dropdowns and real-time inference.


## 🛠️ Tech Stack

| Tool            | Use Case                        |
|----------------|----------------------------------|
| `Python`        | Core programming language        |
| `Pandas`        | Data preprocessing and cleaning  |
| `scikit-learn`  | ML model training & inference    |
| `Gradio`        | Web UI for the recommender       |
| `Hugging Face`  | Spotify dataset integration      |
| `Google Colab`  | Runtime & deployment             |


## 📁 Project Structure

├── app.py                 # Gradio Web App (main UI + ML logic)
├── model_utils.py         # Model training & feature handling
├── preprocess.py          # Dataset filtering and transformation
├── sample_inputs.py       # List of display names for dropdown
└── requirements.txt       # Package requirements

## 📦 Installation

You can run this project locally or in **Google Colab**.

### Option 1: Colab (Recommended)
1. Open `app.ipynb` notebook in Google Colab.
2. Run all cells to launch the live app.
3. Interact via the Gradio link at the bottom.

### Option 2: Local

git clone https://github.com/your-username/smart-music-recommender.git
cd smart-music-recommender
pip install -r requirements.txt
python app.py

## 📊 Dataset

We used the [`maharshipandya/spotify-tracks-dataset`](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset) hosted on Hugging Face. The dataset includes:

- 114k+ tracks
- Audio features (danceability, energy, etc.)
- Metadata: artist, album, language, genre, etc.

## 🧠 ML Approach

- **Model**: RandomForestClassifier (genre prediction)
- **Input**: Audio feature vector of selected track
- **Output**: Top N similar tracks based on learned genre patterns

## 🤝 Acknowledgements

- Hugging Face for the Spotify dataset
- Gradio for the effortless deployment tools
- scikit-learn for the ML utilities

## 📬 Contact

For questions, feedback, or collaborations:
**Imaad Fazal**  

## 📝 License

This project is licensed under the [MIT License](LICENSE).

**#MachineLearning #MusicRecommender #Spotify #Gradio #Python #Colab #OpenSource**
