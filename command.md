pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker compose up -d --build
docker compose up --force-recreate -d --build
docker exec -it django /bin/sh

# for task grouping 
from celery import group
from newapp.tasks import tp1,tp2,tp3,tp4
task_group = group(tp1.s(),tp2.s(),tp3.s(),tp4.s())
task_group.apply_async()