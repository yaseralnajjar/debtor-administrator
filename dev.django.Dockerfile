FROM python:3.6.6-alpine3.8

WORKDIR /debtoradmin/app

# Install libraries
RUN apk update \
    && apk upgrade \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools

# Install python dependencies
COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt

# Copy django app
COPY manage.py .
COPY backend/ ./backend/