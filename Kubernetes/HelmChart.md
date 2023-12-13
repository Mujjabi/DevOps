# Helm Charts
Here is the helm [presentation](https://docs.google.com/presentation/d/1HkOsQ8KCyJy8ctYK-wSbRtYAq_sLrjmm/edit?usp=sharing&ouid=109697321687504306233&rtpof=true&sd=true)

In K8s, we don not deploy using Kubectl in production. This is only used during development. 
Helm is ***a package manager*** for Kubernetes that simplifies the deployment and management of applications on a Kubernetes cluster.
The meaning of package manager is that it takes all k8s manifest, put them into one package and deploy it.

It uses charts, which are packages of pre-configured Kubernetes resources, to define, install, and upgrade even the most complex Kubernetes applications.

It is basically a compilation of different k8s manifests thta are needed to deploy an application. It changes depending on the specific resources needed to deploy an application.
Take an example of a stateless applications
```
Front end:
   - Deployment
   - service
   - service account
   - secret
   - configmap
   - poddisruptionbudget
   - horizontalpodautoscaler
   - networkpolicy

API
   - Deployment
   - service
   - service account
   - secret
   - configmap
   - poddisruptionbudget
   - horizontalpodautoscaler
   - networkpolicy

Back end:
   - stateful set
   - service
   - service account
   - secret
   - configmap
   - poddisruptionbudget
   - horizontalpodautoscaler
   - networkpolicy
   - persistent volume (optional)
   - persistent volume claim (optional)
   - jobs (optional)
   - cronjobs (optional)
```
Based on the example below, we would have to write 30 yaml files and to deploy them, we have to type kubectl 30 times

Also, if we have to increase thenumber of replicasets, we have to go back an change 3 files (2 deployment and statefulste)

Also, the sequence of deployment of these yaml files is uncertain, if you run one file in a wrong sequence, the application will fail. For example, if you have horizontal autoscaler, which has a matchlabel which has to be read from the statefulset. This will fail. 

This is just for one application, image if you have to handle 30 application. 

With help, we are going to use one file called value file, to combile all these 30 files. Helm knows the order of the sequence of deploymet. 

## Why helm and not kubectl?

#### Templating and Abstraction: 
Helm charts use templates to parameterize Kubernetes manifests, allowing you to customize deployments for different environments or configurations. This makes it easier to manage and maintain the configurations for complex applications, as you can use variables and conditionals in your Helm charts.

#### Reusability: 
Helm charts can be shared and reused across different projects and teams. This reusability simplifies the process of deploying similar applications or components to different clusters or environments.

#### Versioning and Rollbacks:
Helm provides versioning for charts, making it easy to roll back to a previous version if an update causes issues. This helps in maintaining a consistent and reliable deployment process, especially in production environments where stability is crucial.

#### Dependencies Management:
Helm allows you to define dependencies between charts, so you can manage multiple services or components as a single unit. This simplifies the deployment of complex applications with interconnected services.

#### Release Management:
Helm introduces the concept of "releases," which are instances of a chart deployed on a Kubernetes cluster. Helm helps manage the lifecycle of these releases, making it easier to upgrade, rollback, or uninstall applications.

#### Ecosystem and Community:
Helm has a vibrant community and a large ecosystem of charts available in the Helm Hub. This makes it easy to find, share, and contribute to charts, reducing the effort needed to deploy common applications.

**In summary**, Using kubectl directly can be feasible for simple deployments, but as the complexity of your applications and infrastructure grows, Helm provides a more structured and efficient way to manage Kubernetes resources. It helps in maintaining consistency, improving collaboration, and streamlining the deployment process in production environments.

## Helmchart
Helmchart is just a filesytem directory. This is like a directory that has inside directories and files. Each section of the app (front, api, backend) has its own directory, and inside each directory, we have theyaml files. These files are your k8s manifests that you will use to deploy. When you deploy the helmchart, it will deploy all of the manifests inside the helmchart instead of running kubectl 8 times for each section/box (frontend, API, backend)
```
Helm install "helmchart name"
```
This will apply all the 30 manifests.

Helmchart is basically a directory. Inside this directory, we have the following. This is the structure of helmchart.  

#### 1. chart.yaml:
This keeps track of the helm version

#### 2. chart directory:
This is the directory we put dependecies for other charts.Any chart that depends on this chart will be put here. Everything in this directory gets deployed before everything since these are dependecy files.              

#### 3. templates:
This is the directory where we put all our kubenetes manifest. This is like a standard form to apply for anything, a visa, social security, etc. you dont change anythng in the template. The content filled up can change, but the format and structure of the template doesnt change. 

In helm, all the manifests go into the template directory. These need to be templated in order to standardize the structure of these manifests. Just like a I-130 form that is ready to be filled with different information. 

Here is an example of a statefulset manifest. All information that is filled into this template will come from the value.yaml file. 
```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: {{ .Release.Name }}-my-statefulset
  labels:
    app: {{ .Chart.Name }}
    release: {{ .Release.Name }}
    chart: "{{ .Chart.Name }}-{{ .Chart.Version }}"
spec:
  serviceName: "{{ .Release.Name }}-my-service"  # Reference to the associated service
  replicas: 3  # Set the desired number of replicas
  selector:
    matchLabels:
      app: {{ .Chart.Name }}
      release: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Chart.Name }}
        release: {{ .Release.Name }}
    spec:
      containers:
        - name: my-app
          image: "your-container-image:tag"
          ports:
            - containerPort: 8080  # Port on which your application runs
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: [ "ReadWriteOnce" ]
        storageClassName: "standard"
        resources:
          requests:
            storage: 1Gi  # Set the storage size

```

#### 4. values.yaml:

This files is a controller that controls all the manifests in the template.

The values.yaml file in a Helm chart is a default configuration file that allows you to define default values for your Helm chart templates.

It serves as a way to separate configuration from the chart templates themselves, providing a convenient mechanism for users to customize the behavior of the chart without modifying the templates directly.

If you want to modify anything , you make changes in the value file and these changes are deployed in the respective manifest. 

```
# File: mychart/values.yaml

replicaCount: 3

image:
  repository: "your-container-image"
  tag: "latest"

service:
  name: "my-service"

storage:
  size: "1Gi"
  storageClassName: "standard"

```

Just like in dockerhub where we have different images that are written already, that we can pull and use to do anything. Ubuntu, ngnix etc, we can pull and use as we need. 

In helm, we use helm hub, where we can go pull the helmchart and use. This is like dockerhub of helm. All helmcharts, go to this website to download/pull the helmchart. [Bitnami](https://bitnami.com/stacks/containers) is a repository that has all hemlchart, and the company called VMware mantains it.

With helm, you can donwload anything.
```
helm fetch  --untar bitnami/wordpress
```

### Fetching helmchart
- Always try to use the helmchart published by the company that owns the chart. For example, if I want sonarqube helmchart, I will choose the image published by sonarsource since its the owner.

- Just like dockerhub, we select the official image verified by the companies that developed them. 

- Repo-1 is mantained by the US government.

- artifacthub.io/ 

## How do you add a helmchart to your virtual machine
We have to download the repository where the helmchart is located. Just like in git, were we cloned repos, we use the command below to dowload the helmchart.
```
helm repo add [chart_name] repo_url
```
After running this command, and you type `ls`, we wont see anything in this repo. this is because this command simply establishes the connection between your virtual machine and the data center where the chart is located. 

So dont be surprised. 

### Updating the helm repo
Just like in github, when you clone a repo and someone makes changes to the remote repo you cloned, you have to git pull to have the latest version of the repository. 

In helm, you always need to have the latest version of the chart. here is how to update all repos. 

```
helm repo update
```

## Listing all helm repositories

If you have many repositories, and want to list them.
```
helm repo list
```

### Installing a chart / application using the repos added. 

```
helm search repo sonarqube
```
This shows you the repositories where this chart is available. 
You select which repo to use to install the helmchart. And use this command to install the helmchart.
```
helm install sonarqube sonarcubesonarcube   #this deploys sonarqube 
#sonarcubesonarcube is the name of the repo we select. 
```

### List all applications being managed by helm in the k8s cluster

We use this command to list all the applications that are currently being managed by helm in the cluster.
```
helm list
```

### Deleting application
If you have deployed the helmchart for a certain application and want to delete it
```
helm delete 

kubectl get all
```
### Downloading the chart to inspect before deploying
Before installing or deploying the chart, you need download the chart ot inspect it and look at the different manifests it carries. 
```
helm fetch --untar sonarqube/sonarqube-Its
```

When this is downloaded, we can now deploy it after adding content to our value.yaml file. 

```
helm install s6christopher sonarqube-Its
```
- s6christopher will be the name of my applications
- sonaqube-Its is the repo where my chart will be fetched from. 