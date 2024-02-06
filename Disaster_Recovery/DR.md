# Disaster Recovery
### RTO and RPO
RTO (Recovery Time Objective) and RPO (Recovery Point Objective) are two critical parameters in disaster recovery planning that help organizations define their goals and set expectations for the recovery process.
Recovery Time Objective (RTO):

#### Recovery Time Objective
- RTO represents the targeted duration within which a business process or system must be restored after a disruption or disaster.
- It is essentially the maximum tolerable downtime that an organization can afford for a particular system or application.
- RTO is measured in units of time, such as hours, days, or minutes.
- For example, if a company sets an RTO of 4 hours for a critical system, it means that the organization aims to have that system fully operational within 4 hours of a disruptive event

#### Recovery Point Objective (RPO):

RPO defines the acceptable amount of data loss that an organization is willing to tolerate in the event of a disruption or disaster.
It indicates the maximum allowable time gap between the last available backup and the point at which the disruption occurred.
RPO is also measured in units of time and is typically expressed in hours or minutes.
For instance, if a company has an RPO of 1 hour for a specific application, it means that in the event of a failure, the organization is willing to lose, at most, 1 hour's worth of data.

## Backup

Backup refers to the process of creating and storing copies of data to ensure its availability and recoverability in the event of data loss, corruption, accidental deletion, or a system failure. The primary purpose of backups is to safeguard valuable information and provide a means for restoring data to its original state or a previous point in time.


### Full backup, differential backup, snapshot

Full backup, differential backup, and snapshot are different methods used in data backup and recovery strategies. Each serves a specific purpose and has its advantages and disadvantages.

#### 1. Full backup
- A full backup involves copying all selected data at a specific point in time.
- It creates a complete replica of the entire dataset, including all files and folders.
- Full backups are comprehensive but can be time-consuming and resource-intensive, especially as the volume of data increases.
- They provide a standalone copy that can be used for a complete restoration in case of data loss or system failure.
- Typically, full backups are performed periodically, such as daily, weekly, or monthly, depending on the organization's backup strategy.

#### 2. Differential backup
- A differential backup captures the changes made to the data since the last full backup.

- It includes all the data that has been modified or added since the last full backup.

- Differential backups are generally faster than full backups because they only copy the changes made since the last full backup.

- During a restoration process, you need the last full backup and the most recent differential backup to restore the data to its latest state.

- While differential backups can be more efficient in terms of time and storage compared to full backups, they may require more storage space over time as the volume of changes increases.


#### 3. Snapshot
- A snapshot is a point-in-time copy of the data or the state of a system.
- It captures the current state of the entire system or a specific volume without copying all the data.
- Snapshots are often used in virtualized environments, where they can capture the state of virtual machines (VMs) without the need for a full backup.
- Unlike traditional backups, snapshots are typically taken more frequently, providing a more granular recovery point.
- Snapshots are useful for quickly restoring a system to a specific state, but they are not a replacement for traditional backups, as they are often stored on the same storage system and may not protect against certain types of failures.

## Clustered Database
A clustered database, often referred to as a database cluster, is a configuration where multiple servers or nodes work together to provide high availability, fault tolerance, and scalability for a database system. Clustering databases offer several advantages, making them suitable for demanding and critical applications. Here are some key uses and benefits of a cluster database:

#### 1. High Availability (HA):

One of the primary uses of a clustered database is to ensure high availability. In a cluster, if one server or node fails, another node can take over, minimizing downtime and ensuring continuous access to the database.
Clusters employ technologies like failover mechanisms to redirect traffic to healthy nodes, reducing the impact of hardware failures or planned maintenance activities.

#### 2. Fault Tolerance:

Database clusters enhance fault tolerance by distributing data across multiple nodes. In the event of a hardware or software failure on one node, the cluster can still operate with the remaining healthy nodes, preventing data loss or service interruptions.
Redundancy and replication techniques are often employed to maintain copies of data on multiple nodes, reducing the risk of data loss.

#### 3. Scalability:

Clusters support horizontal scalability by allowing the addition of new nodes to the cluster. This enables the database to handle increased workloads and growing amounts of data.
Scaling out, or adding nodes to a cluster, can be a more cost-effective approach compared to upgrading a single server to meet increased performance demands.

#### 4. Load Balancing:

Database clusters often incorporate load balancing mechanisms to evenly distribute incoming queries and transactions among the available nodes.
Load balancing helps prevent individual nodes from becoming overwhelmed with requests, optimizing performance and ensuring efficient resource utilization across the cluster.

#### 5. Performance Improvement:

Clustering databases can enhance performance by allowing parallel processing and distributed computing. Queries and transactions can be executed concurrently across multiple nodes, leading to improved throughput for certain types of workloads.

#### 6. Data Distribution and Replication:

Clusters can employ techniques like data partitioning and replication to distribute data across nodes. This can improve query performance and reduce the risk of data loss in the event of a node failure.
Replication can also be used to create read replicas, allowing for better handling of read-heavy workloads.

#### 7. Disaster Recovery:

Database clusters can be configured to operate across geographically dispersed locations, providing a basis for disaster recovery strategies. In the event of a regional outage or disaster, operations can be shifted to another part of the cluster, maintaining service continuity.

## CronJob

Creating a cron job for backups involves scheduling a task using the cron syntax to execute a backup script or command at specific intervals. 

## S3 BUCKET
Amazon S3 (Simple Storage Service) is a widely used object storage service provided by Amazon Web Services (AWS). An S3 bucket is a fundamental storage container within Amazon S3, used to store and organize data. Here are key characteristics and features of S3 buckets:

1. Object Storage:

S3 is designed for object storage, meaning it allows you to store and retrieve any type of data, such as documents, images, videos, and application backups, as objects within a bucket.

2. Bucket Names:

Bucket names in S3 must be globally unique across all of AWS. This uniqueness is because S3 bucket names are used in URLs to access the stored data, and each bucket name must be unique to ensure proper addressing.

3. Data Durability and Availability:

S3 is designed for 99.999999999% (11 9's) durability of objects over a given year and provides high availability. This makes it suitable for storing critical and highly reliable data.

4. Scalability:

S3 is highly scalable, allowing you to store an unlimited amount of data. You can easily scale up or down based on your storage requirements without worrying about the underlying infrastructure.

5. Data Lifecycle Management:

S3 provides features for managing the lifecycle of your data, including versioning, expiration policies, and transitions between storage classes. This allows you to optimize costs and storage based on the changing access patterns of your data.


## PSQL
This is a postgres client just like kubectl, helm, docker etc.

psql is the command-line interface for interacting with PostgreSQL, a popular open-source relational database management system (RDBMS). 
PostgreSQL is known for its extensibility and compliance with SQL standards. psql provides a powerful and flexible way to interact with PostgreSQL databases directly from the command line.

Here are some common uses of psql:

#### Connecting to a Database:
To connect to a PostgreSQL database, you can use the following command:

```
psql -h hostname -U username -d database_name
```

## Restore

Restoring data from a full backup involves using the backup file or archive created during the full backup process. The specific steps may vary depending on the type of backup tool or method you used.

Always refer to the documentation of the backup tool or method you used for more specific instructions. The commands and procedures may vary based on the backup software, database system, or application in use. If you provide more details about your specific setup, I can offer more tailored guidance.


### AWS CLI
The AWS Command Line Interface (AWS CLI) is a powerful and versatile tool that allows users to interact with various AWS services, including Amazon S3 (Simple Storage Service).