from news.jobs import add_job
from news.adding_news import add_news, add_international_news
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def news_start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(add_news, 'interval', hours=6)
    scheduler.start()


def job_start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(add_job, 'interval', hours=6)
    scheduler.start()


def internationalnews_start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(add_international_news, 'interval', hours=6)
    scheduler.start()
