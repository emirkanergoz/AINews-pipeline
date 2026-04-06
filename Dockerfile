FROM python:3.11-slim
#Which Python version to use

WORKDIR /app
#Which folder will we be working in inside the container?

COPY requirements.txt .
#Copy the requirements.txt file to the container

RUN pip install --no-cache-dir -r requirements.txt
#Install the necessary libraries

COPY . .
#Copy the rest of the files to the container

CMD python scraper.py && uvicorn main:app --host 0.0.0.0 --port 8000
#When the container starts, first it should scrape the data, then start the server.