#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import heartbeat

# Flask
DEBUG = False
SECRET_KEY = os.urandom(32)
APPLICATION_ROOT = '/api/downstream/v1'

# SQLAlchemy (DB)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{{ dsnodemysqluser }}:{{ mysqlpassword }}@{{ mysqldbserver }}/downstream'  # NOQA

FILES_PATH = '/tmp/'
TAGS_PATH = '/tmp/'
MMDB_PATH = '{{ dsnodegeodbpath }}'

HEARTBEAT = heartbeat.Swizzle.Swizzle

TEST_FILE_SIZE = 100
MAX_TOKENS_PER_IP = 5
MIN_SJCX_BALANCE = 10000
MAX_SIG_MESSAGE_SIZE = 1024
REQUIRE_SIGNATURE = False

