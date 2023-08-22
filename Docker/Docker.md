# DOCKER
[LINK]<https://docs.google.com/presentation/d/1igfOG9fDcBVBl3guRdBPJlsocFp3iJwa/edit#slide=id.p12>
There are different Linux flavors, including ubuntu and centOS, and in order to install some applications, you need a different command to install them. For example, for centOs, you need yum install, while for Ubuntu, you need apt-install.
The problem is that one virtual machine cant be used to run all operations regardless of the flavors of Linux. Therefore we would need multiple virtual machines that would be used to run every time a specific flavor is needed. 

## Animal Analogy
If we have a pregnant goat that is sick and suddenly dies. Can we take the fetus from this goat and implant it into a cat's womb? No no no no. 
However, we can develop an incubator that we can use to incubate the fetus to grow. This incubator can be used to implant any animal, as long as we have the **conditions** that can support the fetus to grow similar to the ones of any other female animal. 

However, we need a system for each animal that can support the incubator to run normally with conditions similar to those of the animal.

## IT Significance
You install docker to your virtual machine. The docker is the system that can support the incubator to function properly. The incubator is the container. 
