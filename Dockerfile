FROM python:3.10.0a2-alpine3.12
RUN mkdir /app
ADD . /app
WORKDIR /app
ENTRYPOINT [ "/app/script.sh" ]