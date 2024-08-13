import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys

def main(args):
    # Authenticate, setup spotipy
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Get first page of tracks
    page = sp.playlist_tracks(args[0])

    idx = 1
    while page:
        # Dump this page to output file
        with open(f"tracks/page{idx}.json", 'w') as out:
            json.dump(page['items'], out, indent=3)
        # Advance to next page, exit if this is the last page
        if page['next']:
            page = sp.next(page)
            idx+=1
        else:
            page = None
        

if __name__ == "__main__":
    main(sys.argv[1:])