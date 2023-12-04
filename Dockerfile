FROM python:3.8.10

WORKDIR /chat
COPY src/ /chat
COPY requirements.txt /chat/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "/chat/main.py"]