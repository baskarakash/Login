# Builder stage
FROM python:3.11-slim AS builder
 
WORKDIR /p - Copy - Copy
# ENV PATH="/path/to/pg_config:$PATH"
 
# Copy only the necessary files to install dependencies
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

 

