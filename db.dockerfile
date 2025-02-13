FROM mariadb:11.6-noble

COPY sql/*.sql /docker-entrypoint-initdb.d/
