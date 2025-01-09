import streamlit as st
from google import genai
from PIL import Image
import io
import pathlib
import os

# Streamlit app title
st.title("Google Generative AI App")

# Read the Google API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Sidebar for API key input (optional, for local testing)
with st.sidebar:
    st.header("API Key")
    if not GOOGLE_API_KEY:
        GOOGLE_API_KEY = st.text_input("Enter your Google API key:", type="password")

# Main app functionality
if GOOGLE_API_KEY:
    client = genai.Client(api_key=GOOGLE_API_KEY)
    MODEL_ID = "gemini-2.0-flash-exp"

    st.header("Choose Generation Type")
    generation_type = st.radio(
        "Select the type of generation:",
        ["Text Generation", "Image-Based Generation"]
    )

    if generation_type == "Text Generation":
        st.subheader("Text Generation")
        user_input = st.text_area("Enter your text prompt (e.g., 'What's the largest planet in our solar system?'):")

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

    elif generation_type == "Image-Based Generation":
        st.subheader("Image-Based Generation")
        uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        user_prompt = st.text_area("Enter your prompt for the image (e.g., 'Write a short and engaging blog post based on this picture.'):")

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