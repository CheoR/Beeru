# FROM python:3-alpine3.10

# WORKDIR /app

# COPY Pipfile Pipfile.lock /app/

# COPY . /app

# EXPOSE 3000

# CMD ["flask" "--app" "src" "run" "--debug"]

FROM python:3.10.11-alpine
RUN pip install pipenv

ENV PROJECT_DIR /usr/local/bin/src/app

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

# --system --deploy
RUN pipenv install --deploy --ignore-pipfile

CMD ["flask" "--app" "src" "run" "--debug"]
