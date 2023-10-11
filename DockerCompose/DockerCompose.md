# Docker-Compose

If you know docker, docker-compose should be easy. Here is the link to the powerpoint for [docker-compose](https://docs.google.com/presentation/d/14k2-5mk6C-G-nZI4hGUH-ZM0jV3MhGjjW13MQpegC8U/edit?usp=sharing). 

There are 2 docker compose
        1. **docker-compose**
        2. **docker compose ---(version2)**

In this class we will be looking at docker-compose not docker compose. 

We need to do YAML first before we do compose. 

Since docker run can only spin one container at a time, we would need to spin so many containers if we have a multiservice (microservices) application that needs multple containers (one container per service). However if we use docker-compose, we can spin multiple containers at once to launch the microservice application. 

Docker-compose is written in YAML and its important to understand the structure. Below is the structure of docker-compose file, **LEARN THIS STRUCTURE**

        1. The version  - Its mandatory 

        2. The services - Its Mandatory 

        3. The declaration  - its optional

1. ### The Version:
This set the version of the compose file and the version number is controlled by the coler by the best practice. if you dont choose the version, docker will choose the lastest. 

The version is written in quotes as shown below:
```
Version: '3'
```

2. ## The Services
This section list all services and each service represent a container that docker will run, so if u have 3 services docker will run 3 containers if you have 10 servuce docker will run 10 containers. 

The service has different options. Some of them are mandatory and some are not. Forexample, the image is mandatory since each service is a container, and the image give birth to the container. 

Other options are optional depending on what you want to do. 
```
Service:
    portainer:  #this is the service
        image: Portainer/portainer-ce:alpine    #the image to be built
        command: -H unix://var/run/docker.sock   #this is like the CMD in dockerfile
        restart: always   #this has 4 options, "no", "on-failure" "always" "unless-stopped'
        volumes:      #this is to persist volume at this location
            - $PwD/devops:/data   
        network:
             -devops
        environment:  #these are environment variables. This can also be added to your   dockerfile while building the image
             - GF_SECURiTY_ADMIN_USER=admin   
        depends_on: 
            - backend   #this tells dockerfile to spin the backend container before spining the portainer container since it depends on it. 
        hostname: portainer  #normally this is just api address, hard to read, so its easy to give it a name instead
        container_name:
        working_dir:   ## put this in your dockerfile when building image instead
        entrypoint:   ## put this in your dockerfile when building image instead
           

```



The minimum number of service you can have is one. if you dont have a service, you dont have a docker-compose file. 



### Network
We add the network section so that its easy for containers to communicate. When you put the containers under the same network, they can easily communicate easily. 

If you have containers that are not under the same network, they wont be able to communicate. 

```
version: '3'

services:
  chris:
    image: ubuntu
    networks:
      - izzy
                             # Add other container-specific configurations if needed

  miles:
    image: golang
    networks:
      - izzy
            # Add other container-specific configurations if needed

  nashea:
    image: nginx
    networks:
      - izzy
             # Add other container-specific configurations if needed

networks:
  izzy:
    driver: bridge
```


## Expose and ports in docker-compose network

### Expose:

The expose option is used to specify ports that should be accessible by other containers within the same Docker Compose network, but it doesn't publish the ports to the host machine. It is a way to declare which ports the container exposes to other services within the same Docker Compose application.

It is typically used when defining internal communication between services within a Compose application.

Exposed ports are not directly accessible from outside the Compose network, and they are only visible to other containers within the same network.
It does not map ports to the host machine.

### ports:  

The ports option is used to publish a container's ports to the host machine, making them accessible from outside the container and the Docker Compose network. It is used to enable external access to services within the container.

With ports, you can specify a mapping from a port on the host machine to a port in the container. This allows external clients to access the service running inside the container using the host machine's IP address and the mapped port.

It is commonly used when you want to access services from the host machine or other machines in your network.

## mapping ports 80:81 for example.

In a container environment (e.g., Docker), when you specify a port mapping like "port 80:81," you are defining a relationship between a port in the container and a port on the host machine.
The left side of the colon (port 80) refers to the port inside the container, and the right side (port 81) refers to the port on the host machine.

This means that when you access port 81 on the host machine, the traffic is directed to port 80 inside the container.

Port mappings are commonly used to allow external access to services running inside a container. For example, if a web server in the container listens on port 80, you can map it to port 81 on the host, so you can access the web server by visiting http://host-machine-ip:81.

Ports are unique, so you can expose the same port twice. this will give you error, "port already allocated"

## STRUCTURE RULES

1. Two or more containers cannot map under the same port. 
2. Two or more containers cannot have the same name
3. Two or more services cannot have the same name.

## The declaration
This is optional and we only use this when we have used network, volume, secrets on services. If one of your services need a network, volume, or network, you have to declare it. 

```

version: '3'

Services:
    Covid19:
       image:
       container-name: 
       ports: 80

    Newyear:
       image:
       container-name: 
       ports: 80
   
Volume:
    db-data:

secrets:
    db-password:
        file: db/password.txt

networks:
    backnet:
    frontnet:
```