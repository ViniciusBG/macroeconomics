# set base image (host OS)
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /app/src

# copying only requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8501

CMD streamlit run hello.py --server.port 8501
