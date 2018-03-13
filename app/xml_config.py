#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

class XMLConifgBot:
    def __init__(self, path_to_xml):
        self.pathToXml = path_to_xml
        with open(self.pathToXml) as f:
            content = f.read()
        self.content = BeautifulSoup(content, "lxml")

    def getSettingsByStateName(self, state_name):
        return self.content.find('state', {'name': state_name})

    def getTransitionByText(self, state_name, text):
        stateSetting = self.getSettingsByStateName(state_name)
        for transition in stateSetting.find_all('transition'):
            if re.match(transition['input'], text):
                return transition