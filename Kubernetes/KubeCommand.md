# K8s Commands
These are some of the commands in kubernetes 

- Creating a namespace within a cluster
```
kubectl create ns s6christopher
```

- cding or changing to new namespace

```
```

- Deleting a resource that you are not using
```
kubectl delete "object name"  "name of your object"

kubectl delete service  chrisservice
```

- listing all available namespaces in the cluster
```
kubectl get ns | grep s6

s6                Active   16d
s61               Active   2d12h
s6arsene          Active   5m
s6christopher     Active   7s
s6colagene        Active   8d
s6felix           Active   9d
s6jbaafi          Active   9d
s6nic             Active   9d
s6oluwafunmilay   Active   9d
```
  -  Checking details on the pods, includes all infor
```
kubectl get pod -owide
```
 - Checking / describing the services 
```
kubectl describe svc thomisis
```

- Check services running
```
kubectl get svc -A
```
- see if there is a pod disruption budget
```
kubectl get pdb
```
 -  Applying or deploying a manifest
```
kubectl apply -f path/to/your-manifest.yaml

```
-  Knowing APIversion of a resource / object
```
kubectl api-resources | grep deployment

```
