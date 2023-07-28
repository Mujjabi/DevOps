# Linux Class Notes - DevOps Easy Learning

To identify who you are or identify which server you are connected to. You can use the commands below:
- id : identification
- whoami : who im I?
- uname: This command displays all system information, including the kernel name, network node hostname, kernel release, kernel version, machine hardware name, processor type, and operating system.
- uname -a Here are some of the commands in linux. In linux, we use command lines to navigate different folders or directories. For example:
- pwd: where am i? or present working directory
- ls : list the folders in my current directory
- cd : change directory or move from one directory to another. To use cd, you need to know where you are going 
```
cd s6christopher
#this take you from where ever you are to the s6christopher folder
```
- mkdir: create a folder or directory 

- touch:  This makes or creates files within a directory. (txt, tf, ppt, etc)

- rmdir: removes working directory 

## The kernel
The Linux operating system doesn’t understand commands directly since it doesn't use the same language. This is like when you are working on a project, and you and your workmate speak different languages. 
In this case, you have someone to translate from one language to another language so that the two workmates understand each other.   

In Linux, the kernel is the translator, the middleman between us and the operating system. The kernel translates the commands for the OS so that it understands, and the response from the OS goes through the kernel to translate it back to what we understand. 

The OS only communicates in numbers between zero and one. so this needs to be translated to make sense to us. 

Definition from GPT “The kernel is the first layer of software that runs when the computer is turned on, and it provides a bridge between the hardware and the software running on the system. It acts as an interface between the software and the underlying hardware components, such as the CPU, memory, and input/output devices”

## A Shell
In Linux, a shell is a command-line interface (CLI) program that allows users to interact with the operating system by typing commands. The shell provides a way to control and manipulate the system, manage files and directories, and launch applications.

There are several types of shells available in Linux, including:

- Bash: This is the default shell on most Linux distributions. It is a powerful, feature-rich shell compatible with many older shell scripts.

- Zsh: This is an advanced shell with many features that improve productivity and efficiency, such as tab completion and spelling correction.

- Ksh: This is a shell that is commonly used on Unix systems. It is known for its powerful scripting capabilities.

- Fish: This modern shell is designed to be user-friendly and easy to use. It features syntax highlighting and auto-suggestions, among other things.

## Signs 
$ - If you have this sign when you login to the server, you are just a regular user 

“#” - This means you are a super-user and have all the powers to do certain things 

To change from regular user to super-user, you type “sudo -i”


- sudo -i
  This command switches you from a regular user to a root user (super user)
```
su -s6christopher
#this is switch user from current to s6christopher 
#sudo and su are basically the same
```
- su - root #this switches you to root user. This needs a root password, the super user. 
However, the Company wont give you this password, they just add you to the admin group so that you have previleges. 

## Command and Argument
In Linux, there is a command and argument. For example, when you open folders on your laptop, you can ask to arrange the folders in a certain way based on time, size, alphabetic order etc. 

In Linux, the command is the first part and the argument is the second part that controls the display setting. 

For example “ls” shows the list of all the folders in the  directory,

but ls -l shows the list in a long format. 

You don't need to memorize all these commands and arguments. You can check the manual in Linux using the line of code below:

- man ls
Man stands for manual. It checks the manual for all the arguments for the ls command. 
The arguments can also be combined in one code. See code below


- man ltr
When you check the manual, “l” stands for l; long listing, “t” stands for sort by modification time, newest first, and “r” stands for reserve order. 

To exit the manual version, press “q”.

You do not need to cram things, use the manual 

Another example is when you try to delete files and directories. Using the command below

- rm 
but you can also put an argument to forcefully remove using “rf” argument

- rm -rf

#you can also move files from one directory to another 

- mv 
To check all arguments for the rm command, use manual 

- man rm
  
## Creating A file 
- Touch command
```
touch {1..500}.txt
#This creates 500 txt files. You can also use different formats like csv, png, etc
```
## Reading a file in Linux
To read the content of a certain file, we use the command cat.
```
cat filename
#to exit cat, you ctlr c
```
However, this can only be used if the file is less than one page. if something is more than one page, use the more and the less command. 
```
#one page
cat 
nl

#more than one page
less
more
```
## Editing the file
we use the command vim to edit the content of the file

```
vim filename
```
If you are at the bottom of the page in the terminal, u use the command clear to go back up. This does not wipe out the history, it only takes you back up. 


## clearing content

#if you write something and dont wanna run it, you type control c (^c)

## Copying files or directories 

#We use the comman cp command to copy content from one directory to another
```
cp
cp -r    #this copy one file or folder
```
The argument r means copy recursively. This means that copy the directory and its content into another directory
Eg, folder "eric" has 5 files, u cant copy 'eric' to "chris" without r argument.

