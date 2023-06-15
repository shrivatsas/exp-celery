from celery import Celery

broker_transport_options = {
    'predefined_queues': {
        'celery': {
            'url': 'http://localhost:4566/000000000000/sample-queue'
        }
    }
}

app = Celery('tasks', broker_url='sqs://localstack:localstack@localhost:4566', broker_transport_options=broker_transport_options)

@app.task(rate_limit='10/m')
def add(x, y):
    return x + y