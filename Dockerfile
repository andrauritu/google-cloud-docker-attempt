# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib


# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# COPY .env /app/.env



# COPY ./secrets /app/secrets


# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
# ENV GOOGLE_APPLICATION_CREDENTIALS=/app/secrets/django-service-account.json 
#the line above is  IMPORTANTE 

# Run collectstatic command (optional, if you have static files)
RUN python manage.py collectstatic --noinput




# Expose port 8000 for the application
EXPOSE 8000

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]
