#!/usr/bin/python3
# -*- coding: utf-8 -*-
from enum import Enum
from app.xml_config import XMLConifgBot

HEROKU_APP_NAME = 'warm-taiga-86371.herokuapp.com'
env = 'dev'
TELEGRAM_TOKEN = '568880226:AAGX19mmh0jgT2BrQqz2johhzJiGPFc0k80'
db_file = "database.vdb"

xml_config_path = "app/bot_states.xml"

class States(Enum):
    S_START = "start"
    S_SELECT_NAME = "select_action"
    S_END_NAME = "end_state"