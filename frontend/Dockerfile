# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install flask requests

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
