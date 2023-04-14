FROM node:18-alpine3.16

WORKDIR /code

COPY frontend/package*.json .

RUN npm i

COPY frontend .

CMD [ "npm", "run", "build"]

EXPOSE 5173