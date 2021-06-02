FROM ubuntu:latest
ENV USER root
# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends python3-pip python3-venv openssh-server git zsh curl gnupg2 \
     && python3 -m pip install --upgrade pip \
     && pip install wheel \
     && pip install ansible \ 
     && pip install paramiko 
     
RUN apt-get install iputils-ping

#COPY .zshrc /root/.zshrc

# Zerotier installation and configuration
# This should only run one time at first build of container, otherwise UID changes
RUN curl -k https://install.zerotier.com/ | bash \
     && /usr/sbin/zerotier-one -d \
     && /usr/sbin/zerotier-cli join b6079f73c69c7aae 

# Git configuration 
RUN git config --global user.name Adam Licht \
     && git config --global user.email amlicht89@gmail.com

