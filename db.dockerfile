FROM mariadb:11.6-noble

ARG INIT_DIR="/docker-entrypoint-initdb.d"
ENV DB_NAME="pa25"

# get sql files
# WORKDIR /sql
# COPY sql/*.sql .

# setup entrypoint
WORKDIR ${INIT_DIR}
COPY ./docker/db-init.sh .
RUN chmod 755 db-init.sh
