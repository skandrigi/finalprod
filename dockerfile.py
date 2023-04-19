# Use the official Python image as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the command to start the server
CMD [ "flask", "run", "--host=0.0.0.0" ]
