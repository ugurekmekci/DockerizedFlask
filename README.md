## DockerizedFlask

This project is a working example of multi-container web application consisting Nginx, Postgres and Flask.

## Installation

Clone repo using the git command and navigate into project directory.

```bash
git clone https://github.com/ugurekmekci/DockerizedFlask.git

cd DockerizedFlask
```

To get the containers running, build the images and then start the services.

```bash
docker-compose build

docker-compose up -d
```

Create DataBase Model

```bash
docker-compose run web /usr/local/bin/python create_db.py
```

- To check running contaiers health and display a live stream of resource usage statistics

```bash
docker ps

docker stats
```

To clean up DB volumes follow steps below respectively.

```bash
docker-compose down -v

docker-compose up -d

docker-compose run web /usr/local/bin/python create_db.py
```

To view the logs
```bash
docker-compose logs
```


Versions:

- Docker Version 19.03.11
- Docker Compose 1.18.0

