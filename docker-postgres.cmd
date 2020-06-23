REM firsst, docker volume create --name=pgdata
REM docker run --rm --name pg-docker --env POSTGRES_PASSWORD=docker -p 5432:5432 --volume C:\Users\alexeyd\volumes\postgres:/var/lib/postgresql/data postgres
docker run --rm --name pg-docker --env POSTGRES_PASSWORD=docker -p 5432:5432 --volume pgdata:/var/lib/postgresql/data postgres