#!/usr/bin/env sh

DNAME="webskel2_devel"

case $1 in
debug)
    docker run \
        --name $DNAME-debug \
        --rm=true \
        -v $PWD/src:/srv/http \
        -p 80:5000 \
        -ti webskel2 \
        python ./run.py
    ;;

test)
    docker run \
        --name $DNAME-test \
        --rm=true \
        -v $PWD/src:/srv/http \
        -p 80:5000 \
        -ti webskel2
    ;;

run)
    docker run \
        --name $DNAME \
            --rm=true \
            -p 80:5000 \
            -ti webskel2
    ;;

build)
    docker build -t $DNAME .
    ;;

*)
    echo "Usage: ./helper [run | test | debug | build]"
    exit 1
    ;;
esac
