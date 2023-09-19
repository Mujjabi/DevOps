# DOCKER
Here is the [docker](https://docs.google.com/presentation/d/1QbPGlIae_pS93FOYesO28rXTf_bQXtHBQFFRueFFq30/edit#slide=id.g19f892e151f_0_0) ppt on google drive and the [ppt](https://docs.google.com/presentation/d/1igfOG9fDcBVBl3guRdBPJlsocFp3iJwa/edit#slide=id.p12) 

There are different Linux flavors, including Ubuntu and centOS, and in order to install some applications, you need a different command to install them. For example, for centOs, you need yum install, while for Ubuntu, you need apt-install.
The problem is that one virtual machine cant be used to run all operations regardless of the flavors of Linux. Therefore we would need multiple virtual machines that would be used to run every time a specific flavor is needed. 

## Animal Analogy
If we have a pregnant goat that is sick and suddenly dies. Can we take the fetus from this goat and implant it into a cat's womb? No no no no. 
However, we can develop an incubator that we can use to incubate the fetus to grow. This incubator can be used to implant any animal, as long as we have the **conditions** that can support the fetus to grow similar to the ones of any other female animal. 

However, we need a system for each animal that can support the incubator to run normally with conditions similar to those of the animal.

## I.T Significance
You install docker to your virtual machine. The docker is the system that can support the incubator to function properly. The incubator is the container. 
Inside the container, you put the Centos, ubuntu or the different flavors. Docker is then used to support these containers. So that when you run a centos command on an ubuntu virtual machine, you can tell docker to check the centos container to support the command. 
## Container and Image
The application is inside the image, and the image is inside the container (Incubator), and the incubator is inside the virtual machine. 
The baby heart is inside the baby, the baby is inside the incubator and the incubator is inside the hospital.
Therefore, the application has nothing to do with the virtual machine since it is too far encapsulated inside the container. But Docker is used to support the container when the application is needed to run.

The container is a virtual machine at a small scale. It's like a baby and a mom are the same; the baby is just small. 

The virtual machine/computer is made of libraries, binaries and operating systems. The heaviest part is the operating system. The container is very light because it only has libraries and binaries but it doesnt have an operating system. **However, the container uses the virtual machine's operating system to function**. The container relies on docker to start working (its like the container engine) but depends on the virtual machine to live or function. Just like how the baby depends on the mom's nutritional supply to live. The container uses the VM OS to function. 

## Image
The images is actually inside of the container. It is a combination of libraries and binaries. These communicate with the OP of the machine as its power supply and docker as the engine. So we put the code inside the image, and the container transforms the code into an application. 
Just like a woman's body can receive sperm and transform it into a baby. The woman's body is the container, the sperm is the code, and baby is the application. **In this case, the vagina is the image where the sperm/code is placed**. The image is the environment or gives the environment to host the code. Just like the vagina gives the environment to host the sperm. If you want to modify the application, you have to modify the image or the code. But if you want to troubleshoot the application (misbehaving), u check the container. If the fetus is not good, u check the woman, but if u want to create a superbaby, you modify the sperm. 

## GitHub and Image
The Github repository is where the developer pushes the code to build the application. The DevOps engineer copies the code from GitHub into the image, which is later transformed by the container into an application. 
To modify the application, the devoper has to change the code in github which is then copied back into the image and later the container modifies the application using the new code.

Images are read only (RWX read write execute permission). 
In github, we have the **docker file** and we have the code. The code is compacted/compressed into the docker file to become the image. 

images are kept in **dockerhub**
## Dockerfile and Docker Image

A Dockerfile is a plain text file that contains a set of instructions used to build a Docker image.
It defines the environment, configurations, dependencies, and steps required to create a specific Docker image.
Dockerfiles can include instructions to install software, copy files into the image, set environment variables, configure settings, and more.
Dockerfiles are often versioned along with your source code and are used to ensure consistent and reproducible builds across different environments.
Docker Image:

A Docker image is a lightweight, standalone, and executable software package that includes all the necessary code, runtime, system tools, libraries, and settings to run a piece of software.
Docker images are built from Dockerfiles and can be thought of as snapshots of a specific state of a software application.
Images are immutable, meaning they can't be changed once created. If you need to make changes, you typically create a new image with the desired modifications.
Images can be shared, stored in Docker repositories (like Docker Hub), and used to create and run Docker containers.

The workflow typically involves creating a Dockerfile to define how an image should be built and then using the Docker CLI to build the image from the Dockerfile. 
Once an image is built, it can be used to create Docker containers, which are running instances of the image.

Here's a simplified overview of the process:

Write Dockerfile: Create a Dockerfile that specifies the instructions for building an image.
Build Image: Use the docker build command to build an image from the Dockerfile.
Run Containers: Use the built image to create and run Docker containers.
For example, here's how you might build an image using a Dockerfile named Dockerfile in the current directory:

## CI/CD
Continuous integration and continuous deployment. When an application needs to be modified, you modify the code, integrate it back into the image and get deployed by the container. 

## Docker commands
Just like the git commands, all docker commands start with docker. 

Docker pull: You can download images using docker pull and
Docker images: view images on your virtual machine. Just like when u down a document on your computer, you go to your downloads, or when u download a picture, you go to your gallery. 
docker tag old-image-name new-image-name : Rename image from the old name to a new name. However, the old image is not deleted.
Docker inspect "image name" : to inspect and get information about the image. 


## Repositories and Images
ubuntu is just a repository were we have individuals ubuntu images as listed below. Ubuntu is the family with multiple images
  - ubuntu:18.04
  - ubuntu:20.20
  - ubuntu:16.04
  - ubuntu:latest or ubuntu
If we dont have the name of the image, this means that we are using the latest image of ubuntu. This can be nginx, debian, centos, redhat, etc. 


## Official and None-official Image
Unofficial has not been verified and certified by docker. Forexample ubuntu is certified by docker, but developeasylearning is not certified. Therefore, the presentation of the images differe based on if the image is certified or no. ubuntu:08.04 is a certified image but devopeasylearning.s5ramces:latest is not certified image. This is identified by the slash / in the image name/ 

For nonofficial image, you have the account name before the slash (devopeasylearning), the repository name after the slash(s5ramces) and image name after the : (latest).

Sometimes, the company can pull an official image like ubuntu, add some security packages and then push it back to their own repository under a different image name.

Forexample, we can tag the image ubuntu and rename it to something else.  

docker tag ubuntu:latest  #This is official image of ubuntu
docker tag devopseasylearning/S6:V2.0.0   #This is unofficial image called V2.0.0 from the S6 directory under the account of devopseasylearning. 

### Exercise
1- pull the  image called "postgres:14"

2- tag that image to devopseasylearning/[ENTER YOUR PREFER NAME HERE]: [ENTER A TAG NAME HERE]

3- login to docker using the command 
     docker login 
         * the username is devopseasylearning
         * the password is DevOps2021@

4- push the new image

This is how to do it.
First you need to **tag** the image before you push it. Docker Image tags are simple labels or aliases given to a docker image before or after building an image to describe that particular image. Here, I am labeling postgres14 as "dockerimages" in s6christopher. However, since this is not an official image, we have to login in order to complete the authentication process before docker lets us pull the image. This step is not done for official images like ubuntu. 

```
root@s6christopher@EK-TECH-SERVER03:/student_home# docker tag postgres:14 devopeasylearning/s6christopher:dockerimages
root@s6christopher@EK-TECH-SERVER03:/student_home# docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: devopeasylearning
Password: DevOps2021@
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

After logging in to docker, we are authenticated, and we can now push the image to s6christopher. Here, devopeasylearning is the account to upload the images and s6christopher is the repository. This is like having a google account and a folder. You can upload anything into that folder without logging in. 
```
root@s6christopher@EK-TECH-SERVER03:/student_home# docker push devopseasylearning/s6christopher:dockerimages
The push refers to repository [docker.io/devopseasylearning/s6christopher]
04e017127c16: Mounted from devopseasylearning/s6colince
062ec552e2ba: Mounted from devopseasylearning/s6colince
7fc968c31077: Mounted from devopseasylearning/s6colince
f92e92c27185: Mounted from devopseasylearning/s6colince
100a5a1ba358: Mounted from devopseasylearning/s6colince
47773d43262e: Mounted from devopseasylearning/s6colince
14c8967e9af9: Mounted from devopseasylearning/s6colince
c775f22000b9: Mounted from devopseasylearning/s6colince
99238cd3e254: Mounted from devopseasylearning/s6colince
913650ffc054: Mounted from devopseasylearning/s6colince
fa5241af99da: Mounted from devopseasylearning/s6colince
faf4c37880d0: Mounted from devopseasylearning/s6colince
a2d7501dfb35: Mounted from devopseasylearning/s6colince
dockerimages: digest: sha256:08f848e81ab9501ad9eb1e7948a6e9c2c6db7d63104b77703ad8125cd61b51cc size: 3040
```

Also, you can only push images to the account you have authenticated with. Forexample, on facebook, chris and chris-1 are 2 different accounts. Here I had made a mistake when tagging the images, when I wanted to push, it wasnt working. 
```
root@s6christopher@EK-TECH-SERVER03:/student_home# docker tag postgres:14 devopeasylearning/s6christopher:dockerimages   #I missed the s in devopseasylearning. 
root@s6christopher@EK-TECH-SERVER03:/student_home# docker push devopseasylearning/s6christopher:dockerimages
The push refers to repository [docker.io/devopseasylearning/s6christopher]
An image does not exist locally with the tag: devopseasylearning/s6christopher    #Therefore I had issues here.
```


# Container and Dockerfile
An Image is just a sheet of paper with specific instructions about the container you need.
The first thing you do is tell docker the operating system you want your container to have. For example , I want my container to have ubuntu linux flavor. You created a dockerfile.
The first word of the Dockerfile on each line has to be capitalized. 

Here is an example of a dockerfile with commands. 

```
FROM ubuntu:22.04  #Here you set up the default image in the container. The version required is determined by the developer of the application. The developer will tell u. 
WORKDIR S6_Session  #This helps to set "Devops" as your default directory in the container. Every time you log into the container, this will be your working directory. Docker creates it.
RUN mkdir S6christopher  #This is used to run a command. This command create a directory inside s6-session directory. 
COPY remoterepository .  #copy code from remoterepository to current working directory. 
COPY . .  #copy everything from virtual machine and paste it in my working directory (s6_Session) in the container. I.e copy the entire application code
ADD . .  #This is the same as copy and are interchangeable. But ADD you can copy remote files (equvalent of wget or curl), but COPY doesnt. Download using a link from website. see below
ADD https://en.wikipedia.org/wiki/DevOps_toolchain#/media/File:Devops-toolchain.svg .  #This will download the image and add it here. 
RUN useradd blandine  #created a new user. 
USER blandine  #This changes the default user to blandine. This means, everytime you login into the container, this will be the user instead of root.  
USER 1000 #This can me switched to the UID of the user. If you run the id of the user. Everything that runs below will be executed by the user, therefore they should have the right permission or set them at the end. Forexample, to install something, u need a root. And you cant use Sudo. 
```

## Exercise
There is a git repository located at https://github.com/devopseasylearning/S4-pipelines.git holding application code directories called TF, UI, auth and DB

The default user for the container is called devopseasylearning the application codes mentioned above should be placed in the container directory called app located under the / directory

The base image is ubuntu: 18.04

```
FROM ubuntu:18.04
WORKDIR /app

RUN apt-get update
RUN pat-get install -y git
RUN git clone https://github.com/devopseasylearning/S4-pipelines.git  #Clone the repository inside the container from the virtual machine (copying files and codes)

RUN mv S4-pipelines/TF S4-pipelines/UI S4-pipelines/auth S4-pipelines/DB . #move all these files in my current container directory 
RUN rm -rf S4-pipelines  #delete it since we have copied what we want. 

RUN useradd devopseasylearning  
USER devopseasylearning  #This is put at the end since devopeasylearning doesnt have permission to run some sudo commands above.

```
We can also clone the repository onto our virtual machine so that we dont have to clone the whole repo onto our container

```
git clone https://github.com/devopseasylearning/S4-pipelines.git 
cd S4-pipelines

FROM ubuntu:18.04
WORKDIR /app
COPY TF /app/TF
COPY UI /app/UI
COPY auth /app/auth
COPY DB /app/DB
RUN useradd devopseasylearning  
USER devopseasylearning  #This is put at the end since devopeasylearning doesnt have permission to run some sudo commands above.
```


# Accessing the container
To enter the container, run this code
```
docker run -it s4 bash  
```

# Containalization of an application
- Ask the developer the language of the application. This determines the base image 
- does the application needs to persist any volume?

- Is there any specific pop 

- Does the application need -- to start? 

Forexample, When a devoper tells you to build a docker.file for the application, you need to know what langauge they used.
Forexample golang:1.16 or ubuntu:18.04 etc.

Therefore, when building a docker file, it can handle any golang application that was developed using the libraries of golanf:1.16 or ubuntu:18.04 or less. Should be equal or below, Nothing more than this. If you use golang:1.17 or 20.04, the dockerfile will automatically file. Even if the dockerfile hasnt been changed at all. This is because the libraries of newer images (golang and ubuntu) dont match. 

Dockerfile version needs to be above the application. Always ask the developer which version they are using (golang 1.16), and you choose one equal or above it to develop the docker file. This is what mantaining the dockerfile, changing the "FROM" argument to bump up the Operating System.

## Environment Variables
Environment variables in Docker are a way to pass configuration information and other data to a container at runtime. Docker allows you to set environment variables within a container, either by specifying them in your Dockerfile or by passing them as arguments when running a container. 

You can set environment variables directly in your Dockerfile using the ENV instruction. Here's an example:
```
FROM some_base_image
# Set environment variables
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV APP_ENV=production
```


## Port and Expose command
A port is a like a hole that we put on the container to see whats inside. These holes are called ports. You can have multiple ports. 

In a Dockerfile, the EXPOSE instruction is used to indicate which ports should be made accessible from the container to the host system or other containers. However, it's important to understand that using EXPOSE alone doesn't actually open or publish these ports; it simply documents which ports the container is designed to listen on.

```
FROM some_base_image      # Specify the base image

EXPOSE 80      # Expose a port for the application to listen on

EXPOSE 50, 80, 8080, 5050, 1000, 5000  #select specific ports
EXPOSE 80-1000  # a range of ports 

```

In this example, EXPOSE 80 indicates that your container will be listening on port 80.


## The Volume
Volume is just a storage where the application stores information. Forexample , on facebok, when you connect to facebook and loginto your account, when you upload a foto, it is stored on the volume.

In the context of Docker and containerization, a "volume" refers to a Docker feature that allows you to manage and persist data independently of the container itself. Volumes are used for storing and sharing data between containers, between the host and containers, or simply for persisting data that should survive even if a container is stopped, removed, or replaced.

## CMD or command
This is the first command that will run when your container starts.  Forexample to enter the container via terminal, we run this command

CMD is an instruction in a Dockerfile that specifies the default command to run when a container is started from the Docker image. It defines the executable and any arguments that should be passed to it. The CMD instruction is typically used to provide the primary command or process that should run inside the container when it starts. If you provide multiple CMD instructions in a Dockerfile, only the last one will take effect
```
docker run -it s6 bash

```
With a docker file, we include this command under the command "CMD". If you have multiple CMDs in your docker file, docker will only consider the last CMD
CMD changes based on the language used to build the application. Forexample, images like Ubuntu, nginx, we use bash. 
```
CMD ["python", "app.py"]  #applications built in python

CMD ["bash"]   #Application built with ubuntu

```

CMD ["./my_app"]
CMD ["/bin/bash -c ./my_app"]   #this is the same as the previous 

## ENTRYPOINT
This is also the first command that run when the container start. The entry point is basically specifies the shell that will be used to execute the CMD command. Therefore, CMD and ENTRYPOINT are complimentary and run as a combination. When the container starts, the combination Entrypoint-CMD run. 
The default entry point is /bin/bash -c but this can be changed or over written if the entry point is specified. 
```
CMD ["-b"]

```
If the entrypoint is not specified in the dockerfile as shown below, the entry point will automatically be /bin/bash -c as defaultt. But if the entrypoint is specified, it will override the default, as shown below. 
```
ENTRYPOINT ["top"]
CMD ["-b"]
```




