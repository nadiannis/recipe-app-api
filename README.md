<div align="center">
  <br>
  <h1>recipe-app-api</h1>
  <p>🍳 A recipe API built with Django REST Framework 🍳</p>
  <br>
</div>

[![Checks](https://github.com/nadiannis/recipe-app-api/actions/workflows/checks.yml/badge.svg)](https://github.com/nadiannis/recipe-app-api/actions/workflows/checks.yml)

## Table of Contents

- [Description](#description)
- [Tech Stack](#tech-stack)
- [Run Locally](#run-locally)
- [Run a Command on a Service](#run-a-command-on-a-service)
- [Contributing](#contributing)

## Description

This is a recipe API built with Django REST Framework (DRF). It's built to learn more about REST API, API Documentation, Docker, GitHub Actions, Clean Code, & Test-Driven Development (TDD).

## Tech Stack

- Language: [Python](https://www.python.org)
- Web Framework: [Django](https://www.djangoproject.com)
- REST API Framework: [Django REST Framework (DRF)](https://www.django-rest-framework.org)
- Database: [PostgreSQL](https://www.postgresql.org)
- API Documentation: [Swagger](https://swagger.io)
- Containerization: [Docker](https://www.docker.com)
- Continuous Integration: [GitHub Actions](https://github.com/features/actions)
- Linter: [Flake8](https://flake8.pycqa.org)
- Code Formatter: [Black](https://pypi.org/project/black) & [isort](https://pypi.org/project/isort)

## Run Locally

- Make sure you have [Docker](https://www.docker.com) installed on your computer.

- Clone the repo.

  ```sh
  git clone https://github.com/nadiannis/recipe-app-api.git
  cd recipe-app-api
  ```

- Build the Docker image.

  ```sh
  docker-compose build
  ```

- Create & start the containers.

  ```sh
  docker-compose up
  ```

  You should now be able to access the app through a browser. Check out the app at [http://127.0.0.1:8000](http://127.0.0.1:8000).

- Stop & remove the containers.

  If you want to stop the app, you can stop & remove the containers by executing this command.

  ```sh
  docker-compose down
  ```

## Run a Command on a Service

You can start a container to execute a one-time command with `docker-compose run --rm <service-name> sh -c "<command>"`.

These are several commands you can execute in the app container.

### Lint the Code

```sh
docker-compose run --rm app sh -c "flake8"
```

### Format the Code

```sh
docker-compose run --rm app sh -c "black ."
```

### Sort Python Imports

```sh
docker-compose run --rm app sh -c "isort ."
```

### Run the Test Suite

```sh
docker-compose run --rm app sh -c "python manage.py test"
```

### Make Migrations

```sh
docker-compose run --rm app sh -c "python manage.py makemigrations"
```

### Apply All Migrations

```sh
docker-compose run --rm app sh -c "python manage.py migrate"
```

### Create a Superuser

```sh
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

## Contributing

If you see something that can be improved, you can open an [issue](https://github.com/nadiannis/recipe-app-api/issues) or create a [pull request](https://github.com/nadiannis/recipe-app-api/pulls).
