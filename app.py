import streamlit as st
import openai

# Retrieve OpenAI API key from Streamlit secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# App title and description
st.title("Discover Obscure Music")
st.write("Enter a song and artist to get AI-generated recommendations!")

# Input fields for song and artist
song_name = st.text_input("Enter a song name:")
artist_name = st.text_input("Enter the artist name:")

# Button to generate recommendations
if st.button("Get Recommendations"):
    try:
        # ChatGPT prompt for recommendations
        messages = [
            {"role": "system", "content": "You are a music expert who provides obscure song recommendations."},
            {"role": "user", "content": f"Suggest 5 obscure songs similar to '{song_name}' by {artist_name}. Include a short description for each song."}
        ]
        
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if "gpt-4" is unavailable
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )

        # Parse the API response
        recommendations = response["choices"][0]["message"]["content"]

        # Display the recommendations
        st.write("**AI-Generated Recommendations:**")
        st.write(recommendations)

    except Exception as e:
        # Handle errors
        st.error(f"An error occurred: {e}")

