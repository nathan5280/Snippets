from celery import Celery

app = Celery('ex2_next_steps.server.celery_srv',
             broker='amqp://',
             backend='amqp://',
             include=['tasks'])

# Optional configuration
app.conf.update(result_expires=3600, )


if __name__ == '__main__':
    app.start()