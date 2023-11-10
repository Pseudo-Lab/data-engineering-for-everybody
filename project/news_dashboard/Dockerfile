FROM python:3.10

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean;

ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

ENV PATH $JAVA_HOME/bin:$PATH

COPY requirements.txt requirements.txt
RUN pip install -U pip &&  \
    pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]