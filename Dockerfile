FROM ubuntu:14.04
MAINTAINER "Ian Laird"

RUN \
    apt-get update --fix-missing && \
    apt-get install -y supervisor python python-flask gunicorn && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /srv/http

ADD container-files /
ADD src/ /srv/http

CMD supervisord -n
