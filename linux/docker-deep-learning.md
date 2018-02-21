# Docker for Deep Learning
This set of notes documents the process for installing Docker on Ubuntu
to support Deep Learning with Tensorflow and Nvidia GPU.  The goal
is to get a Docker container set up on a local machine with an 
Nvidia GPU and then be able to deploy it to AWS.

## Install Docker
Following the steps in the Docker installation manual for Docker CE
```commandline
https://docs.docker.com/install/linux/docker-ce/ubuntu/#extra-steps-for-aufs
```

Follow post installation steps.
```commandline
https://docs.docker.com/install/linux/linux-postinstall/
```

## Install Docker Compose
```commandline
https://docs.docker.com/compose/install/
```

## Inststall AWS Elastic Container Storage CLI
```commandline
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html
```

## Docker Tutorial
Work through this tutorial
```commandline
https://docker-curriculum.com/
```

## Deleting Containers
Delete one or more containers explicitly.
```commandline
docker rm <container_id1> [<container_id2>]
```

Delete all exited containers as follows.
```commandline
docker rm $(docker ps -a -q -f status=exited)
```

## Stoping Container
Stop all running containers.
```commandline
docker stop $(docker ps -q)
```

## Common Commands and Options
* **run --rm** Automatically remove the container when it exits.
* **run -d** Detach the container from the shell it is started from.
* **run --name** Name the container
* **run -p <to-port>:<from-port>** Map the application exposed port to an exposed port.
 

