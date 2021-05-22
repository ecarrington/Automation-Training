FROM ubuntu:latest
ENV USER root
# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends python3-pip python3-venv openssh-server git zsh curl gnupg2 \
     && python3 -m pip install --upgrade pip \
     && pip install wheel \
     && pip install ansible \ 
     && pip install paramiko 

#COPY .zshrc /root/.zshrc

# Zerotier installation and configuration
CMD curl https://install.zerotier.com/ | bash 
CMD /usr/sbin/zerotier-one -d 
CMD /usr/sbin/zerotier-cli join b6079f73c69c7aee 

# Git configuration 
CMD git config --global user.name Adam Licht 
CMD git config --global user.email amlicht89@gmail.com

