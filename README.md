# FAAS Functions

## First FaaS Function
https://blog.alexellis.io/first-faas-python-function/

## Face Detection Example
https://realpython.com/traditional-face-detection-python/

## Installing OpenCV in Raspberry Pi
* https://www.learnopencv.com/install-opencv-4-on-raspberry-pi/
* https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
* https://github.com/Ellerbach/Raspberry-IoTEdge/blob/master/opencv-342.Dockerfile

## Remove all Docker images and containers
https://techoverflow.net/2013/10/22/docker-remove-all-images-and-containers/
```bash
#!/bin/bash
# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi $(docker images -q)
```

## Install faas-cli on Arm32v7
```bash
curl -sSL https://cli.openfaas.com | sudo sh
```

## Create Multi-stage builds to decrease openCV size
https://docs.docker.com/develop/develop-images/multistage-build/