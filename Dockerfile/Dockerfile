# Simple Search Engine - Caio J. Carvalho

# Base image and maintainer infos
FROM ubuntu
MAINTAINER Caio Jordão Carvalho <caiojcarvalho@gmail.com>

# Update packages and install some items
RUN apt-get update && \
apt-get install -y openjdk-8-jdk python2.7 wget tar lsof git python-pip

# Downloading and installing Solr
RUN wget http://ftp.unicamp.br/pub/apache/lucene/solr/6.0.1/solr-6.0.1.tgz
RUN tar zxvf solr-6.0.1.tgz

# Cloning the project
RUN git clone https://github.com/cjlcarvalho/SimpleSearchEngine

# Installing the required libraries
RUN pip install -r SimpleSearchEngine/requirements.txt

# Running the terminal
CMD ["/bin/bash"]

EXPOSE 80
