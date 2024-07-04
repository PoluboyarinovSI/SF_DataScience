FROM python:3.10-slim-buster
WORKDIR /usr/app
COPY ./app ./
COPY ./requirements.txt ./
#RUN apt-get update && apt-get -y upgrade
#RUN apt-get -y install gcc
RUN apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev g++
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "./server.py"]