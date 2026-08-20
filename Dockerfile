FROM python:3.13-slim

WORKDIR /app

COPY app/requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY app/app.py .

EXPOSE 5000

CMD ["python", "app.py"]
