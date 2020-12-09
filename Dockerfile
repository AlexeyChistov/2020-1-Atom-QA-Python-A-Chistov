FROM python:3.8

WORKDIR /tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
