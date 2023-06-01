FROM python:3.10

# ENV PATH $PATH:$HOME/.local/bin
ENV PROJECT_DIR /src

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# Set the environment variable for Flask
ENV FLASK_APP=src
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=True

COPY . ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

RUN pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000
RUN flask init-db

CMD [ "flask", "run", "--host=0.0.0.0", "--debug", "--port=5000"]
