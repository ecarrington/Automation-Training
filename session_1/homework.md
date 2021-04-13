## Objectives:
  - If on Windows 10, install Windows Subsystem for Linux (documentation in Automation Hub)
  - Install Python3 and set up a virtual environment called 'ansible'
  - Install Ansible in Python Virtual Environment
  - Install Git
  - Install vscode


### Install Windows Subsystem For Linux
All steps below are performed in the Ubuntu Environment

##### Update your Linux Environment
```cli
sudo apt-get update
sudo apt-get upgrade -y
```

### Install Git
```cli
sudo apt install git-all
```

### Install Python3

##### First, see what version you are running
```cli
$ python3 --version
```

##### Next, install Python3.6
```cli
sudo apt-get install python3.6
```

### Install Ansible

##### Create Ansible directory for Virtual Environment
```cli
mkdir ansible
cd ansible
```

###### Install and upgrade pip
```cli
sudo apt install python3-pip -y
python3 -m pip install --user --upgrade pip
```

##### Install Python Virtual Environment
```cli
sudo apt-get install python3-venv -y
```

##### Build Virtual Environment
```cli
python3 -m venv ansible
```

##### Activate Virtual Environment
```cli
source ./bin/activate
```

###### Install additional Python tools
```cli
$(ansible) pip install wheel
$(ansible) sudo apt-get install python 3.6-dev -y
```

##### Install Ansible
```cli
$(ansible) pip install ansible==2.9
```
##### Check Ansible Version (should be 2.9)
```cli
ansible --version
```

##### Install Paramiko
```cli
pip install paramiko
```

### Download VSCODE For Windows or Mac from https://code.visualstudio.com/download
