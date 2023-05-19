FROM python:3.10

# ENV PATH $PATH:$HOME/.local/bin
ENV PROJECT_DIR /src

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# Set the environment variable for Flask
ENV FLASK_APP=src

# # Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

COPY . /${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

EXPOSE 5000

RUN flask init-db

CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
