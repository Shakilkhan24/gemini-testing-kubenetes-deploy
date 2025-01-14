import streamlit as st
from google import genai
from PIL import Image
import io
import pathlib
import os

# Read the Google API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Sidebar for API key input (optional, for local testing)
with st.sidebar:
    st.header("API Key")
    if not GOOGLE_API_KEY:
        GOOGLE_API_KEY = st.text_input("Enter your Google API key:", type="password")
    
    # Add a "Get API Key" link below the API key input field
    st.markdown("[Get API Key](https://aistudio.google.com/app/apikey)")

# Main app functionality
if GOOGLE_API_KEY:
    client = genai.Client(api_key=GOOGLE_API_KEY)
    MODEL_ID = "gemini-2.0-flash-exp"

    st.header("Choose Generation Type")
    generation_type = st.radio(
        "Select the type of generation:",
        ["Text to Text", "Ask about Image"]
    )

    # Dynamically change the title based on the selected category
    if generation_type == "Text to Text":
        st.title("Text Generation...")
    elif generation_type == "Ask about Image":
        st.title("Ask anything about a Image")

    if generation_type == "Text to Text":
        st.subheader("Text Generation")
        user_input = st.text_area("What do you want to know?'):", height=100)

        if st.button("Generate Text"):
            if user_input.strip() == "":
                st.error("Please enter a text prompt.")
            else:
                with st.spinner("Generating response..."):
                    try:
                        response = client.models.generate_content(
                            model=MODEL_ID,
                            contents=user_input
                        )
                        st.success("Response generated successfully!")
                        st.markdown("### Response:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

    elif generation_type == "Ask about Image":
        st.subheader("...Anything about IMAGE...")
        uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        user_prompt = st.text_area("Any query about the Image? Tell me.'):", height=100)

        if st.button("Generate from Image"):
            if not uploaded_file or not user_prompt:
                st.error("Please upload an image and provide a prompt.")
            else:
                with st.spinner("Processing image and generating response..."):
                    try:
                        # Save the uploaded image to a temporary file
                        img_path = pathlib.Path("uploaded_image.png")
                        img_path.write_bytes(uploaded_file.getvalue())

                        # Open the image using PIL
                        image = Image.open(img_path)
                        image.thumbnail([512, 512])  # Resize for display
                        st.image(image, caption="Uploaded Image")

                        # Generate content based on the image and prompt
                        response = client.models.generate_content(
                            model=MODEL_ID,
                            contents=[
                                image,
                                user_prompt
                            ]
                        )
                        st.success("Response generated successfully!")
                        st.markdown("### Response:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

else:
    st.warning("Please enter your Google API key in the sidebar or set it as an environment variable.")