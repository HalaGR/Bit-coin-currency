FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /bitcoin-app
WORKDIR /bitcoin-app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["bitcoin-app.py"]