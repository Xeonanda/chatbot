import streamlit as st
import requests
import json
import os


def download_large_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

google_drive_url = "https://drive.google.com/uc?export=download&id=1Xgt5GrsmwoGXYrJSdZ7WKc3ZohaVeorc"
download_large_file(google_drive_url, "PlantTomatoDisease.h5")

st.write("Large file downloaded")

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

file_path = "PlantTomatoDisease.h5"  # Adjust this to the correct file name

if os.path.exists(file_path):
    st.write(f"File {file_path} exists.")
else:
    st.write(f"File {file_path} not found.")

st.write("Current directory contents:")
st.write(os.listdir())

st.write(f"File size: {os.path.getsize(file_path) / (1024 ** 2):.2f} MB")
