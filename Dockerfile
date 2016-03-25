FROM python:2.7
MAINTAINER "Ian Laird"

ENV DEBIAN_FRONTEND noninteractive
RUN mkdir -p /srv/http
WORKDIR /srv/http

# Requirements
ADD ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Source Code
ADD src/ /srv/http

# Service Run
CMD gunicorn -b 0.0.0.0:5000 run:app
