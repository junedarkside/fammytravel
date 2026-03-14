FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir django djangorestframework django-cors-headers psycopg2-binary

# Copy project files
COPY . .

# Create Django project
RUN django-admin startproject api .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
