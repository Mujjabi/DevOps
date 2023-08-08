# Tools to know in AWS (Console Home) 
- EC2 (Elastic Compute Cloud)
- VPC (Virtual Private Cloud)
- S3
- Route 53
- System Manager
- IAM
- Elastic Kubernetes services
- Certificate Manager
- Secret manager
- Elastic Container Registry
- EC2 Dashboard
- Elastic IPs
- Load Balancers
- Snapshots

## Elastic IPs
This is set up so that when you stop your EC2 instance, it doesnt generate a different IP when you restart it again next time

## Auto Scaling Groups 
When server usage increases, and causes a server overload, which causes a need to launch more servers.
For example, on Black Friday, when prices go down, more people shop, causing a crush on the server. Instead of buying more servers, they automatically lunches other instances to manage the traffic, and when it goes below a certain level, the instances shut down automatically. (On-demand instances, only launched when needed).  Instead of adding servers (idle servers) in the data center, aws lunches instances when needed.  
Infrastructure tools (Terraform) - used to automate instances. 

## Dedicated Hosts:
This is a different system from the on-demand model. Here you pay instant for a certain period of time. 

## Key pairs
The key to accessing the server

## Security groups
Its used to filter traffic accessing the server. 

Jenkins - Jenkins

s6christopher - s6christopher

s6nashea - s6nashea
