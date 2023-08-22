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
