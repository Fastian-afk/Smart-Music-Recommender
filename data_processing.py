
import pandas as pd

def load_and_prepare(csv_path='spotify_dataset.csv'):
    df = pd.read_csv(csv_path)

    df['display_name'] = df['track_name'] + ' — ' + df['artists']
    df = df[df['display_name'].notna()]
    df = df[df['track_genre'].notna()]
    df = df[df['duration_ms'] > 60000]  # remove super short clips

    return df
