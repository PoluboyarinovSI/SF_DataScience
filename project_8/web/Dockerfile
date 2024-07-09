FROM python:latest
WORKDIR /usr/app
COPY ./app ./
COPY ./requirements.txt ./

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install gcc
RUN apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev g++

RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements3.txt
RUN pip install --no-cache-dir lightfm==1.17

#RUN pip install lightfm --upgrade --ignore-installed scipy
#RUN pip install git+https://github.com/daviddavo/lightfm
#RUN pip install --no-use-pep517 lightfm==1.16

EXPOSE 5000
CMD ["python", "./server.py"]