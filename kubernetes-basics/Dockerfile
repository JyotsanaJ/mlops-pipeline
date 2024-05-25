FROM python:3.9-slim-buster

WORKDIR /app

COPY /app /app
COPY requirements.txt .

RUN pip install -r requirements.txt

# COPY /app/model /app/
# COPY /app/helper.py /app/
# COPY /app/main.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# EXPOSE 8000