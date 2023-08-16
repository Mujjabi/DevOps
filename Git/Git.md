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
git checkout main  #this moves you to the main branch. this is like cd in linux
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
1. using the (`) key. 
- To paste a simple code block, you can use three (`) S
- This key can also be used to highlight a text or paragraph. Just put it at the begining of that paragraph like this. `Hey my friends`
   
2.  Code block with the syntax of the language
- You still add a code block using the same three symbols, however, at the end, you need to add the naming of the specific langauge below the closing (`). Forexample add .yaml to a docker file. 

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


## Branck Protection
Branch protections is needed to protect the branch so that no one can merge content to the main branch without creating a pull request and seeking approval. 
To add this feature to your github, you might have to upgrade to a different github account that you have to pay for. 
Go to branch protection and add a list of branches that you want to protect. Everytime someone wants to modify the branch, they need to submit a pull request. 

This setting is under settings of a specific repository. 

## Git restore
This restore changes locally. This is only used when you havent commited from the working directory to the local repository. 
These changes are saved but not staged or commited already. 
```
git restore *

```
## Git reset 
There main moded that git reset can do these include : 
- **Mixed reset:** removes commits but reserves changes in the working directory. This is the default option. This basically undoes the commit but saves changes u have been working with.
  
- **Soft reset:**  Removes commits and brings back to the staging area. This is used if u want to make one commit for all changes made. Therefore if made commits already, then make more changes thta need to be committed,you can undo the innitial commits, make the change and make a new commit with all changes before u push.
  
- **Hard reset:** Wipe out changes from working directory and the staging area.All changes disappear everywhere and cant be recovered, BE VERY CAREFUL WITH THIS UNDO COMMAND
These are used in this form
```
$ git log --oneline
01da54f (HEAD -> main, origin/main, origin/HEAD) Testing gitignore
c88c3a7 test
8f16022 gitignore test
ee2fd56 Created a gitignore file and added list of files. modified git.md
2f64e23 Adding links and code blocks
38d9384 Added how to edit readme file
git reset --mixed ee2fd56
```

## Git revert 
This reverts commits that were pushed to public repositories. 
Forexample, All the changes have been pushed and jenkin used them to build the code and make changes to the website. if the customer complains and want the old version of the website, you can use git revert to undo changes pushed to the public. 
```
git log --oneline

01da54f (HEAD -> main, origin/main, origin/HEAD) Testing gitignore
c88c3a7 test
8f16022 gitignore test
ee2fd56 Created a gitignore file and added list of files. modified git.md
2f64e23 Adding links and code block
#we want to recover the first push when we added the links and code block.

git revert 2f64e23
```

## Merge Conflict

This happens when two people are working on the same line or block or code at the same time. 
When one of them tries to push their changes, this creates a merge conflict because git is not sure what changes to save hence creating a merge conflict.
In this case, the 2 people have to talk and decide which changes to commit and delete the other changes. 
Here is when we use the pull request to compare the versions and make the changes necessary. 


## A Git Tag
In git, a tag is a reference or label that is assigned to a specific commit in the repository history. it is a way to mark important points in the development timeline, such as a major release, milestones or significant changes in the software development. 
For example, the release of a program, there are major released that are tagged with the version release name such as **v1.5.0, v1.6.0, v1.7.0** etc. 

Every tag also has a document or note called a **Release note**, that contains all infomation about the released version or the tag. 
To create a tag with the version name, use the code below
```
git tag v1.0.0

git push --tag
```
This will take a snapshot of the project at that particular point of time. This will zip up the project will all the content at that particular tag. 

## Creating a Release and release note
This is done from github, after creating the tag, you can create a release from that tag, 


## Creating a branch at a particular commit
```
git checkout -b feature branch commit id or hash

# for example, creating a brach here.
$ git log  #this displays all commits

commit fc6c38d49f3995c831008274c0e93b9a066624ab (HEAD -> s6christopher, origin/s6christopher)
Author: Chris_VSCode <mujjabi2@illinois.edu>
Date:   Tue Aug 15 19:56:55 2023 -0500

    Ready for 6 figure paycheck

commit 7da06705d68c2cd0138e9dfb0666e076e5961e99 (origin/s7michael, origin/s6tom, origin/s6tia, origin/s6rostaing, origin/s6romeo, origin/s6raoul1, origin/s6ola, origin/s6nic, origin/s6mannars, origin/s6lynda, origin/s6laurent, origin/s6hina, origin/s6dolapo, origin/s6delphine, origin/s6colince, origin/s6colagene, origin/s6arsene, origin/s6Arnauld, origin/main, origin/S6IDRIS, origin/HEAD, main) 
Author: tia12 <58248085+tia12@users.noreply.github.com>
Date:   Tue Aug 15 19:41:09 2023 -0500

    Initial commit
```
Select the particular commit that you want to use to create a brach. Forexample, i want to creat a brach at commit made by Chris_Vscode

```
git checkout -b V1.00 fc6c38d49f3995c831008274c0e93b9a066624ab
git tag V1.00
git push -u branch_name tag_name

git push -u main v1.00
```
## Creating a branch from a specific Tag
```
git checkout -b branch-name tag id
#For example, creating a branch from our initial tag v1.0.0.2

git checkout -b version2 v1.0.0.2
git push
```
## Git Cherry-Pick
The cherry pick is used when collaborating with someone else, and you would like to extract some work from their branch that are not merged to main. This way, no need to merge to the main, one can just get the information directly from the branch of their interest. The other collaborator needs to send you the lasted commit or the commit of the version of their work that you need to pull to your branch. 
Even though you git pull, the branches are extracted to my local machine but the content is still in the individual branches, in order to grab content from a particular branch, you can use the cherry pick as shown below

```
git checkout collaborator-branch
git log --oneline
#copy the id of the commit hash of your interest

git checkout yourbranch
git cherry-pick copied-commit hash

$ git checkout s6hina
Switched to branch 's6hina'
Your branch is up to date with 'origin/s6hina'.

mujjabi2@CPSC-P10R16242 MINGW64 ~/Remote_Repositories/DEL_ORG_Repo/final-s6 (s6hina)
$ git log --oneline
934a124 (HEAD -> s6hina, origin/s6hina) added pull_request_template.md
6b4ea71 edit readme file
de38b26 added hina file

mujjabi2@CPSC-P10R16242 MINGW64 ~/Remote_Repositories/DEL_ORG_Repo/final-s6 (s6hina)
$ git checkout s6christopher 
Switched to branch 's6christopher'
Your branch is up to date with 'origin/s6christopher'.

mujjabi2@CPSC-P10R16242 MINGW64 ~/Remote_Repositories/DEL_ORG_Repo/final-s6 (s6christopher)
$ git cherry-pick 934a124

[s6christopher 7373d3a] added pull_request_template.md
 Author: hina ahmed <hinaahmed@devops.com>
 Date: Tue Aug 15 20:00:39 2023 -0500
 1 file changed, 19 insertions(+)
 create mode 100644 pull_request_template.md

```


## Code Freeze
This is when no more changes are allowed to the codespace, and focus is put on stabilizing the current work. 


## 