This tells linux, copy eric and his content into chris

- cp *  #copy everything in the thatdirectory

- cp *.yaml # This copies everything that ends with yaml

- cp yaml* #copy everything that starts with yaml


### We can also use mv command
#mv comman can change the name of a file/folder  
```
mv s6chris s7chris  #this will rename s6chris to s7chris
```
Also cut files from one location to another

```
mv s6chris/s7chris #this will move all content of s6chris to s6chris
mv -t parent dir1 dir2 dir3 #moves multiple directories into one parent directory
```
The first bar represents the root directory. Top-level directory.
The rest of the bars represent who is inside what. 

```
/eric/s6/file.txt
#The first slush represent the root directory
#Inside the root directory, we have eric. S6 is inside eric, and "file.txt" is a file inside s6

/eric/s6/file/
#if we put a bar at the end, the "file" becomes a directory
```

## Tree visualization of folders

- tree -d
This shows you a tree and the hierachy of how folders are organized

## Absolute path
Changing from one directory to another, you need to put the complete path of where you are going (The absolute path)
```
cd /home/s6eric/SESSION-01-DEVELOPMENT/
#This takes you from wherever you are back to SESSION-01-DEVELOPMENT
```

## Autocomplete button
The “TAB” button, it autocompletes the path to wherever you want to go. 

You can use this to autocomplete the command.

To see the content of the specific folder, you double TAB.
To open the Linux folder, you press ls li TAB,
```
/home/s6christopher/documents/linux/commands
ls li TAB
#this will take you to the linux directory
#To view the content of this folder, you press TAB twice. 
```
## Short path to the directory

if you are already in the folder and want to see the content of another folder that is inside the master folder, you don't need to put the complete path. 
Just type ls folder name. You can use cd to go inside that folder/directory.
```
cd .. 
#this takes you back to the previous directory
/home/s6christopher/documents/linux/
#cd .. would take you back to the document folder
cd ../.. takes you 2 steps backwords
cd -
#this brings you to the directory you were before.
cd - would take me back to /linux directory
```
## Creating Folders and files inside folders
Creating a parent directory and a sub-directory at once, we use the command below
```
mkdir -p /chris/thesis/chapter
#this means, within chris, create a directory "thesis" as a parent and create a child directory called chapter
```

## Creating a folder and a file inside the folder in one line of code

using the semicolon ; or the && between the mkrir and touch command
Forexample, create a directory called "devops" and a file called "learning"
```
mkdir devops; touch learning 
OR
mkdir devops && tough learning 
OR
mkdir devops && cd devops && tough learning
```

## Knowing Linux Distribution

```
cat /etc/os-release
OR 
cat /etc/*release
OR
cat /etc/*release*
```

### Knowing the IP Adress

- For windows
```
 curl ifconfig.me
```

Knowing the size of the file
```
 du -sh [file name]
 du -sh SESSION-01-DEVELOPMENT
 ```

## Number of words, lines and characters
```
wc -l  #number of lines
wc -w #number of words
wc -c  #number of characters
```

## Narrowing the Search (grep command)

If you ls to see the list, and want to narrow down the list to a specific type of files, you can use the pipe grep
```
ls -s  
chris-1, chris-4, tia-1, eric-3, chris-5, chris-6, nashea-3, nashea-1, bob2  
```

If I only want to see the folders/files with chris, i use the pipe grep  
```
ls -l |grep chris  
chris-1 
chris-4 
chris-5 
chris-6
```
I can also be more specific if looking for a particular chris file   
```
ls -l |grep chris |grep chris-4 
chris-4  
```
#### Note: To type the pipe, press shift and the key below the backspace
If the word you are looking for is embedded in another word (Christmas, chris), the grep command will display all possible options of the chris.
If u only want the exact word, you include a “w” before the word
```
ls -l |grep -w chris  #w standards for word
 #only chris will be displayed and not christmas
 
 ls -1 |grep -i chris # this means ignore case sensitive. If lower case or uppercase, ignore it. 
 ```

## Head and Tail command

This helps to show the first or last lines of  a file

It is used together with the cat command
```
cat chris-1 |head -10
```
## Package manager (installing, updating and removing packages)

To install or update packages, we used command apt
1. Updating package
```
apt update
```
This is used for patching or hardening, which adds an extra layer of security
2. Checking if package is already installed
```
which tree
s6christopher@EK-TECH-SERVER04:~$ which tree
/usr/bin/tree
```

3. Installing a package
If the package is not installed or updated, this command installs or updates it. 
```
apt-get install [package name]
apt-get install tree 
```

### Removing the package
```
apt remove tree
#this removes the program/package.
```
Installing and removing programs/packages sometimes require human intervation. 

