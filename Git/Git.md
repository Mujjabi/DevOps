# Git and GitHub - Version Control System

Version control system is very important in DevOps. Helps to track changes made during project development and keep a version of each stage of the project. 

VCS is a system that document changes made to a file or a set of files. It allows multiple users to manage multiple revision of the same unit of information.

Version control, also known as source control, is the practice of tracking and managing changes to software code. Version control systems are software tools that help software teams manage changes to source code over time.

A version control system records changes to files stored in the system. These files can be source code, assets, or other documents that might be part of a software development project. Teams make changes in groups called commits or revisions

## Control System VCS allows you to:
- Revert the code files back to their previous state
- Recall and revert the entire project back to its previous state
- Compare code changes over specific durations of time
- Find who last modified a piece of code that might be causing an issue or a problem
- Know who introduced a particular issue and when
- Manage version of you code overtime
- keep track of of all changes

## Different VCS Tools used in DevOps
- Git (Most popular): Git is one of the most popular and widely adopted distributed version control systems. It provides excellent support for branching, merging, and distributed development workflows.
Git is known for its speed, flexibility, and robustness. It is commonly used in both small and large-scale projects and is supported by various hosting platforms like GitHub, GitLab, and Bitbucket

- Github: GitHub is a widely used web-based hosting platform for Git repositories. It provides a rich set of features for collaboration, code review, issue tracking, and project management. 
GitHub is known for its extensive community and vast ecosystem of open-source projects.

 
- GitLab: GitLab is another popular web-based hosting platform for Git repositories. It offers a complete DevOps platform with integrated CI/CD pipelines, issue tracking, code review, and container registry.
GitLab is available both as a cloud-hosted service and as a self-hosted solution.

 
- Azure DevOps: Azure Repos is a version control service provided by Microsoft Azure. It supports both Git and Team Foundation Version Control (TFVC) repositories. 
Azure Repos integrates seamlessly with other Azure DevOps services, enabling teams to collaborate on code, perform code reviews, and manage builds and releases in a unified environment.


- Bitbucket: Bitbucket is a web-based hosting platform that supports both Git and Mercurial repositories. It provides features like code review, pull requests, issue tracking, and continuous integration (CI) pipelines. 
Bitbucket is often used for private repositories and offers integrations with other Atlassian products like Jira and Confluence.


- AWS CodeCommit: AWS CodeCommit is a fully managed, highly scalable version control service provided by Amazon Web Services (AWS). 
It supports Git repositories and integrates well with other AWS services, making it suitable for cloud-based development workflows

## Git Hub Console
master branch

- A tag: is a snapshot of the project at a given time. This is the version at a particular time. 

- webhooks: Allows notifications to external services when changes happen. 

### Opening or cloning the repository from remote to local
```
/bash
git clone "https url"
```
### make a directory a git repository
```
mkdir directory
git log #this shows if the folder is a git or not

git init #this makes the folder a git repository 
```
## Generating a token for authentification
This is done in in global setting and token can be set to expire after a certain period of time,
say 90 days, 7 days, 30 days or no expiration. 

The token is then used as a password to clone the git repository to the local machine. 
```
git clone https link
username: 
password: "paste token"
```
This is not used anymore because you have to use the token everytime you need access to the remote repository. instead we use the ssh key authentication. 

## Generating SSH on your local machine for authentication
```
ssh-keygen
Generating public/private rsa keypara
Generating public/private rsa key pair.
Enter file in which to save the key (Jenkins/.ssh/key): #store the key in the ssh directory, create a name for the key. 
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```
If possible, don't put a phrase in case you forget. If you do, write it somewhere to not forget otherwise you won't have access to the repository. 

After generating the SHH key on your local machine, 2 keys will be generated. The private and a public key. Copy the public key and paste it git hub global setting under “SSH and GPG key”. Create a new SHH key and paste the copied public key here. 

After, write this command In your local machine to authenticate access to the remote repository.
```
git config --global core.sshCommand "ssh -i ~/.ssh/key" 
#replace "key" with the name of the private key
```
This will allow your local machine to have access/ clone the remote repository and can pull, push, merge content from other collaborators of the remote repository.

### Configuring your email and username to git.

This helps with tracking who made the commits pushed to the remote repository
```
git config --global user.name "Your Username"
git config --global user.email "your.email@example.com"
```
When you commit changes and push them to the remote repository, we can check these changes and who made them using the command git log
```
root@ip-172-31-82-245:/home/DevOps# git log
commit c87d6ae4c3b6baf809b1be1482490e1898e5cd82 (HEAD -> main, origin/main, origin/HEAD)
Author: Christopher <mujjabic@gmail.com>
Date:   Wed Jul 26 19:57:12 2023 +0000

    Add new directory and its content

commit ce23f485dfa3ac4eacf0520062d27961f287872e
Author: Christopher Mujjabi <60195025+Mujjabi@users.noreply.github.com>
Date:   Mon Jul 24 21:16:52 2023 -0500

    Initial commit
```

## Git workflow
### 1. Staging a directory to the staging area

After cloning the remote repository, you can now add content (directories and files) from your local machine.  

After adding content, you need to stage it from your working directory to the staging area.  
```
git add "folder_name"
git add -A #evertyhing
git add.
```
### 2. Committing the staged work

After staging your work, you need to review and approve it before you commit it from the staging area to the local repository. you can also add a message that describes what you have changed/added in the content. 
```
git commit -m “added the initial code”  #m is for message
```
### 3. Pushing content to the remote repository

After you have committed all the new content and you are ready to upload it to the remote repository, we have to use the command git push to execute this command. 
```
git push
```
### 4. Checking the log or records of all commits

This shows all the activities done to the repository and who did it and when it was done. 
```
git log   #shows who when and what was added
```
### 5. Recovering a certain stage of the workflow
```
git revert "commit Id"
```
### 6. Getting the status of the working directory
```
git status
```
## Creating branches from the main branch
```
git branch  #this shows you your current branch
git branch -a # this shows you all the branches you have
git checkout main  #this moved you to the main branch. this is like cd in linux
git branch submaster #this creates a branch called submaster from the main branch. 
```
If we create a folder under the submaster branch, it is only in this branch not on the main until it is merged to the main

## creating a branch and moving to that branch in one code
```
git checkout -b branchname

git checkout -b superbranch
#this creates a superbranch and moves you to this branch.
```
You can use git switch to do the same function
```
git switch -b submaster
```






