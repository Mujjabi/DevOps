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




