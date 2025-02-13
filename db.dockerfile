FROM mariadb:11.6-noble

ENV DB_NAME="pa-25"

# get sql files
WORKDIR /sql
COPY sql/*.sql .

# setup entrypoint
COPY ./docker/db-init.sh /docker-entrypoint-initdb.d/
RUN chmod 755 /docker-entrypoint-initdb.d/db-init.sh
