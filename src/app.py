import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Activating Spotify credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Getting top tracks for artist
artist_uri = 'spotify:artist:6vjF8XdNoqVRj5G021FBM6'

artist = sp.artist(artist_uri)

results = sp.artist_top_tracks(artist_uri)

tracks = results['tracks']

# Storing track information in DataFrame
data = pd.DataFrame(tracks)

data = data.sort_values(by='popularity')

# Plotting duration vs. popularity 
plt.scatter(data.duration_ms, data.popularity)
plt.xlabel('duration in ms')
plt.ylabel('popularity')
plt.show()