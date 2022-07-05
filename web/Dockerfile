FROM ubuntu:20.04

#set the working directory
WORKDIR /app

#copy all the content where this file resids
COPY . /app/

RUN apt update &&\
    apt list --upgradable &&\
    apt -y install build-essential &&\
    apt-get -y install manpages-dev &&\
    apt install python3 -y &&\
    apt -y install python3-pip &&\
    pip3 install local_packages/*.whl &&\
    pip3 install -r requirements.txt

EXPOSE 3000

CMD [ "uwsgi", "app.ini" ]