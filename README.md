# Business Care API
## Stucture of the project

```bash
├── compose.yml
├── docker
│   ├── # docker related files
├── sources
│   ├── app.py
│   └── # python source files
└── sql
    ├── 01-create.sql
    ├── 02-insert-user.sql
    ├── 03-insert-X.sql
    └── # all sql scripts
```

## How to deploy (for dev)
- this project is packaged using Docker Compose. To deploy the API, run :
```bash
docker compose up -d
```
- When you ran this command, several services will start :

### SQL
- The Mariadb Database will run. An init script is executing all the `.sql` files from the `sql` directory of this repo via a [bindmount](https://docs.docker.com/engine/storage/bind-mounts/). This is to ensure that the teams is always using the lastest SQL scheme thoughout the developpement of the project.
- All the sql files will be sourced **IN ORDER** (keep that in mind)
- Note that the database is **NON PERSITANT**. This is because you should only rely on the `.sql` files because this is not in production.


### Uvicorn (Python Web Server)
- The python FastAPI will run on **port 8000** using uvicorn
- A [bindmount](https://docs.docker.com/engine/storage/bind-mounts/) is also setup between `sources` (host) and `/app` (container). This is to allow for easier developpement, the IDE and the server can access the same files

## Ensure that deployement went well
- to check that every service is started, run
```bash
docker compose ps
```
- Ensure that under the "STATE" column, the services are noted as "Up"

# Troubleshoot
## Ping
- Get the IP of the containers. Use these command :
```bash
docker network ls # to list all the networks 
docker network inspect <network-name> 
docker network inspect <network-name> | grep -B3 "IPv4" # parse the output
```
- Test network-layer connectivity
```
ping <ip>
```
- If their is no connectivity, verify that the containers are on the appropriate network. Also verify that the network on which they run is correctly setup

## Test Application connectivity
- If you can ping the containers, now try to get a reponse from the services that are running

### Python Web Server
- To troubleshoot the web server, try to run this command from you host machine
```
curl <python-ip>:8000
```
- If you have no reponse, then you should check the port forwarding

### Database
- To troubleshoot the database, try to run this command from you host machine
```
telnet <mariadb-ip> 3306
```
- If you get a `Connection refused`, then you should check the port forwarding

# TODO 
## sql
- table pour les contrats
- société client -> représentant
- status des devis
- devis
- table de type de certifications
- table des communautés pour le forum
- associations
