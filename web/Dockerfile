FROM python:3.11-slim-buster


WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/


COPY entrypoint.sh /code/

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
