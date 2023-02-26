FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000