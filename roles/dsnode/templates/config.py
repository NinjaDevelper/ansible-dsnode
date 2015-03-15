#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import heartbeat

# Flask
DEBUG = False
SECRET_KEY = os.urandom(32)
APPLICATION_ROOT = '/api/downstream/v1'
SERVER_ALIAS = '{{ dsnodehostname }}'

# SQLAlchemy (DB)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{{ dsnodemysqluser }}:{{ mysqlpassword }}@{{ mysqldbserver }}/{{dsnodemysqldbname}}?charset=utf8'  # NOQA

TAG_KEY = '{{dsnodetagskey}}'

FILES_PATH = '{{ dsnodetmppath }}'
TAGS_PATH = '{{ dsnodetagspath }}'
REMOTE_TAGS_PATH = '{{ dsnoderemotetagspath }}'
MMDB_PATH = '{{ dsnodegeodbpath }}'

HEARTBEAT = heartbeat.Merkle.Merkle
{% if (inventory_hostname == groups['dbserver'][0]) %}
HEARTBEAT_PATH = '{{ dsnodeheartbeatpath }}'
{% else %}
HEARTBEAT_PATH = '{{ dsnoderemoteheartbeatpath }}'
{% endif %}

MONGO_LOGGING = True
MONGO_URI = 'mongodb://{{dsnodemongodbuser}}:{{mongodbpassword}}@{{mongodbserver}}/{{dsnodemongodbname}}'
PROFILE = True

DEFAULT_CHUNK_SIZE = 33554432
MAX_TOKENS_PER_IP = 5
MIN_SJCX_BALANCE = 10000
MAX_SIG_MESSAGE_SIZE = 1024
REQUIRE_SIGNATURE = False
DEFAULT_INTERVAL = 300
MAX_CHUNKS_PER_REQUEST = 10
MAX_SIZE_PER_ADDRESS = 1073741824

# changing this requires deleting the data/heartbeat file
# and rebuilding the chunk database
HEARTBEAT_CHECK_FRACTION = 0.001

