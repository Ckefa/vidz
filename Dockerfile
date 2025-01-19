FROM python:3.13

WORKDIR /app 

RUN apt-get update && apt-get upgrade -y 

COPY ./requirements.txt /app

RUN pip3 install --no-cache-dir --upgrade pip


RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:5000 wsgi:app > /var/log/vidz.log 2>&1"]
