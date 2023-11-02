# Kubernetes 
Here is the link to the kubernetes [powerpoint](https://docs.google.com/presentation/d/1WxApP_IwQOfjdVjHrLKoOrlzZXwbWM4M/edit#slide=id.g142824cfa6a_1_26)

### Container Orchestration tool
it can scale, automate, deploy, contenizarize
To orchestrate means it does everything, scaling, automating, deploying, and managing containerized applications. 

## Components of K8
We have 2 components:
   - The master / control plae
   - The cluster / Node group
The master controls the cluster.

![Alt text](<WhatsApp Image 2023-10-23 at 19.39.06_2f1496e6.jpg>)
### Terminologies 
You can have K8 on premise, or you can have it online. When it is on-premise, the components are called master and cluster. However, when you have it virtually, it is called the control plane, and node group. 
On-premise  = Physically present. 
Cloud  = Virtual / online

### Administer K8.
If your K8 is on premise, it means you are responsible for physically buying and installing the k8 infrastructure. If anything happens, you are responsible for fixing it and you control everything. This is called administering k8. 

If someone asks you "do you administer k8? and you say yes, it means you have just told them your k8 is on-premise. 

### In-cloud K8
When K8 is in the cloud, the cloud provider will create the whole infrastructure. The provider will manage the control plane (master) and the devOp will manage the node group (cluster). 
The cloud provider will always guarantee a working control plane if anything happens. However, you are responsible for your node group. If any of the nodes die, the cloud provider will spin new nodes for you. 

### Consuming k8
When k8 is in the cloud and you didn't build the infrastructure, we say you **consume k8**. This is the difference between administering and consuming. Administer on premise, consume on cloud.

### K8 providers:
There are more than 50 cloud providers, but below are the top 5 providers. Even though it is the same k8s, they differ in flavors. Here are the flavors based on the company. 


- Amazon Web Services (AWS): AWS offers Amazon - Elastic Kubernetes Service (EKS) for managing - Kubernetes clusters on their cloud platform.

- Google Cloud Platform (GCP): GCP provides Google Kubernetes Engine (GKE) for running and managing  Kubernetes clusters.

- Microsoft Azure: Azure Kubernetes Service (AKS) is Microsoft's managed Kubernetes offering.

- IBM Cloud: IBM Cloud Kubernetes Service is IBM's managed Kubernetes solution.

- Oracle Cloud: Oracle Cloud Container Engine for - Kubernetes (OKE) is Oracle's managed Kubernetes - service.

- DigitalOcean

- Alibaba Cloud also offers managed Kubernetes services.

## The workflow
![Alt text](<WhatsApp Image 2023-10-23 at 20.34.39_c2665ffd.jpg>)
**The application -> Container -> Pod -> Node -> cluster -> Control Plane**

The application lives inside the container, the container lives inside the pod, the pod lives inside the node, the node lives inside the cluster, the cluster is controlled by the control plane
Node is a common virtual machine. 

Cluster is an envelope around the node

pod is an envelope around the container 

## The Node
These are the 3 major components of the node. They have to be installed on every single node. 

![Alt text](<WhatsApp Image 2023-10-23 at 20.15.55_39308ac3.jpg>)

  
  ## This is a kubernetes cluster. 
![Alt text](image-2.png)

 ### Kubelete: 
 This is an agent of k8 and its the one running the show. Over sees all processes in the cluster. It works for me. I think i want to know inside the node, kubelete gives me the information.(how many pods do u have, are they running, is there a problem) This is the single point of contact inside the node. If you lose contact with kubelete, you have lost the node. 

### Docker:
 Needed in each node to make  containers. This is an agent for docker-engine to create containers in each node. 

### Kubeproxy:
As long as you here the work "proxy" in IT. It has something to do with networking. kube proxy is a port that manages networking. If you deploy the application and you see the app in the browser, its the proxy that exposes the app the external.Its a port and not an agent. If the proxy is not working, your app wont connect to the network. 

If the control plane controls the cluster, and the cluster is just an envelope around the node, therefore, the control plane controls the node not the cluster. 

Also, if the single point of contact in the node is kubulete, therefore control plane talks or communicates with kubelete. 

The cluster is the backend, the human being cant talk to the cluster. The human being talks to the control plane, and the control plane talks to the node (cluster). 

Forexample, UI (frontend)-> API -> Database(backend).

Here, the control plane is the UI and the node is the backend. 

### A Pod
In simple terms, a pod is a collection of containers, its just an envelope around a/containers. 
A "pod" is the smallest deployable and scalable unit in the platform. 

It's a fundamental concept and represents a single instance of a running process in a cluster. 

A pod can contain one or more containers, which are tightly coupled and share the same network namespace and storage volumes. 

In most cases, pods are used to run a single container, but in scenarios where multiple containers need to work closely together, they can be grouped within the same pod.

You need atleast one running container to have a pod. 

**However**, Best practice, dont over load one pod with a lot of containers. From 1 to 3 is okey, but over 3 in making the pod too heavy. You can create another pod and put the other containers, and make the 2 pods communicate if neccesary. 





## The master (Control Plane)
The control plane, also known as the master node, is the central management and control unit of a Kubernetes cluster. It is responsible for orchestrating and managing the entire cluster's operation. 

The control plane consists of several core components:

1. **Scheduler:** Its in charge of pod scheduling. This tells where the pod will be created. Which node to create the pod. etc. 
The scheduler assigns work (pods) to nodes based on resource requirements, constraints, and other policies.

2. **Controller manager:** Controls and manages everything about the cluster. 
The controller manager watches the state of the cluster through the API server and ensures that the desired state, as defined in various controller loops (e.g., ReplicationController, Deployment), is maintained.

3. **etcd:** This is a database. it stores information.  etcd is a distributed key-value store that stores the entire state of the cluster, including configurations and data. It acts as the cluster's source of truth.

4. **API Server:** None of the kubernetes components talk to each other, because they were developed/written in different language. Therefore, The ApI server is there to make the translation to ensure communication between components like docker, kubelet, etcd, scheduler etc. 

![Alt text](image-4.png)
Forexample, if i want to create more pods, I talk to the controller manager, which sends a message to the scheduler through the APi server, the scheduler looks for the node with less pods and create a pod on that node (talks to kubeletes to find which node to create a pod). kubetes talks back to scheduler through the ApI server. 

## Kube config
Kubernetes has maximum security. We dont directly talk to the API-server. The API on our virtual machine talks to the API-server, using a key called kube-config key. When you create an account, k8 gives you the config key for authentication. 
![Alt text](image-3.png)

The key is stored at this path: HOME/.kube/config

If you cant connect to k8s, 2 things you need to do before asking your collegue:

   1. Check if you have the key.  cat ~/.kube/config

   2. Verify if you have the correct key. This is because the key is rotated every 2-3 weeks, for security reasons. (copy your key put it in one file, copy the provided key and put it in another file, use vscode to compare the 2 files. vscode will show u the differences between the 2 files)
### Keypair
Somethings is equal to something. It is used to store important keys to access the cluster.  
![Alt text](<WhatsApp Image 2023-10-24 at 20.03.07_b559ed34.jpg>)

In Kubernetes, a "Keypair" and "Value" typically refer to key-value pairs within resources like ConfigMaps and Secrets. These key-value pairs are used to store and manage configuration data, sensitive information, and other settings in a structured format. 
##### Key-Value Pair:
A key-value pair is a fundamental data structure where data is organized into pairs of keys and their corresponding values. In Kubernetes, key-value pairs are often used to represent configuration settings or data that applications, containers, or pods need to access. Each key is a unique identifier, and its associated value contains the actual data.

# OBJECTS
Objects are all components that makes up a pod. The pod consumes all of them to be functional. These are called the kubernets API objects or k8 objects. Here are the objects broken down. 

### Note: All objects are written in yaml file

## 1. ConfigMap
#### PROBLEM: How do we deal with non sensitive data in K8S? How does Docker-compose fail us?
Docker-compose doesnt separate/split sensitive and non-sensitive information/data in the environment variables, such as user, passwords, etc. Some of the env variables are secrets/sensitive while other are non-senstive. 

**Non-sensitive data:** Data if someone (hacker) gets hold of it, they cant hurt you.
Forexample, if someone accesses your username for you bank account, they cant access your account since they dont have the password. The username is categorized as non-sensitive. 

The good news is that, in k8s, the 2 datas are stored separetely in 2 different objects. In k8s, we manage non-sensitive data using something called a config-map aka CM.

![Alt text](image-6.png)

**A ConfigMap is a Kubernetes resource that allows you to store configuration data as key-value pairs. ConfigMaps are typically used to store non-sensitive configuration information that can be injected into containers as environment variables or mounted as files. They are commonly used for setting application configurations, environment variables, or properties.**

## 2. Secret

**Sensitive Data** : This is data that when accessed can hurt us. This include passwords etc. 
In k8s, this type of data is stored ina  different object called secret. 
This data is stored in Base64 encode format, and k8 will automatically translate it. 

This means you go to the base64 website, paste your password and base64 will give you characters that are equal to your password. Enter this in k8. For config-map, the data is stored in plain text. In k8s, we manage sensitive data using something called secret.

**A Secret is another Kubernetes resource that stores sensitive or confidential data, such as passwords, API keys, and TLS certificates, as key-value pairs. Secrets are designed to keep sensitive data secure and are typically mounted as files or injected as environment variables into containers in a way that is more secure than ConfigMaps.**
### Point to note
The k8 deployable file depends on the secret file but it needs some information such as environmental variables to deploy. In the secret file, we store all the secret data as environmental variables.
For secret infor, only the **KEY** to the information will appear in the deployable file, and not the actual **VALUE** of the secret. The deployable file talks to the secret file to access the actual value.

![Alt text](image-5.png)

for example, when we echo an enviromental variable in the deployable file, the response will be the **'value"** of that variable in the secret file. When you echo the env variable in the deployable yaml variable, spits the actual decoded data in the secret 
```
echo $REDIS_PASSWORD
my_secret_password
```
It wont give us the base64 encoded response cmVkaXM= , it will give us the actual password. 

**The conclusion here is that k8s consumes secret object and configmap as environment variable in a form of key-value pair. we dont have to enter them as env manually as we do in the docker-compose file**

**Also, the pod needs secret and configmap as objects to run**

2 different objects can carry the same name. For example, the configmap and the secret can both have the same name. 

## Inspecting pod objects
Using the command below, we can inspect the status and properties of each object in the pod. 
```
kubectl get deploy, cm, secret, po
```
![Alt text](image-8.png)

We can see that there is one deployment file expected, and it's running.

We can see the configmap with data 6. Meaning that there are 6 environmental variables in our configmap.

We can also see that there is a secret object, with 5 environmental variables.

We can also see the pod, and it's ready and running. 

## 3. Deployment file 
This is a YAML file that is like the docker-compose file, it refers to the config map and the secret after they have been created (separately). This file collects the information from this dependant file (sec and cm), to create a pod. Therefore, ***the deployment gives birth to the pod***

In order for the pod to be created, the configmap and secret have to be created or deployed before the deployment file is run. This is like building a car, the car cannot be driven before all the parts are put together, and the driving comes last after all parts have been built and assembled together. 

# 4. The Scheduler and Demon Set 
It's in charge of pod scheduling. This tells where the pod will be created. Which node to create the pod. etc. 
The scheduler assigns work (pods) to nodes based on resource requirements, constraints, and other policies. 
The scheduler works like a human being, if the node has less pods, it will schedule all the new pods in the node with less pods. For example, if I have 6 nodes, below, the scheduler will put all pods in node 3 (red pods) as shown below. 


Each pod to be scheduled is responsible for going to each node and collecting the metrics of that node (CPU, Memory, Storage and Logs) to the datacenter, in order to know its status and capability before any other pods are added. 


However, if we rely on the scheduler to distribute these pods to collect the metrics, we cant get information of all nodes since pods will only be scheduled on nodes with less pods. 

In order to solve this problem, we have to replicate the same pod to go to all nodes so that it collects the metrics. 
