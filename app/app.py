#!/usr/bin/env python

import os
from random import randrange
from flask import Flask
from prometheus_client import start_http_server, Counter
import logging

# Constants
SUCCESS_RATE = int(os.getenv('SUCCESS_RATE', 50))
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8080))
PROMETHEUS_PORT = int(os.getenv('PROMETHEUS_PORT', 8000))

# Initialize Flask app and Prometheus counter
app = Flask('sampleapp')
c = Counter('requests', 'Number of requests served, by custom_status', ['custom_status'])

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    if randrange(1, 100) > SUCCESS_RATE:
        c.labels(custom_status='bad').inc()
        logging.error("Internal Server Error")
        return "Internal Server Error\n", 500
    else:
        c.labels(custom_status='good').inc()
        logging.info("Hello World!")
        return "Hello World!\n", 200

if __name__ == '__main__':
    start_http_server(PROMETHEUS_PORT)
    app.run(host=HOST, port=PORT)