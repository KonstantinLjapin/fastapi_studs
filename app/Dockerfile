FROM python:3.11-slim-buster
LABEL authors="lyapin"

RUN mkdir /app
WORKDIR /app/app


COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["python3", "main.py"]