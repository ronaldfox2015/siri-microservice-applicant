FROM python:3.11-slim
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt requirements.txt
COPY app/ .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
EXPOSE 80
