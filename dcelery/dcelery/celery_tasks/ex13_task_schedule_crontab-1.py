from datetime import timedelta

from celery.schedules import crontab

from dcelery.celery_config import app

# app.conf.beat_schedule = {
#     'task1':{
#         'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task1',
#         'schedule': crontab(minute='0-59/10', hour='0-5', day_of_week='mon'),
#         'kwargs': {'foo': 'bar'},
#         'args': (1, 2),
#         'options': {
#             'queue':'tasks',
#             'priory':5,
#         }
#     },
#     'task2':{
#         'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task2',
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

"""
* * * * *
| | | | |
| | | | +----- Day of the Week (0 - 6) (Sunday=0 or 7)
| | | +------- Month (1 - 12)
| | +--------- Day of the Month (1 - 31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
"""

"""
* * * * *       # Run every minute
*/5 * * * *     # Run every 5 minutes
30 * * * *      # Run every hour at 30 minutes past the hour
0 9 * * *       # Run every day at 9 AM
0 14 * * 1      # Run every Monday at 2 PM
0 0 1,15 * *    # Run on the 1st and 15th of each month
0 20,23 * * 5   # Run every Friday at 8 PM and 11 PM
*/15 * * * * *  # Run every 15 seconds (non-standard)
0 0 * * *       # Run every day at midnight
0 12 * * MON    # Run every Monday at 12 PM
0 0 1-7 * *     # Run on the first 7 days of each month
0 0/2 * * *     # Run every 2 hours
0 */6 * * *     # Run every 6 hours
0 0-8/2 * * *   # Run every 2 hours from midnight to 8 AM
0 0,12 * * *    # Run at midnight and noon every day
0 0 * * 0       # Run every Sunday at midnight
0 0 1 1 *       # Run on January 1st every year
0 0 1 1 MON     # Run on the first Monday of January every year
"""