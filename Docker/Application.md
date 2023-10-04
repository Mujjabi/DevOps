## An Application
Here is the powerpoint to DEL Application [presentation](https://docs.google.com/presentation/d/1zEeNrW_bhAqCiOsQ_cLepwI6mRV3URIy5kW52IaIYvw/edit#slide=id.p). 
### What is an application??

Is a computer software package that performs a specific function for an end user or another application based on carefully designed feature.

*Simple language:* it means application are just simple software that solve a particular need for either users also called customers or other applications. 

Every application on my phone is there to serve a specific need. 

Eg. facebook application help user to connect around the world. Here are examples of applications we use everyday. 

![Alt text](image-2.png)

## Types of Applications
As devop engineers, we deal with 2 types of applications: 
1. Stateless application:

Is an application program that does not save client data generated in one session for use in the next session with the client.

Each session is carried out as if it was the first time and responses are not dependent upon data from a previous session. 

This means this application doesnt require **"volume"** and no **database.**

2. Stateful application. 

Stateful applications save data to persistent disk storage for use by the server, bu client and by the other applications.

An example of a stateful application is a databse or key-value store to which data is saved and retrieved by other applications. 

Therefore, **You need to persist a volume. You need a database.**

Here is how to create database for posgress.

Connection strings - These are environment variables that need to be declared between developer and devop. 

## Created a database
masteruser: s6class
password: s6classs6class
port: 5432

```
root@s6christopher@EK-TECH-SERVER03:/student_home# psql -h s6-database-instance-1.czimqpmzgn63.us-east-1.rds.amazonaws.com -U s6class  -d postgres -p 5432
Password for user s6class: 
psql (12.16 (Ubuntu 12.16-0ubuntu0.20.04.1), server 15.3)
WARNING: psql major version 12, server major version 15.
         Some psql features might not work.
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

postgres=> 
```
Creating more databases
```
CREATE DATABASE "DATABASE NAME" ;
 \l  #checks database list
```

## Microservices
Microservices are the different components of an application. For example, Amazon.com application has all different components that are all containerized into different containers. 
Caching: responsible to "learn" client behavior and suggest similar items to buy.
address: container responsible for adding client names.  Etc
Auth: That lets people to log in
Cart: That lets you add things to your cart
Creditcard: Container that lets you add or use your credit card. 
The bussiness logic is that each component has a role that it contributes to the functionality of the application. 

![Alt text](<WhatsApp Image 2023-10-03 at 20.40.15.jpg>)
When somethings happens, we know which container to check first to solve the issue. 
Forexample if someone says they cant hear, the first thing the doctor checks is the ear. If someone says they cant login, the first thing to check is the login container. 

If the application is running on one container, we call it a **single service application** while if the application is run by multiple container we call it a **microservices application**.

If you do something on the app, the command is sent to the client, the client sends to the API and the API sends to the database, and the response of the database goes back to ApI then to the client.
![Alt text](<WhatsApp Image 2023-10-03 at 21.10.07.jpg>)

## Information flow in the application

UI (User Interface) = Client = frontend.

API (Application Programming Interface) and Database = backend

### The frontend
The client is what we see, what our eyes see. Forexample, facebook app is what I see when i go to facebook.com. When i go to amazon.com, I see the client. 

If I try to login to amazon and I see a 404 error, this means the UI container is down. 

Everything we do on the website, we make an **API call** that triggers a response. All the API calls end up in the backend. The backend is like the foundation of the application. Therefore, when we are building the application, we need to follow a specific sequence, start with the backend (foudation), build the API, then end with the frontend (client). Because all the things done on the client, an api call is made to the backend. 

### The backend
This is what is running behind the scenes.            