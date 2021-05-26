# Automation-Training
Work Training - Ansible and Python Network Automation

### Structure
Each session will have a repository with its own applicable playbooks, scripts, examples, roles, and other automation dependencies. Each folder acts on the inventory file and ansible.cfg file located in the root of this directory. Each folder will also have its own README pages with useful links and resources, as well as course notes for reference. 

### Remote Development using VsCode and Docker
Vscode allows us to develop straight into docker containers using the remote-containers plugin. This creates a 'bridge' between itself and a container. This is handy because we can now leverage the power of docker and ZeroTier VPN service to connect remotely to our EVE-NG nodes running in Google Cloud platform, making them appear as if they are local to us. Not only this, but running a pre-built Docker environment ensures a consistent experience for every user as dependencies are predefined in the Dockerfile. 

### Configuring Remote-Containers for VsCode
There is a good writeup for this configuration that can be found [here](https://code.visualstudio.com/docs/remote/containers). It covers both Windows and Linux intallations, but for brevity I've including the initial configuration steps below. Containers consist of two primary files; devcontainer.json, which defines configuration parameters relating to how VsCode will run your container, and the Dockerfile itself, which contains the set of instructions used for building the container. 

#### Linux
Recommended OS at time of writing: Ubuntu 20.04.2 LTS

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
- Use control + P to open the VsCode shell and select 'remote-containers: add development container'. Select ubuntu bionic. This will give you the basic .devcontainer folder structure we can use as a boilerplate for building our own Dockerfile and devcontainer.json file
- Then, build your devcontainer.json file. This file defines how the container will run in VsCode's remote development environment
- Next, build your Dockerfile, which is the set of instructions the container will use to install dependencies when it boots.
- Reference [here](https://code.visualstudio.com/docs/remote/create-dev-container#_create-a-devcontainerjson-file)

**Run your new Docker container in VsCode**
- Control + P will open your VsCode shell. Select 'remote-containers: rebuild and reopen in container'. This does exactly what it says it will do - it rebuilds your current environment inside of the container that is sitting in your .devcontainers folder. It should also be noted this rebuilds your entire workspace in a container, so its a good idea to have a dedicated workspace for a project you are trying to containerize. 
- At this point, you should be able to open a terminal and access your container. You're now free to develop in VsCode and run that code inside your container.
- To exit out of your container (it will still be running, however), Control + P and execute the command 'reopen locally', which will reopen your VsCode environment locally.
- To re-enter your container that is already running, Control + P and execute the command 'reopen in container'. There is no need to rebuild if the container is already running.

#### Windows
This method leverages Docker Desktop, which is designed to run as a native Windows application. It is important to note we must enable either Hyper-V AND WSL2 backend in order for Docker to function properly. The reason for WSL2 is so we may run Linux containers. If using WSL2, please note Windows 10 version 1903 or later is required. You can check this by running ```console winver ``` in your command terminal. 
- Enable Hyper-V in Windows Features
- Initial installation guide for WSL can be found [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Do not skip this step!
- Install the WSL2 kernel from [here](https://docs.microsoft.com/en-us/windows/wsl/wsl2-kernel)
- Run the installer. Once complete, open Powershell and run ```console wsl --list```, which will list all the distros and version of WSL in the version column. 
- If you need to upgrade from WSL1 to WSL2, run the following in Powershell: ```console wsl --set-version <distro-name> 2```. I'd recommend Ubuntu 20.04. 
- It will take some time to migrate your distros. Once the upgrade is complte, you can run ```console wsl -l -v``` and ensure your versions now read '2'. 
- Reference for upgrading WSL1 to WSL2 can be found [here](https://dev.to/adityakanekar/upgrading-from-wsl1-to-wsl2-1fl9)
- Finally, install Docker Desktop from [here](https://docker.com/products/docker-desktop)

Once WSL2 is installed, configured, and verified running properly, ensure WSL 2 back-end is enabled. Right click on the Docker task bar and select 'settings'. Check 'use the wsl 2 based engine', and verify your correct distribution is enabled under 'resources > WSL integrations'.

You should now be able to install and configure the remote-containers extension for VsCode as detailed above in the Linux configuration. 

**If your container will not start (Windows)**
- Try to launch manually via Docker Desktop
- If Docker Desktop does not load and you get an error stating your account is not in the 'docker-users' group, navigate to computer management > local users and groups > find the 'docker-users' group, and add your account to it. 

