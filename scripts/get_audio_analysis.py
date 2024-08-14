import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
import csv

def main():
    # Authenticate, setup spotipy
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    with open('tracks_with_features.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        headers = ['track_name', 'track_id', 'artists', 'date_added', 'release_date', 'popularity', 'duration_ms', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']
        csvwriter.writerow(headers)
        for page_file in os.listdir('tracks'):
            page = None
            with open(f'tracks/{page_file}', 'r') as input:
                page = json.load(input)
            for element in page:
                write_track(element, csvwriter, sp)
        

def write_track(track_info: dict, output: csv.writer, sp: spotipy.Spotify):
    """
    Given the JSON information about a track from an API call, write its information and audio features to a row of csv
    """
    track = track_info['track']
    track_name = track['name']
    track_id = track['id']
    artists = []
    for artist in track['artists']:
        artists.append(artist["name"])
    artists = "+".join(artists)
    date_added = track_info['added_at']
    release_date = track['album']['release_date']
    popularity = track['popularity']
    duration_ms = track['duration_ms']
    audio_features = sp.audio_features(track_id)[0]
    danceability = audio_features['danceability']
    energy = audio_features['energy']
    key = audio_features['key']
    loudness = audio_features['loudness']
    mode = audio_features['mode']
    speechiness = audio_features['speechiness']
    acousticness = audio_features['acousticness']
    instrumentalness = audio_features['instrumentalness']
    liveness = audio_features['liveness']
    valence = audio_features['valence']
    tempo = audio_features['tempo']
    time_signature = audio_features['time_signature']

    row = [track_name, track_id, artists, date_added, release_date, popularity, duration_ms, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature]
    output.writerow(row)



if __name__ == "__main__":
    main()
