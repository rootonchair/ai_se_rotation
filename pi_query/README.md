# PI query project

A backend that compute pi to arbitrary precision

## Install

Require python3

```
pip install -r requirements.txt
```

## Guide

### Start RabbitMQ

Start RabbitMQ service through docker

```
docker run -d --name some-rabbit -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq:3

```
### Start Celery and Flower

For MacOS, Ubuntu
```
celery -A celery_worker worker --loglevel=info
celery flower
```

For Windows
```
celery -A celery_worker.celery worker --loglevel=info --gevent
celery flower
```

### Start FastAPI

```
uvicorn main:app --reload
```

### Query

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to make query
