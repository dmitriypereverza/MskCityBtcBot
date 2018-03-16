#!/usr/bin/python3
# -*- coding: utf-8 -*-

import inject

from app import config
from app.StateConfig import StateConfig
from app.XmlConfigParser import XMLConifgBot

def diConfig(binder):
    binder.bind(
        'statesConfig',
        StateConfig(XMLConifgBot(config.xml_config_path).getContent())
    )
inject.configure_once(diConfig)