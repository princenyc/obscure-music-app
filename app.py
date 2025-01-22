import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
SPOTIFY_CLIENT_ID = "a138efe96c83470c82e28f020b5bf700"
SPOTIFY_CLIENT_SECRET = "f004697b23a544a0933a13e522602dfd"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

st.title("Discover Obscure Music")
st.write("Enter a song and artist to find similar obscure songs!")

song_name = st.text_input("Enter a song name:")
artist_name = st.text_input("Enter the artist name:")

if st.button("Find Similar Songs"):
    try:
        # Search for the song
        results = sp.search(q=f"track:{song_name} artist:{artist_name}", type="track", limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_id = track['id']
            st.write(f"Found: {track['name']} by {track['artists'][0]['name']}")

            # Find recommendations
            recommendations = sp.recommendations(seed_tracks=[track_id], limit=5)
            st.write("Similar Songs:")
            for rec in recommendations['tracks']:
                st.write(f"- {rec['name']} by {rec['artists'][0]['name']}")
                st.write(f"[Listen on Spotify](https://open.spotify.com/track/{rec['id']})")
        else:
            st.error("Song not found. Please try another.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
