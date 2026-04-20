from apscheduler.schedulers.base import BaseScheduler


def register_jobs(scheduler: BaseScheduler) -> None:
    scheduler.add_job(lambda: None, trigger='interval', minutes=30, id='noop_reminder', replace_existing=True)
