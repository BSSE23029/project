FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ .

# Run the app
CMD ["python", "main.py"]