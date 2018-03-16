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

    def getContent(self):
        return self.content