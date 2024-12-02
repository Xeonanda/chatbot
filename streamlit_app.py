import streamlit as st
import requests
import joblib
import json

@st.cache_resource
def download_model():
    model_url = "https://your-cloud-storage-url/model.pkl"
    response = requests.get(model_url)
    with open("model.pkl", "wb") as f:
        f.write(response.content)
    return joblib.load("model.pkl")

@st.cache_data
def load_json():
    json_url = "https://your-cloud-storage-url/config.json"
    response = requests.get(json_url)
    return json.loads(response.content)

model = download_model()
config = load_json()

st.title("My Custom Streamlit App")
st.write("Model and configuration loaded successfully!")
