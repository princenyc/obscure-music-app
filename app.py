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
        prompt = f"""
        Suggest 5 obscure songs that are similar to the song '{song_name}' by {artist_name}. 
        Include a short description for each song.
        """
        
        # Call the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use "gpt-4" if available
            prompt=prompt,
            max_tokens=250,  # Controls the length of the response
            temperature=0.7  # Adjusts creativity (higher = more creative)
        )

        # Parse the API response
        recommendations = response.choices[0].text.strip()

        # Display the recommendations
        st.write("**AI-Generated Recommendations:**")
        st.write(recommendations)

    except Exception as e:
        # Handle errors
        st.error(f"An error occurred: {e}")
