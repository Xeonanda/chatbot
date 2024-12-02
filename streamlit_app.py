import streamlit as st
import requests
from tensorflow.keras.models import load_model
import io

uploaded_file = st.file_uploader("Upload your model", type=["h5"])

if uploaded_file is not None:
    # Load the model directly from the uploaded file
    model = load_model(uploaded_file)
    st.write("Model loaded successfully!")
else:
    st.write("Whar")

@st.cache_data
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename

google_drive_url = "https://drive.google.com/uc?export=download&id=1wlW9UOEqk5F2Psynik5FS3J3zZQV-sMU"
filename = "class_names.json"  # Adjust this to the file type
download_file(google_drive_url, filename)

st.write("File downloaded successfully!")