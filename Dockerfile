FROM python:3.10-slim
WORKDIR /app
COPY . .
CMD ["python", "test_HashTable.py"]
