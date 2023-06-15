```
    pyenv install python3.9
    pyenv local python3.9
    pyenv virtualenv celery
```

```
    sudo apt install libcurl4-openssl-dev libssl-dev
    pip install celery[sqs]
    pip install localstack
    pip install awscli-local[ver1]
```

```
    awslocal sqs create-queue --queue-name sample-queue
    
    {
        "QueueUrl": "http://localhost:4566/000000000000/sample-queue"
    }
```

Insert tasks to the queue
```
    python -m main

    awslocal sqs get-queue-attributes --queue-url http://localhost:4566/000000000000/sample-queue --attribute-names All
```

Start the worker
```
    celery -A tasks worker --concurrency=1 --loglevel=INFO
```