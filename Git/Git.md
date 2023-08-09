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
## Code Review and Pull Requests
This process enables us to protect the main branch from any errors and bugs from other contributors. We carefully review any content they commit from their branches before we merge it into the main branch.
Therefore, we have to make a pull request to their branch in order to review their content before merging with the main branch. 

This also helps to resolve a merge conflict. This happens when 2 people are modifying the same thing at the same time. This happens when you are working in the same branch

## Pull Request Template
This is a document/form that other collaborators have to fill in before merging their branch to the main branch. When they submit a pull request to the reviewer, they have to explain what exactly they were doing. 

You have to create a directory called .github inside the repository, and inside this directory, you create a rmarkdown file with the diffeent questions you want other people to answer when they do a pull request
```
mkdir .github
touch Pull_Request_Template.md
vim Pull_Request_Template.md
```
## Gitignore file
In this file, you add all the files or directories that you dont want git to track. When you do git commits and push, the changes in the files or directories listed in the gitignore will not be tracked.
```
touch .gitignore  #Added gitignore file
##List all the folders or files that you dont want git to track
Data  
manuscripts
/manuscripts/drafts/thesis.doc    #for a specific file, you have to put the path to the file 
```
Git will stop tracking files Data and manuscripts 






## Readme File
This is a markdown file that is used as a log of every change made in a repository.
The # controls the font size depending on what you want
#### Bold and italic
The * can either make words bold or italic. if its one it makes it italic and if its 2 it makes it bold. forexample here, this *word* is italic while this **word** is bold. 

You can create lists, create tables, etc 
#### Tables with rows and columns
You can create tables using the pipe (|) as the column separate and (-) to create line to make header. See below.

|Item   | Unit | Price (UsD) | Status    |
|-------|------|------------|-------------|
|keyboard|1    |300         |  Bought     |
|keyboard|1    |300         |Bought       |
|keyboard|1    |300         |Bought       |
|keyboard|1    |300         |Bought       |

## Code Block
1. using the ` key.
To paste a simple code block, you can use three (`) S
   
2.  Code block with the syntax of the language
You still using the three 
#### Adding Link
To add a link you open the ([) to add the message like click here and then use the brackets to add the link. Forexample [Here](https://github.com/Mujjabi) is the link to my github account. Remember to not put space between the closing ] and the opening (, otherwise it will look like this [Here] (https://github.com/Mujjabi). 

#### Adding Images
To add images to the markdown file, 
- Create a folder called images and load all the Images you want to display or put in readme file.
- name your images
- Use a syntax below to display images
  ```
  ![](/absolute path of the image)
  ![](/folder_images/image1.jpg)
  ```
## Organization account creation
This is when a company creates an organizational account that contains all the repositories of that company. People within the company can be added to specific repositories 
and they can collaborate within that repository. 
You create a github account using th company email and the company sends you an invitation to join the company organizational account and repositories. 
DO NOT USE YOUR PERSONAL EMAIL to create this account. 

![image](https://github.com/Mujjabi/DevOps/assets/60195025/75c9d91b-8e82-41d7-83b1-f1af551966c3)












