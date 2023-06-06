# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements files to the container
COPY requirements.txt /app/

# Install the production and development dependencies
RUN pip install --upgrade pip --no-cache-dir && \
    pip install -r requirements.txt

# Copy the Flask app code to the container
COPY . /app/

# Set the environment variable for Flask
ENV FLASK_APP=src

# Enable debug mode for hot-reloading
ENV FLASK_ENV=development

# Expose the port on which the Flask app runs
EXPOSE 5000

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]
