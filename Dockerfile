FROM python:3.10.10-slim-buster

WORKDIR /usr/src/app

RUN apt-get update

RUN python -m pip install --upgrade pip

COPY ./requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY ./entrypoint.sh ..
RUN chmod +x ../entrypoint.sh

ENTRYPOINT ["/usr/src/entrypoint.sh"]