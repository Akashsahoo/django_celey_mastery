from datetime import timedelta

from dcelery.celery_config import app

# app.conf.beat_schedule = {
#     'task1':{
#         'task': 'dcelery.celery_tasks.ex12_task_schedule_customization.task1',
#         'schedule': timedelta(seconds=5),
#         'kwargs': {'foo': 'bar'},
#         'args': (1, 2),
#         'options': {
#             'queue':'tasks',
#             'priory':5,
#         }
#     },
#     'task2':{
#         'task': 'dcelery.celery_tasks.ex12_task_schedule_customization.task2',
#         'schedule': timedelta(seconds=10),
#     }
# }

@app.task(queue="tasks")
def task1(a, b, **kwargs):
    result = a + b
    print(f"Running task 1 - {result}")

@app.task(queue="tasks")
def task2():
    print("Running task 2")