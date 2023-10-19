# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    clang \
    && apt-get clean

COPY ta-lib /opt/homebrew/opt/ta-lib

#RUN  export PATH="$PATH:$(pwd)"

#RUN  cd /opt/homebrew/opt/ta-lib/ && \
#     ./configure --prefix=/opt/venv --build=aarch64-unknown-linux-gnu && \
#     make && \
#     make install
 

# Create and set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port (assuming it's 8000)
EXPOSE 8000

# Copy your application code into the container
COPY . /app/

# Command to run your FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
