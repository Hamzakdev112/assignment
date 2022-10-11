FROM python:3.7-slim
# OS stuff
RUN apt-get update 
RUN apt-get install dialog apt-utils -y -q
RUN apt-get install -y -q less vim cron wget 
RUN apt-get install -y python3-pip
# Python stuff
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /usr/local/bin/python -m pip install ipdb

# Root user environment stuff
COPY .docker/assets/bashrc /root/.bashrc
COPY .docker/assets/bash_aliases /root/.bash_aliases

# Static files served from here
RUN mkdir -p /www/static_live

# Application stuff
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000
#CMD ["./.docker/assets/start_server.sh"]