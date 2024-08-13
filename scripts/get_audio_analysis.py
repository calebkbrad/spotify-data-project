import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
import csv

def main():
    # Authenticate, setup spotipy
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    page = None
    with open('tracks/page1.json', 'r') as input:
        page = json.load(input)
    
    # print(json.dumps(page, indent=2))
    # print(page[0]['track']['id'])

    # print(json.dumps(sp.audio_features(page[0]['track']['id']), indent=4))

    with open('tracks_with_features.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        headers = ['track_name', 'track_id', 'artists', 'date_added', 'release_date', 'popularity', 'duration_ms', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']
        csvwriter.writerow(headers)
        element = page[0]
        track = element['track']
        track_name = track['name']
        track_id = track['id']
        artists = []
        for artist in track['artists']:
            artists.append(artist["name"])
        artists = "+".join(artists)
        date_added = element['added_at']
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
        csvwriter.writerow(row)


if __name__ == "__main__":
    main()
