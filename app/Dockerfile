FROM python:3-slim

WORKDIR /

RUN pip install flask prometheus_client
COPY app.py /app.py

STOPSIGNAL SIGINT
CMD ["python", "/app.py"]
