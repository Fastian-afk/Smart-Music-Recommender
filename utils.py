
import pandas as pd

def get_track_options(df):
    return [f"{row['track_name']} — {row['artists']}" for _, row in df.iterrows()]

def get_track_features(df, track_display_name):
    row = df[df['display_name'] == track_display_name]
    if row.empty:
        return None
    return row[['danceability', 'energy', 'tempo', 'valence']].values[0]
