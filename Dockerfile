FROM python:3.10-slim 

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip 
RUN pip3 install --no-cache-dir -r requirements.txt 


COPY google_gen_ai.py .

CMD ["streamlit", "run", "google_gen_ai.py"]


