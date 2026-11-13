import streamlit as st
from google import genai
import random

# Page Configuration for an Astronomy Theme
st.set_page_config(page_title="AI_stronomy", page_icon="🔭", layout="centered")

st.title("🔭 AI_stronomy: Visual Astronomy Explorer")
st.write("People have told you to keep your feet on the ground, but your head is in the stars? This is the perfect place for you! Ask any astronomy-related question, and I will provide you with an engaging and accurate answer.")

# Initialize the Gemini Client
client = genai.Client(api_key="AQ.Ab8RN6KKb2zNxISGHRQ3KAB-aLbNsdGawjx8qgEB4bP-MDzgrg")


# A list of fun custom loading phrases
loading_messages = [
    "Scanning the universe for answers...",
    "Traveling at the speed of light, restricted by Earth’s Wi-Fi...",
    "Downloading the universe: 99 percent complete, just trying to locate the missing 95 percent of dark matter...",
    "Please ignore the black hole currently consuming all your RAM while loading..."
    "Calibrating telescopes: Focusing on a galaxy far, far away instead of doing actual work..."
    "Counting stars: Estimated time remaining is roughly 13.8 billion years..."
]

# Pick one randomly
chosen_message = random.choice(loading_messages)

if user_q := st.text_input("Ask me anything about astronomy!", placeholder="e.g., How do black holes form?"):
    with st.spinner(chosen_message):
        user_q = user_q.strip()
        try:
            # Call the Gemini model
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=f"You are an expert astronomer and science communicator. Answer this question engagingly and accurately: {user_q}"
            )
            
            # Display the result
            st.markdown("### Discovery:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")