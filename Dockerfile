FROM python:3.10-slim

WORKDIR /app

# Install Python dependencies
COPY app/requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the app
COPY app/ .

# Run Flask app
CMD ["python", "-u", "app.py"]

