import streamlit as st
import requests
import tempfile
from tensorflow.keras.models import load_model
import io

# File uploader
uploaded_file = st.file_uploader("Upload your model", type=["h5"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())  # Write file content to temp file
        tmp_file_path = tmp_file.name  # Get the path of the temporary file

    try:
        # Load the model from the temporary file
        model = load_model(tmp_file_path)
        st.write("Model loaded successfully!")
    except Exception as e:
        st.error(f"Failed to load model: {e}")
else:
    st.write("Please upload a model file")

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