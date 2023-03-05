FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE $PORT
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
