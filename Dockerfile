FROM python:3.10-alpine

WORKDIR /app

COPY app/requirement.txt .
RUN pip install -r requirement.txt

COPY app/ .

CMD ["python", "app.py"]



