# Business Care API
## Stucture of the project

```
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

## How to deploy
- this project is packaged using Docker Compose. To deploy the API, run :
```
docker compose up -d
```
- When you ran this command, several services will start :

### SQL
- The Mariadb Database will run. An init script is executing all the `.sql` files from the `sql` directory of this repo via a [bindmount](https://docs.docker.com/engine/storage/bind-mounts/)
- All the sql files will be sourced **IN ORDER** (keep that in mind)


### Uvicorn (Python Web Server)
- The python FastAPI will run on **port 8000** using uvicorn

## Ensure that deployement went well
- to check that every service is started, run
```
docker compose ps
```
- Ensure that under the "STATE" column, the services are noted as "Up"

## Troubleshoot
- to come
