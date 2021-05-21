FROM ubuntu:latest
ENV USER root
# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends python3-pip python3-venv openssh-server git zsh \
     && python3 -m pip install --upgrade pip \
     && pip install wheel \
     && pip install ansible \ 
     && pip install paramiko 

COPY .zshrc /root/.zshrc


