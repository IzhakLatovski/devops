FROM jenkins/jenkins  
USER root  
# Install Docker
RUN curl -sSL https://get.docker.com/ | sh
# Install Docker-compose
RUN curl -L \  
  "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" \  
  -o /usr/local/bin/docker-compose \  
  && chmod +x /usr/local/bin/docker-compose  
USER jenkins  