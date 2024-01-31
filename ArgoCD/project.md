## Description

Since We have decided to deploy to production our Expresso-shop application, we need to setup a monitoring alert that will  check the application health and also the service managing it.

Prometheus stacks come very handy to us because it is first open-source and very efficient. This will allow us to reduce cost on DataDog and maybe we may decide on the future to retire DataDog. 
Upon checking Prometheus can monitor easily ArgoCD which is the GitOps tool selected for production deployment including all applications deployed via ArgoCD. 
Prometheus is capable of sending all alerts on Grafana for observability  and Alertmanager can send alert to Slack as well 


As a Application Engineer I wan to use Prometheus stacks to monitor ArgoCD including the Expresso-shop app

So that I can be alerted on time .

 

## Definition of done:

ArgoCD servicemonitors are enabled and  deployed

ArgoCD servicemonitors  are available with status UP on Prometheus 

ArgoCD dashboard is created in Grafana 

Alerts are being send to Slack 

the entire code is Merged to Github

Documentations are written and available on Confluence