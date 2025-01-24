# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install flask

# Expose the port
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]
