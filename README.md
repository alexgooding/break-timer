# break-timer

## Usage (Production Implementation TODO)
To deploy a development or production environment, ensure Docker/Docker Compose is installed, and execute the following.
```
docker compose -f docker-compose-<dev|prod>.yml --profile migrate_db up
```
This will initialise the SQLite database, and start the web app (accessible at http://0.0.0.0:8000/home). Once the database file has been generated, subsequent start-ups of the app can be executed without the database migration profile argument.
