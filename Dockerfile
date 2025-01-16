# Use the official Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Upgrade pip and install the dependencies
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY google_gen_ai.py .

# Set the environment variable for the Google API key
ENV GOOGLE_API_KEY=your_google_api_key_here

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit application (bind to localhost only)
CMD ["streamlit", "run", "google_gen_ai.py", "--server.port=8501", "--server.address=0.0.0.0"]