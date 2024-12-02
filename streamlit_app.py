import streamlit as st
import requests
import os
from tensorflow.keras.models import load_model
import h5py

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
model_url = "https://drive.google.com/uc?export=download&id=1wlW9UOEqk5F2Psynik5FS3J3zZQV-sMU"

# Specify where you want to store the model in the app's local directory
model_path = os.path.join("models", "PlantTomatoDisease.h5")

# Ensure the model directory exists
if not os.path.exists("models"):
    os.makedirs("models")

# Download the model if not already cached
downloaded_model_path = download_model(model_url, model_path)

# Load the model
if os.path.exists(downloaded_model_path):
    file_size = os.path.getsize(downloaded_model_path)
    if file_size > 0:
        st.write(f"Model file found, size: {file_size / (1024 * 1024)} MB")
        model = load_model(downloaded_model_path)
        st.write("Model loaded successfully!")
    else:
        st.error("The model file is empty!")
else:
    st.error("Model file does not exist!")

try:
    with h5py.File(downloaded_model_path, 'r') as f:
        st.write("Model file opened successfully!")
        # List the contents of the model file
        st.write(f.keys())
except Exception as e:
    st.error(f"Failed to open model file: {e}")