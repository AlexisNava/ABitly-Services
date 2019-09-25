FROM python:3.6.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV=production

CMD [ "python", "app.py" ]
