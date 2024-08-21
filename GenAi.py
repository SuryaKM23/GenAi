import streamlit as st
import google.generativeai as genai

# Set up the page title and layout
st.set_page_config(page_title="Ask_Mee : )", layout="centered")

# Title for the app
st.markdown("<style>h1 {text-align: center; color: #1a73e8;}</style>", unsafe_allow_html=True)
st.markdown("# Ask_Mee : )")

# Configure Google Generative AI with your API key
genai.configure(api_key="AIzaSyDPHiLm6naB51MXmJyFn6pU_4Wgmq2Biq0")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Inject custom CSS for better UI
st.markdown("""
    <style>
    body {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        margin: 0;
        padding: 0;
    }

    /* Button styling */
    .stButton button {
        background-color: #1a73e8;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 25px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        display: block;
        margin: 0 auto;
        transition: color 0.3s ease;
    }

    .stButton button:active {
        color: #1a73e8;
        background-color: white;
        border: 2px solid #1a73e8;
    }

    /* Footer styling */
    .footer {
        margin-top: auto;
        font-size: 14px;
        color: #555;
        padding: 15px 0;
        text-align: center;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# UI container for the search input and button
with st.container():
    # Input for user question
    text = st.text_input("", placeholder="Type your question here...")

    # Button to trigger the search
    search_button = st.button('Go')

# Handle search button click
if search_button:
    if text:
        try:
            # Send the message to the AI model and get the response
            response = chat.send_message(text)
            # Display the response
            st.markdown("### Response:")
            st.markdown(f"<div class='markdown-text-container'>{response.text}</div>", unsafe_allow_html=True)
        except ValueError as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")

# Footer for branding or additional instructions
st.markdown("""
    <div class="footer">
            Intergated with Google Generative AI
    </div>
""", unsafe_allow_html=True)
