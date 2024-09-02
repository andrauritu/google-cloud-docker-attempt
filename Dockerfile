# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV GOOGLE_CLOUD_PROJECT=portfolio-website-429814

# Install PostgreSQL client (not the server)
RUN apt-get update && apt-get install -y postgresql-client

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/


# Run collectstatic command (optional, if you have static files)
# RUN python manage.py collectstatic --noinput

# Expose port 8000 for the application
EXPOSE 8080

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "portfolio.wsgi:application"]
