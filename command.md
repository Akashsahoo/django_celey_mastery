pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker compose up -d --build
docker compose up --force-recreate -d --build
docker exec -it django /bin/sh


# Remove all docker
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)

# Run on Django to inspect task
celery inspect active
celery inspect active_queues

# celery rabbitmq priortiywise tasks manage.py shell
from dcelery.celery import t1,t2,t3
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)

# for task grouping 
from celery import group
from newapp.tasks import tp1,tp2,tp3,tp4
task_group = group(tp1.s(),tp2.s(),tp3.s(),tp4.s())
task_group.apply_async()

# for task chaining
from celery import chain
from newapp.tasks import tp1,tp2,tp3,tp4
task_chain = chain(tp1.s(),tp2.s(),tp3.s(),tp4.s())
task_chain.apply_async()