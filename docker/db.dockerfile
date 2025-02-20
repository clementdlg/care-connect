FROM mysql:9.2.0

ARG INIT_DIR="/docker-entrypoint-initdb.d"
ENV DB_NAME="pa25"

# get sql files
WORKDIR ${INIT_DIR}
COPY sql/*.sql .

# setup entrypoint
# COPY ./docker/db-init.sh .
# RUN chmod 755 db-init.sh
