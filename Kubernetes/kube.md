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

 - Kubelete: This is an agent of k8 and its the one running the show. Over sees all processes in the cluster. It works for me. I think i want to know inside the node, kubelete gives me the information.(how many pods do u have, are they running, is there a problem) This is the single point of contact inside the node. If you lose contact with kubelete, you have lost the node. 

- Docker: Needed in each node to make  containers. This is an agent for docker-engine to create containers in each node. 

- Kubeproxy: As long as you here the work "proxy" in IT. It has something to do with networking. kube proxy is a port that manages networking. If you deploy the application and you see the app in the browser, its the proxy that exposes the app the external.Its a port and not an agent. If the proxy is not working, your app wont connect to the network. 

If the control plane controls the cluster, and the cluster is just an envelope around the node, therefore, the control plane controls the node not the cluster. 

Also, if the single point of contact in the node is kubulete, therefore control plane talks or communicates with kubelete. 

The cluster is the backend, the human being cant talk to the cluster. The human being talks to the control plane, and the control plane talks to the node (cluster). 

Forexample, UI (frontend)-> API -> Database(backend).

Here, the control plane is the UI and the node is the backend. 

## The master (Control Plane)
We have 4 core elements in the control plane. 

1. **Scheduler:** Its in charge of pod scheduling. This tells where the pod will be created. Which node to create the pod. etc. 

2. **Controller manager:** Controls and manages everything about the cluster. 

3. **etcd:** This is a database. it stores information. 

4. **API Server:** None of the kubernetes components talk to each other, because they were developed/written in different language. Therefore, The ApI server is there to make the translation to ensure communication between components like docker, kubelet, etcd, scheduler etc. 

![Alt text](image-4.png)
Forexample, if i want to create more pods, I talk to the controller manager, which sends a message to the scheduler through the APi server, the scheduler looks for the node with less pods and create a pod on that node (talks to kubeletes to find which node to create a pod). kubetes talks back to scheduler through the ApI server. 

## Kube config
Kubernetes has maximum security. We dont directly talk to the API-server. The API on our virtual machine talks to the API-server, using a key called kube-config key. When you create an account, k8 gives you the config key for authentication. 
![Alt text](image-3.png)
