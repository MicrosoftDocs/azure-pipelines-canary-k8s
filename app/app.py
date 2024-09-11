#!/usr/bin/env python

import os
from random import randrange
from flask import Flask
import logging

# Constants
SUCCESS_RATE = int(os.getenv('SUCCESS_RATE', 50))
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8080))

# Initialize Flask app
app = Flask('sampleapp')

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    if randrange(1, 100) > SUCCESS_RATE:
        logging.error("Internal Server Error")
        return "Internal Server Error\n", 500
    else:
        logging.info("Hello World!")
        return "Hello World!\n", 200

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)