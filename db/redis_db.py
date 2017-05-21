# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/17

from redis import ConnectionPool
from redis import Redis

from config import REDIS_CONF

def init_redis():
    pool = ConnectionPool(**REDIS_CONF)
    rds = Redis(connection_pool=pool)
    return rds

rds = init_redis()