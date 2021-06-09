FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PIP_INSTALL_REQUIRES_VIRTUALENV 0
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
