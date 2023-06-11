FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

RUN flask db.create

RUN flask db.seed

EXPOSE 8080

CMD ["python", "app.py"]