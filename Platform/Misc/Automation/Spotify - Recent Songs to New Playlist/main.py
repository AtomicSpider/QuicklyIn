import os
import uuid

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-recently-played playlist-modify-public playlist-modify-private"))

recent_tracks = sp.current_user_recently_played()

playlist_id = sp.user_playlist_create(
    sp.current_user()['id'], f'auto_recent_{uuid.uuid4().hex}')['id']
track_ids = [x['track']['id'] for x in recent_tracks['items']]

snapshot = sp.playlist_add_items(playlist_id, track_ids)
