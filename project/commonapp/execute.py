from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from commonapp.jobs import send_weekly_mail


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_weekly_mail, 'cron', day_of_week="fri", hour="16", minute="00")
    scheduler.start()
