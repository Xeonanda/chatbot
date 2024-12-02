import streamlit as st
import requests
import os
import joblib

# Function to download the model if not cached
@st.cache_data
def download_model(url, model_path):
    # Download the file only if it does not exist
    if not os.path.exists(model_path):
        st.write("Downloading model...")
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            with open(model_path, "wb") as f:
                f.write(response.content)
            st.success("Model downloaded successfully!")
        else:
            st.error("Failed to download model!")
    return model_path

# Set the URL of your model (e.g., Google Drive or S3 link)
model_url = "https://drive.google.com/uc?export=download&id=wlW9UOEqk5F2Psynik5FS3J3zZQV-sMU"

# Specify where you want to store the model in the app's local directory
model_path = os.path.join("models", "PlantTomatoDisease.h5")

# Ensure the model directory exists
if not os.path.exists("models"):
    os.makedirs("models")

# Download the model if not already cached
downloaded_model_path = download_model(model_url, model_path)

# Load the model
if os.path.exists(downloaded_model_path):
    model = joblib.load(downloaded_model_path)
    st.write("Model loaded successfully!")
else:
    st.error("Model could not be loaded.")
