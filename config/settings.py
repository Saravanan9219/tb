import aredis
from redis import Redis
from rq_scheduler import Scheduler


REDIS = aredis.StrictRedis(
    host='localhost',
    port=6379,
    db=0
)


SCHEDULER = Scheduler(connection=Redis())
