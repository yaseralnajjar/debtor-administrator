FROM python:3.6.6-alpine3.8 as setup-python-alpine

# Needed for pycurl
ENV PYCURL_SSL_LIBRARY=openssl

# Install libraries
RUN apk update \
    && apk upgrade \
    && apk add --virtual deps gcc python3-dev linux-headers musl-dev postgresql-dev \
    && apk add --no-cache libpq \
    && apk add --no-cache --virtual .build-dependencies build-base curl-dev \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install pycurl \
    && apk del .build-dependencies

# Intall python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Clean up
RUN apk del deps

# Downloading django app deps finishes here




FROM node:8.11.4-alpine as build-spa-stage
ARG HOST_ENV
ARG GOOGLE_OAUTH_CLIENT_ID

WORKDIR /debtoradmin/app

# install js dependencies
COPY package.json yarn.lock ./
RUN yarn install

# build vue app
COPY vue.config.js .
COPY public ./public/
COPY src ./src/
RUN yarn build

# Build vue app finishes here




FROM setup-python-alpine

ARG IS_BUILD=true
ARG HOST_ENV

WORKDIR /debtoradmin/app
COPY --from=build-spa-stage /debtoradmin/app/ .

COPY manage.py .
COPY backend/ ./backend/

# Collect static files
RUN python manage.py collectstatic --noinput