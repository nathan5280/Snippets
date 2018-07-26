# Celery on RabbitMQ
Starting simple with Celery.  Working from this 
[Tutorial](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html).

Celery is a server that will run multiple copies of your python model script on true 
independent threads.  This eliminates the GIL issue when running threads inside of the 
normal Python interpreter.  Celery handles all of the interprocess communications
between your server application and the background Celery server.  This
communication is done through a message broker.  In this example RabbitMQ
is used.   

*Notes:
* There are additional setup steps for RabbitMQ and Celery.
* There are additional startup steps to make sure Celery and RabbitMQ
are running and pointed to your source Python Model Scripts.

## Install RabbitMQ
```commandline
http://www.rabbitmq.com/install-debian.html
```
You will probably need to install erlang first.

After install check that rabbitmq is up and running.
```commandline
service rabbigmq-server status
```

## Setup RabbitMQ

* user: celery_user
* password: celery_pwd
* vhost: celery_host
* tag: celery_tag

```commandline
sudo rabbitmqctl add_user <user> <password>
sudo rabbitmqctl add_vhost <vhost>
sudo rabbitmqctl set_user_tags <user> <tag>
sudo rabbitmqctl set_permissions -p <host> <user> ".*" ".*" ".*" 
```

## Install Celery
```commandline
pipenv install celery
```

# Running Applications
## Example 1

### Start Celery Worker
```commandline
cd ex1_first_task
export PYTHONPATH=.

celery -A tasks.tasks worker --loglevel=info
```

### Start Client
```commandline
cd ex1_first_task
export PYTHONPATH=.

python client.py
```

## Example 2
```commandline
cd ex2_next_steps
export PYTHONPATH=.

celery -A tasks.tasks worker --loglevel=info
```

### Start Client
```commandline
cd ex1_first_task
export PYTHONPATH=.

python client/client.py
```
