FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y postgresql-client && apt-get clean \
    && pip install -r requirements.txt
COPY . .

RUN chmod +x ./docker/entrypoint.sh

ENTRYPOINT ["./docker/entrypoint.sh"]
CMD ["postgres", "python", "main.py"]
