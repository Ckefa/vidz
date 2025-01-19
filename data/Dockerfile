FROM mariadb:latest

WORKDIR /app 

COPY init.sql /docker-entrypoint-initdb.d/ 

ENV MYSQL_ROOT_PASSWORD=Admin1234
