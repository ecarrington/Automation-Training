# Automation-Training
Work Training - Ansible and Python Network Automation

### Structure
Each session will have a repository with its own applicable playbooks, scripts, examples, roles, and other automation dependencies. Each folder acts on the inventory file and ansible.cfg file located in the root of this directory. Each folder will also have its own README pages with useful links and resources, as well as course notes for reference. 

### Remote Development using VsCode and Docker
Vscode allows us to develop straight into docker containers using the remote-containers plugin. This is handy because we can now leverage the power of docker and ZeroTier VPN service to connect remotely to our EVE-NG nodes running in Google Cloud platform, making them appear as if they are local to us. Not only this, but running a pre-built Docker environment ensures a consistent experience for every user as dependencies are predefined in the Dockerfile. 

### Configuring Remote-Containers for VsCode
There is a good writeup for this configuration that can be found [here](https://code.visualstudio.com/docs/remote/containers)

##### Linux
Recommended OS at time of writing: Ubuntu 20.0.1

**Install Docker**
```console
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg \
sb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**Install Docker Engine**
```console
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

**Install Docker Compose and assign your user to the Docker group. Reboot for user settings to take effect**
```console
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker $USER
```

**Install remote development extension pack in VsCode, which includes the remote-containers plugin**
- Use control + P to open the VsCode shell and select 'remote-containers: add development container'. Select ubuntu bionic. This will give you the basice .devcontainer folder structure we can use as a boilerplate for building our own Dockerfile and devcontainer.json file
- Then, build your devcontainer.json file. This file defines how the container will run in VsCode's remote development environment
- Next, build your Dockerfile, which is the set of instructions the container will use to install dependencies when it boots.
- Reference [here](https://code.visualstudio.com/docs/remote/create-dev-container#_create-a-devcontainerjson-file)

**Run your new Docker container in VsCode**
- Control + P will open your VsCode shell. Select 'remote-containers: rebuild and reopen in container'. This does exactly what it says it will do - it rebuilds your current environment inside of the container that is sitting in your .devcontainers folder. 

##### Windows