Forexample, do you really want to install that package [y/n]

To avoid this human intervention, you can add -y at the end
```
apt-get install tree -y 
```

## Hosting a website on a webserver

we use the wget command to download a code from a webserver github

```
wget path/filenme
```
## Webserver
A webserver is somewhere we store anything that opens in a browser. we have 3:

- apache

- tomcat

- HTML

## Environment variable
The env command helps to print the environment variable or system variables for example passwords, usernames etc. it is similar to the if statement.

These are commands saved as shortcuts as environment variables. To be stored to the machine, you need to export it using the export command. For example, if I constantly use a command to check the amount of memory available on the server, and its a long command, I can save it as an environment variable so that next time I don't need to type in the command, I just echo the variable itself

```
root@ip-172-31-82-245:~/Linux# FREE_AWK=$(free -h |grep -i mem|awk -F " " '{print$7}')
root@ip-172-31-82-245:~/Linux# echo $FREE_AWK
596Mi
```
I can export this command so that next time I need to check the available memory, I just echo the env variable. You can also check all your environment variables using the env command. 

If it is not exported, it is only stored in your current shell, not exported. When you shutdown the server, it wont run. 

```
root@ip-172-31-82-245:~/Linux# export FREE_AWK=$(free -h |grep -i mem|awk -F " " '{print$7}')
root@ip-172-31-82-245:~/Linux# echo $FREE_AWK
596Mi
root@ip-172-31-82-245:~/Linux# env
SHELL=/bin/bash
SUDO_GID=1000
SUDO_COMMAND=/bin/bash
SUDO_USER=ubuntu
PWD=/root/Linux
LOGNAME=root
HOME=/root
LANG=C.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
LESSCLOSE=/usr/bin/lesspipe %s %s
TERM=xterm
LESSOPEN=| /usr/bin/lesspipe %s
USER=s6christopher
DISPLAY=localhost:10.0
SHLVL=1
FREE_AWK=596Mi
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
SUDO_UID=1000
MAIL=/var/mail/root
OLDPWD=/root
_=/usr/bin/env
```
## Disk Usage and Memory (Troubleshooting a slow server)

- CPU 
To check the number of CPU connected to the server, you use command nproc 
```
nproc
s6christopher@EK-TECH-SERVER04:~$ nproc
2
```
- ROM : Read Only Memory - You can only read but not write. store things like the clock, calender etcy 

