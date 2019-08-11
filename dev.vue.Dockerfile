FROM node:8.11.4-alpine
ARG GOOGLE_OAUTH_CLIENT_ID

WORKDIR /debtoradmin/app

# Install js dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Build vue app
COPY vue.config.js .
COPY public ./public/
COPY src ./src/
RUN yarn build