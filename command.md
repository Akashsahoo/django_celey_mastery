pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker compose up -d --build
docker compose up --force-recreate -d --build
docker exec -it django /bin/sh

