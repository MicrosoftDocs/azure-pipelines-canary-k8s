# Use a specific version of the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app.py .

# Use a non-root user for security
RUN useradd -m appuser
USER appuser

# Set the stop signal
STOPSIGNAL SIGINT

# Command to run the application
CMD ["python", "app.py"]