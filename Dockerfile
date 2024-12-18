# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    vim

# Install pycryptodome
RUN pip install pycryptodome

# Set the working directory
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY python.py .

# Run the Python script
CMD ["python", "./python.py"]