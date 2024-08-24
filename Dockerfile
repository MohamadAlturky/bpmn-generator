FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8055


CMD ["fastapi", "run","app/main.py", "--host", "0.0.0.0", "--port", "8055"]