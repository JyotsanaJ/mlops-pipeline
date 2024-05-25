FROM python:3.9-slim-buster

WORKDIR /app

COPY app .
# COPY /tests /app
COPY requirements.txt .
COPY makefile .

RUN pip install -r requirements.txt

RUN pytest tests

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]