FROM python:3-alpine3.10

WORKDIR /app

COPY Pipfile /app

COPY . /app

EXPOSE 3000

CMD ["flask" "--app" "src" "run" "--debug"]
