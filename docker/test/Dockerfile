FROM python:3.11-alpine

RUN apk update && \
    apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    mariadb-dev \
    libmemcached-dev \
    git \
    bash \
    make \
    libffi-dev \
    openssl-dev \
    build-base \
    yaml-dev \
    zlib-dev \
    jpeg-dev \
    tiff-dev \
    python3-dev \
    cython


ADD resources /resources/
RUN python3 --version
RUN chmod +x /resources/test.sh

WORKDIR /resources/

RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r ./requirements.txt

RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/America/Lima /etc/localtime && \
    echo "America/Lima" > /etc/timezone && \
    apk del tzdata

ENV LC_ALL=en_US.UTF-8

ONBUILD ADD app /app/

WORKDIR /app

ENTRYPOINT /resources/test.sh