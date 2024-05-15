FROM python:3.10.10-alpine
ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/