import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json

def main():
    # Authenticate, setup spotipy
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    page = sp.playlist_tracks("2sZipx3jS6c1Ve3NygGaHx")

    # with open('stuff.json', 'w') as out:
    #     json.dump(page, out, indent=3)
    # for i, track in enumerate(page['items']):
    #     print(f"track {i} is {track['track']['name']}")
    
    # page = sp.next(page)
    # for i, track in enumerate(page['items']):
    #     print(f"track {i} is {track['track']['name']}")
    idx = 1
    while page:
        # with open(f"page{idx}.json", 'w') as out:
        #     json.dump(page['items'], out, indent=3)

        with open(f"page{idx}.json", 'w') as out:
            json.dump(page['items'], out, indent=3)
        if page['next']:
            page = sp.next(page)
            idx+=1
        else:
            page = None
        

if __name__ == "__main__":
    main()