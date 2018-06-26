FROM python:2

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/requirements.txt 
RUN pip install -r requirements.txt

COPY . /code

