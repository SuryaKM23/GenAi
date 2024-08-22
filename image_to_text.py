import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

st.title("Image Captioning")

uploaded_file = st.file_uploader("Upload image", type="jpg")
if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    if st.button("Click to Get Caption"):
        output = query(image_bytes)
        caption = output[0] if isinstance(output, list) and len(output) > 0 else "No caption found."
        st.write(caption)
