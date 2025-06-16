
import gradio as gr
import pandas as pd
import joblib
from utils import get_track_options, get_track_features
from data_processing import load_and_prepare

# Load model and data
model = joblib.load("genre_model.pkl")
df = load_and_prepare("spotify_dataset.csv")

def recommend(track_display_name):
    features = get_track_features(df, track_display_name)
    if features is None:
        return "Track not found.", None
    prediction = model.predict([features])[0]
    recommended = df[df['track_genre'] == prediction].sample(5)
    return list(recommended['display_name']), list(recommended.get('track_id', ['']*5))

options = get_track_options(df)

demo = gr.Interface(
    fn=recommend,
    inputs=gr.Dropdown(choices=options, label="Select a track"),
    outputs=["text", "text"],
    title="🎧 ML Music Recommender"
)

if __name__ == "__main__":
    demo.launch()
