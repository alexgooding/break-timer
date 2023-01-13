# break-timer

## Usage (Production Implementation TODO)
To deploy a development environment, ensure Docker/Docker Compose is installed, and execute the following.
```
docker compose -f docker-compose-db-creation.yml -f docker-compose-dev.yml up
```
This will initialise the SQLite database, and start the web app (accessible at http://0.0.0.0:8000/home). Once the database file has been generated, subsequent start-ups of the app can be executed with the following.
```
docker compose -f docker-compose-dev.yml up
```
Similarly, for a production environment with fixed src and the database as a persistant volume, execute the following for first time setup.
```
docker compose -f docker-compose-db-creation.yml -f docker-compose-prod.yml up
```
Once the database volume has been created, use the following for subsequent start-ups.
```
docker compose -f docker-compose-prod.yml up
```