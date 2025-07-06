FROM python:3.11-slim

WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 8080

ENTRYPOINT ["python", "-u", "simple-web.py"]