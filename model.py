
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(csv_path='spotify_dataset.csv'):
    df = pd.read_csv(csv_path)

    # Feature columns
    features = ['danceability', 'energy', 'tempo', 'valence']
    X = df[features]
    y = df['track_genre']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    joblib.dump(model, 'genre_model.pkl')
    print("Model saved to genre_model.pkl")

if __name__ == '__main__':
    train_model()
