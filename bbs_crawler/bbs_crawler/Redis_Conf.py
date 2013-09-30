#-*- coding:utf-8 -*-

import sys,os
import redis
import re

def get_redis_db():
	'''Get redis db for data'''
	return redis.Redis(host='localhost', port=6379)