- RAM: Random access memory (Volantile memory that temporary stores data before saving to HHD

- HHD: Hard Disk Drive - permanently stores and retrieve digital data.

- SWAP: Portion of the hard drive that the computer uses when you run out of RAM space. This is when your computer. It serves as an extension of the computer's physical RAM (Random Access Memory) and allows the operating system to temporarily store data that doesn't fit in the available RAM. 

### check the space/memory, use the free command

```
free -h
s6christopher@EK-TECH-SERVER04:~$ free -h
              total        used        free      shared  buff/cache   available
Mem:           7.8G        3.0G        196M        3.5M        4.5G        4.4G
Swap:            0B          0B          0B
 ```

## Append and Redirect

To append is to add content to the initial file, but not change anything to the previous file

For example, I want to add a line of code to the end of the file, and do append. this is done with 2 greater than side >>

```
echo "This is chris" >> test100
echo "Yo made it to the class, good luck" >> test100
This will add these 2 lines at the bottom of the initial document test100

To redirect , this overwrites the content of the file and replaces it with the new content

this is done with a single greater sign >


echo "This is now s6christopher" > test100
This will delete the previous content in test100 and replace it with “this is now s6christopher'. 
```

#### BE VERY CAREFUL, YOU CAN EASILY WIPE OUT IMPORTANT CONTENT. THERE IS NO RECYLCE BIN IN LINUX

The Append and redirect command can also create file and add content to it. If the file doesn't exit, it can be created. If it exits, the append will add content at the bottom of this file. However, if it exit already, the redirect command will overwrite it. 

```
cat "hello" >> text10.txt

cat "hello" > text10.txt
```
## BACKING UP DATA

To backup, you need to compress the files and directories. This involves zipping and unzipping files. For this we use the zip and unzip command. Remember to zip RECURSIVELY otherwise, the zip will only act on the parent folder and not zip anything inside it. You can easily lose data if you don't act/zip recursively.
```
zip christopher.zip maizefile  #zip maizefile and name it christopher.zip
ls 
empty 
```
This only zips the parent folder "maizefile" and not the content inside

```
zip -r christopher.zip maizefile  #zipping recursively. 
ls 
christopher.zip

unzip christopher.zip 
ls
contet content content content 
```
We can also use the “tar” command to compress directories in linux just like zip

```
tar cf  [file_name.tar] [file_name]
tar -cpzf tia-devops.tar tia-devops
```
This means that, compress the file tia_devops into a tar package named tia-devops.tar
To untar, use the following command
```
tar -xvf archive.tar
```

- tar: The command for extracting files from a tar archive.
-x: Specifies that you want to extract files from the archive.
-v: Enables verbose mode, which displays the progress and names of the files being extracted.
-f: Specifies the name of the input file, in this case, "archive.tar". Adjust the file name if needed.

## Comparing Content Of 2 Files in Linux

To compare the content of 2 files to see if there is a difference or not, we use the command “vimdiff”
```
vimdiff chris.txt nashea.txt
```
This will compare the 2 files and highlight the diffences in each line
This can also be done with the diff command

## Creating alias or shortcuts

Sometimes the commands are long, but you can use the “alias” command to create shortcuts for these commands.
```
alias [alias name] = [command]

alias C = "clear"

alias l = "ls -l"
alias u = "uname -a"
```
You should be careful not to overdo alias, you might forget what they mean. Also, when you are working in a team, dont use alias because it might cause miscommunications, your team doesnt know your alias. 

## Exporting alias to bashrc file. 
To export your alias to your local machine, you need to store it to the bashrc file. 

In Linux system, the .bashrc and .bash_profile files are commonly used to store configurations, including aliases, for the Bash shell. Here's an explanation of each file:

- .bashrc: This file is a script that is executed every time a new interactive Bash shell is started. It is typically located in the user's home directory (~/) and can be used to set various environment variables, define aliases, configure the shell prompt, and more. The .bashrc file is specific to each user and allows customization of their shell environment.

In order to apply the changes made to the bashrc or bash_profile files immediately, you need to source the file. 

```
vim ~/.bashrc
#this will open the bashrc file to be able to edit it. 
# Then add the alias you want

alias l ='ls -l'

#save the file then source it to be able to apply the changes immediately
source ~/.bashrc
```

## Downloading and Uploading files from Local Machine to Server
To download and upload content from the server (aws) to local machine, we use the command “scp”

- scp -r #means download directory recursively. All folder and files inside that directory

- scp -r s6christopher@server4.anomicatech.com # connect to server4.anomicatech and log into as s6christopher

```
scp -r s6christopher@server4.anomicatech.com:/tmp/devops . #this (the .) means copy folder devops and paste it where i am currently. 

scp -r s6christopher@server4.anomicatech.com:/tmp/* . #copy everything from tmp directory to where i am. 
```
You can also give absolute path or relative path. to use relative path, u need to be inside the folder where you want the content to be deposited. 
 
## Trouble shooting. 
If there is something wrong with a certain process running on the server, and taking a lot of space or some other reason, we need to kill or terminate that process. There are 2 types of terminating, the harsh kill and the soft kill. The harsh kill terminates the child and parent processes, while the soft kill can kill the child before killing the parent process. The decision to choose the type of kill depends on your investigation regarding the source of the issue. If the source of the issue is caused by only the child process, you only kill the child process.

Eg, troubleshooting a slow server. First you use the “df -h” command to check the amount of free disk space you have. The “h” stands for the human readable

```
root@EK-TECH-SERVER04:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            3.9G     0  3.9G   0% /dev
tmpfs           796M  2.4M  794M   1% /run
/dev/sdb1        62G   14G   49G  23% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/sdb15      105M  5.2M  100M   5% /boot/efi
/dev/sda1        16G   64K   15G   1% /mnt
/dev/loop0       54M   54M     0 100% /snap/snapd/19122
```

Here you can see that we have 62G and we only used 23% and still have 49G. 

If this is not the issue, you use the du - h to check the disk usage and command  free - h command to check RAM, memory.

```
root@EK-TECH-SERVER04:~# du -sh
19M     .
root@EK-TECH-SERVER04:~# free -h
              total        used        free      shared  buff/cache   available
Mem:           7.8G        2.9G        192M        2.9M        4.7G        4.6G
Swap:            0B          0B          0B
```
We see that we have enough memory and this is not the issue.

Therefore, you can use the command “top” or “ps -aux” to see all the processes running in the background. From here, you can see what process is taking all the CPU  (central processing unit). This is like in windows when you click on task manager and it shows you all the processes running in the background and the memory they are using. 

In windows, you can see the process taking space and end it.
In Linux, when you use the top command, it shows you the running processes in real time. 

```
root@EK-TECH-SERVER04:~# top
top - 03:11:40 up 61 days, 15 min, 24 users,  load average: 0.02, 0.01, 0.00
Tasks: 311 total,   1 running, 245 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.2 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  8149164 total,   209464 free,  2998264 used,  4941436 buff/cache
KiB Swap:        0 total,        0 free,        0 used.  4836740 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 1841 root      20   0  108000   7012   6008 S   0.3  0.1   0:00.01 sshd
 7544 jenkins   20   0 4808616 2.219g  24356 S   0.3 28.6  40:11.78 java
    1 root      20   0  226696  10244   6424 S   0.0  0.1   2:58.96 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.87 kthreadd
    3 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 rcu_gp
    4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 rcu_par_gp
    6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:0H-kb
    8 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_wq
```
You can also use |grep command to narrow down the search. 

When you identify the process to kill, you can use the “PID” to kill the specific process. You can use either the kill -9 (harsh kill) or kill -15 (soft kill) 

- ps -aux is the same as top but not real-time. 
- Zombie process: Its a process/task that has been completed  but still running, therefore taking space. 

```
root@EK-TECH-SERVER04:~# ps -aux|grep sleep
root       441  0.0  0.0   7932   748 pts/13   S    02:36   0:00 sleep 1200
root       962  0.0  0.0  14860  1112 pts/8    S+   02:48   0:00 grep --color=auto sleep
root@EK-TECH-SERVER04:~# kill -15 sleep 1200
-bash: kill: sleep: arguments must be process or job IDs
-bash: kill: (1200) - No such process
root@EK-TECH-SERVER04:~# kill -15 441
root@EK-TECH-SERVER04:~# ps -aux|grep sleep
root       980  0.0  0.0  14860  1076 pts/8    S+   02:48   0:00 grep --color=auto sleep
```
Here we checked the processes that are in “sleep” and selected the “sleep 1200” whose PID is 441 and killed using the kill -15. when we check the running processes again, sleep1200 is not there anymore. 

### Server uptime:

To know how long the server has been up since last reboot, we use the uptime command
```
root@s6christopher@EK-TECH-SERVER02://student_home/Docker# uptime -s
2023-05-18 15:49:37
root@s6christopher@EK-TECH-SERVER02://student_home/Docker# uptime -sV
2023-05-18 15:49:37
root@s6christopher@EK-TECH-SERVER02://student_home/Docker# uptime -p
up 4 weeks, 6 days, 16 hours, 56 minutes
root@s6christopher@EK-TECH-SERVER02://student_home/Docker#
```
## Network connectivity (Ping command)
The ping command is a utility used to test network connectivity between your computer and a specific network destination, typically using Internet Control Message Protocol (ICMP). When you execute the ping command followed by a destination IP address or domain name, it sends ICMP echo request packets to the destination and waits for ICMP echo reply packets in response.
Here's what the ping command does:
- Sends ICMP Echo Requests: The ping command sends ICMP echo request packets to the specified destination IP address or domain name.

- Measures Round-Trip Time (RTT): After sending an echo request, ping measures the round-trip time (RTT) it takes for the packet to reach the destination and return back to your computer. It provides statistical information about the minimum, average, maximum, and standard deviation of the RTT.

- Checks Network Connectivity: ping helps determine if there is a successful network connection between your computer and the destination. If the destination responds to the ICMP echo requests, it indicates that network connectivity is established. If no response is received, it suggests a potential network connectivity issue.

- Tests Packet Loss: By counting the number of sent and received ICMP echo request and reply packets, ping can provide information about packet loss. If there is a significant number of lost packets, it indicates a potential issue with the network or destination.

- The ping command is commonly used to diagnose network connectivity problems, check the availability of remote hosts, measure network latency, and troubleshoot network issues. It is a simple and widely available tool for basic network testing.

Please note that some network devices or systems may have ICMP echo requests disabled or configured to prioritize other network traffic, so ping may not always be a definitive indicator of network connectivity.


## Package Manager in Linux
Package manager in Linux is a tool or command that enables us to manage (install, update, uninstall) packages/programs to the operating system. Just like on Windows when you download and install a certain program.  

In Linux, we download programs from a repository. 

To install packages on Linux, first, you need to know the Linux distribution/flavor you are using. Here is the command for that.

```
cat /etc/*release

root@s6christopher@EK-TECH-SERVER02://student_home/Docker# cat /etc/*release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.3 LTS"
NAME="Ubuntu"
VERSION="20.04.3 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.3 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```
This is because the distribution type determines 

## System Configuration Files in Linux
In Linux, the there is a standard directory called the etc directory which is a standard directory for system configuration files in Linux. They play crucial roles in user and group management, password storage, and authentication on the Linux system. The configuration files include the shadow file, passed file and the group file.

- /etc/shadow: This file contains the encrypted password information for user accounts. It is readable only by the root user or users with administrative privileges. 

Only root user has access to modify this file at the company, because it is very sensitive and delicate. If all employees have access, passwords can be easily comprimised. Never open this file with vim (if it allows you to open it, it will be read only). 

This file can only be opened with visudo command. 
```
visudo
```
This sometimes opens in a default format called “nano”, however, you can change it to your preffered setting using this command
```
sudo update-alternatives --config editor


root@ip-172-31-82-245:/home/ubuntu/Linux# sudo update-alternatives --config editor
There are 4 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /bin/nano            40        auto mode
  1            /bin/ed             -100       manual mode
  2            /bin/nano            40        manual mode
  3            /usr/bin/vim.basic   30        manual mode
  4            /usr/bin/vim.tiny    15        manual mode

Press <enter> to keep the current choice[*], or type selection number: 3
#I changed mine to 3 (vim.basic) and worked perfectly

```
- /etc/group: This file stores group account information. It lists the groups on the system and the users who are members of each group.

- /etc/passwd: This file contains essential information about user accounts on the system, such as usernames, user IDs, home directories, and login shells.


## MANAGING ACCESS/PERMISSION TO THE SERVER

There are 2 levels of permission in Linux.

- Regular user

- Root user with password

- Root user without a sudo password.

#### To add user to the server
we us the command useradd
```
useradd s6christopher   #this adds the user called s6christopher
passwd s6christopher #this creates the user's password.
```
After setting a user account and password. As Admin, you shouldn't know the employee password. 

Therefore, after creating a temporary password, you must expire the password to force the user to set a new password, using this command
```
passwd -e s6christopher
```
This expires the temporary password and forces s6christopher to reset password on next login
To check if the password expired, use the change command

```
chage -l s6christopher
```

## Controlling User access to Servers
To control access to the server, we use the command “Usermod” to control access. 
Forexample, if a student doesn't pay, they can be put on nologin list by changing the user shell. 
You can modify the shell and deny login for a specific user. Because they are put on the sbin/nologin (user has “connection close” as an error message). 
```
usermod -s /sbin/nologin s6christopher
```
Connection close can also be other issues happening. The user might be on bin/false. This does the same thing as sbin/login

```
usermod -s /bin/false s6christopher
```
To find out if the user account is locked, u check the shadow file. If the name starts with !!, it means they are locked.
```
cat/etc/shadow |grep s6christopher
```
 I.e if  ! is in front, it means user doesn't have password. we can assign them password using command below.

```
passwd s6christopher #this creates the user's password. 
```
We can solve the issue by adding the user to bin/bash. 

```
/bin/bash - if the user is in bin/bash they can log in without problem. 
usermod -s /bin/bash s6christopher
```

## Modifying user names. 
The usermod command in Linux is used to modify user account attributes. It accepts various arguments (options) to specify the desired modifications. 
Here are some commonly used arguments for the usermod command:

- Changing the user name from one name to the other. 
```
usermod new_name Oldname
```

- Changing a user from one group to a new group
```
usermod -g newgroup username

usermod -aG group1,group2 username  # This adds user to multiple groups listed
```
- Assigning a group to a user using aG argument. 
```
useradd tom  #add a user called tom
groupadd hr  #create group "hr"
passwd tom  #set tom's password
usermod -aG hr tom  #add tom to group hr  #aG means append group, if the user is already 
```
In a group, the user will be moved from one group to another, but if you append, it will add
the user to another group without affecting other user group privileges. 
```
cat /etc/passwd |grep -w tom #look in the user list for the user tom
cat /etc/shadow |grep -w tom #look for tom's password
id tom   #give me tom's info
```
## Deleting user

we use the command userdel to remove a user from the server
```
userdel username
```

## Changing User permission to file/directory access
To change the user mode of a user, group or other from root user to regular user, to grant certain permissions when accessing a file or directory, we use the command chmod. 
The chmod command in Linux is used to change the permissions of files and directories. It stands for "change mode" and is commonly used to modify the read, write, and execute permissions for different user groups (owner, group, and others).

Some of the arguments for this command include

- R: Recursively change permissions for files and directories within a directory.

- v: Verbose mode, which displays detailed output.

- c: Only display output for files that have their permissions changed

```
chmod -R [mode type] file.name
```

- Numeric mode: Uses a three-digit number to represent permissions. Each digit represents the permission for the owner, group, and others, respectively. 
The digits can range from 0 to 7, with each digit corresponding to read (4), write (2), and execute (1) permissions.

- Symbolic mode: Uses symbols to represent permissions. Symbols include:
u for the owner , g for the group, o for others, a for all (owner, group, and others), + to add permissions, - to remove permissions, = to set permissions explicitly

```
rwxr-xr-x    #This is the order for user, group, and other (rwx, rwx, rwx)
```

In this case, user has all rights, group and others only read and execute.
To change the mode or permission, use the command below. 
```
chmod 744 file.txt # Set read, write, and execute forowner, only read for group and others
chmod +x script.sh  #Add execute permissions for all user groups
chmod o-w file.txt #Remove write permissions for others
chmod -R 755 directory/ #Recursively change permissions for all files and directories within a directory\
```

## Change ownership of Files/Directories
The chown command in Linux is used to change the ownership of files and directories. 

It stands for "change owner" and allows you to modify the user and group ownership of a file or directory.

Here are the different ways of using the chown command
```
chown [options] owner[:group] file(s)   #options is the argument (R, v, c)

chown user1 file.txt  #Change the owner of a file to a specific user
chown user1:group1 file.txt  #Change the owner and group of a file
chown :group1 file.txt  #Change the group ownership of a file, keeping the owner unchanged

chown -R user1:group1 directory/ #Change the owner and group recursively for all files and directories within a directory
```

## Creating and Managing User Groups on A Server
In Linux, the groupadd and groupmod commands are used for managing user groups.
Both groupadd and groupmod commands require administrative privileges, so they are typically executed using sudo or by the root user.
It's important to note that modifying group properties can have implications for user accounts and permissions associated with the group

- groupadd: The groupadd command is used to create a new group on the system. It adds a new entry to the /etc/group file, which contains information about the system's groups.
```
groupadd [options] groupname
```
Optional Arguments include -g to specify a specific GID (Group ID) for the group 
and -r to create a system group.

Regular user groups are usually assigned GIDs starting from a certain value (e.g., 1000), while system groups often have predefined GIDs assigned by the operating system.

Examples of system groups in Linux include "root" (GID 0), "adm" (GID 4), "staff" (GID 50), and "sudo" (GID varies across distributions). These groups serve various system-related functions, such as administrative tasks, log management, or system monitoring.

- The groupmod command is used to modify existing group properties. It allows you to change attributes such as the group name or GID.
```
groupmod [options] groupname
```
Optional flags that modify the behavior of the groupmod command. Some commonly used options include -n to specify a new group name and -g to specify a new GID for the group
```
groupmod -n newname mygroup   #mygroup is the current group name to be changed.
```

## Changing user privilege in the sudoers file 
If you want a user to have the same privilege as the root, you can open the shadow file using the visudo and give them the same powers and the root to execute any command.  Here, I added users s6christopher and Jenkins to have the same power as the Root. 
```
visudo

# User privilege specification
root    ALL=(ALL:ALL) ALL
s6christopher    ALL=(ALL:ALL) ALL
Jenkins    ALL=(ALL:ALL) ALL


# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
```

If its a group, it should have a % before the group name. For example group sudo as shown above. 

This means all members in the sudo group can execute any command and members in the admin group can gain root privilege

## The awk, cut commands and creating environment variables
The awk command is used to display information in columns using the field separator. 

It is designed to extract and manipulate data from files or input streams based on specific patterns and rules. awk processes data line by line, splitting each line into fields and performing actions on those fields.

Print specific fields from a file:
```
cat /etc/passwd |grep -w chris |awk -F "insert the field separator" '{print$1}'
cat /etc/passwd |grep -w chris |awk -F " " '{print$1}'
chris
```
This  means that check for users list, and grep for chris, and print the first column. 
The response is "chris"
You can create a script and save it as an environment variable, when you call the variable, it will print the same response
```
AWK_Command = cat /etc/passwd |grep -w chris |awk -F " " '{print$1}'
```
To call for this environment variable, you use the “echo” command. 
```
echo $AWK_Command  #The echo comman prints the environment varible
Chris
```
We can also use a condition (program) that displays the response
```
echo "The username of the user is: $AWK_Command"
The Username of the user is : Chris
```

The Cut command does the same thing as the awk command. But some times one is more applicable than the other.  
Its the same function but the syntax changes a little bit. Instead of the field separator “F”, we use a “d” for delimiter. 

```
cat /etc/passwd |grep -w chris |cut -d "insert the field separator" -f1
cat /etc/passwd |grep -w chris |cut -d " " -f1
chris
```
## Difference between cut and awk
Sometimes, you want to narrow down to a range of columns and not just one specific column. 
In this case, we we cut command is preferred since its hard to print a range of columns using awk.
Forexample, if the kernel version is 5.19.0 and you only want 5.19, u can grep it using the cut instead of the awk

Also, if the field separator is a space and it is not consistent, the cut wont work because the counts each space as a character.
```
root@ip-172-31-82-245:~/Linux# uname -a
Linux ip-172-31-82-245 5.19.0-1028-aws #29~22.04.1-Ubuntu SMP Tue Jun 20 19:12:11 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
uname -a | awk -F " " '{print$3}' |cut -d "." -f1,2
```

Forexample, to grep only the available memory 

```
root@ip-172-31-82-245:~/Linux# free -h
               total        used        free      shared  buff/cache   available
Mem:           957Mi       223Mi       169Mi       0.0Ki       563Mi       588Mi


root@ip-172-31-82-245:~/Linux# free -h |grep -i mem|awk -F " " '{print$7}'  #with awk
588Mi
root@ip-172-31-82-245:~/Linux# free -h |grep -i mem|cut -d " " -f7  #with cut
```
This shows that the cut didnt work since the space is inconsistent. However, awk worked fine. 

## Scripting (Programming)
A script is used to make a program (automation) based on the conditions or commands you want to print.
The script should have the .sh extension. 
```
Vim script.sh
word1="banana"
word2="apple"

if ["word1" ="word2"]; then
    echo "The words are equal."
else
    echo "The words are not equal."   
fi    #this closes the statement, this is like end command.
    
bash script.sh  #The bash command is used to run the program
```

If you run this script, The answer will be "The words are not equal" 
```
USER= cat /etc/passwd |grep -w chris |awk -F " " '{print$1}'
if [$USER ="Chris"]; then
    echo "The user exists and his name is $USER."
else
    echo "The user doesnt exist."   
fi
bash script.sh
```
If the user chris exists, the response will be "the user exists and his name is Chris"
#### Adding more commands
```
USER= cat /etc/passwd |grep -w chris |awk -F " " '{print$1}'
if [$USER ="Chris"]; then
    echo "The user exists and his name is $USER."
else
    echo "The user doesnt exist."
    useradd Chris 
    passwd  Chris
    usermod aG hr Chris
    cat /etc/passwd |grep -w Chris
    cat /etc/shadow |grep -w Chris
    id Chris
fi
bash script.sh 
```

If the user chris exists, the response will be "the user exists and his name is Chris"

#### More than 3 conditions
You can also check for 3 conditions using the “elif” command which means “else if”. 
For example, if you want to check the memory available on the file system, and want to make action depending on how much memory is available, u can use 3 conditions. 
```
Check available memory
see if it is equal to 80%
see if

DF_AWK=$(df -h |grep -i root|awk -F " " '{print$5}')
echo $DF_AWK

if [ "$DF_AWK" = "80%" ]; then
    echo "The filesystem check passed."
elif [ "$DF_AWK" \< "80%" ]; then
    echo "The filesystem check passed, and this is perfect."
else
    echo "The filesystem check failed."
fi
```
The conditions can also be expressed in a non-symbolic form (=,<,> etc). To see the different ways to do this, you can check the manual for test using the man test command

```
man test
     
STRING1 = STRING2
              the strings are equal

STRING1 != STRING2
              the strings are not equal

INTEGER1 -eq INTEGER2
              INTEGER1 is equal to INTEGER2

INTEGER1 -ge INTEGER2
              INTEGER1 is greater than or equal to INTEGER2

INTEGER1 -gt INTEGER2
              INTEGER1 is greater than INTEGER2

INTEGER1 -le INTEGER2
              INTEGER1 is less than or equal to INTEGER2

INTEGER1 -lt INTEGER2
              INTEGER1 is less than INTEGER2

INTEGER1 -ne INTEGER2
              INTEGER1 is not equal to INTEGER2
 ```


## Cron Job / Crontab 
A cron job is a time-based task scheduler in Unix-like operating systems. It allows you to automate the execution of scripts or commands at specific intervals or times. 

The term "cron" refers to the Cron daemon, a background process that runs continuously and initiates scheduled tasks based on predefined schedules.

The syntax for a cron job is as follows:
```
* * * * * command

crontab -e  #this open the crontab file in a text editor
0 0 * * * shutdown -h now  #schedule shutdown at 12am
```

#### Shutdown, poweroff, reboot
These commands are used to restart, stop or reboot the server. You can use the Cron job to schedule the 

- shutdown -r   Restart the system

- shutdown -h 

- shutdown -h now 

- shutdown -h +5 

- shutdown -a   : Abort shutdown 

## Sed command 
The sed command, short for "stream editor," is a powerful text processing tool available in Unix-like operating systems, including Linux. It is used for performing basic text transformations on an input stream (a file or data from a pipeline) and printing the modified output. sed is often used in shell scripts, one-liners, and text processing tasks

OPTIONS: These are optional flags that modify the behavior of sed. Some commonly used options are:

- n: Suppresses automatic printing of the input.

- i: Edits the input file in place (i.e., modifies the file directly).

- e: Allows multiple expressions to be specified in the same sed command.
```
sed 's/hello/world/g' example.txt
```
This means replace the word hello with world in the example.txt file

