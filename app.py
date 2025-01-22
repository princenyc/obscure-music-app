import streamlit as st

st.title("Discover Obscure Music")
st.write("Enter a song and artist to find similar obscure songs!")

song_name = st.text_input("Enter a song name:")
artist_name = st.text_input("Enter the artist name:")

if st.button("Find Similar Songs"):
    st.write("Feature coming soon!")
