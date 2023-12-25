# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the application files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install alembic
# Copy wait-for-it.sh into the image
COPY wait-for-it.sh /app/wait-for-it.sh

# Make wait-for-it.sh executable
RUN chmod +x /app/wait-for-it.sh

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]