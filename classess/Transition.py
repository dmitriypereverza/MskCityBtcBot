#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import inject

from CustomExeptions import Exeptions

class Transition:
    __slots__ = ['input', 'next_state', 'text', 'exec', 'keyboard_btn']

    def setInput(self, input):
        self.input = input
        return self

    def getInput(self):
        return self.input

    def setNextState(self, state):
        self.next_state = state
        return self

    def getNextState(self):
        return self.next_state

    def setText(self, text):
        self.text = text
        return self

    def getText(self):
        return self.text

    def setExecFunction(self, text):
        if len(text) == 0:
            self.exec = '' # Fix it
            return self
        if not re.match(r'.+::.+', text):
            raise Exeptions.ConfigSyntaxExceptions('Define exect param "{}" without "::"'.format(text))
        self.exec = text
        return self

    def execute(self):
        if not self.exec:
            return
        className, methodName = self.exec.split("::")
        getattr(inject.instance(className), methodName)()

    def setKeyboardBtn(self, text):
        self.keyboard_btn = text
        return self

    def getKeyboardBtn(self):
        buttons = self.keyboard_btn.split("||")
        if len(buttons) <= 1 and not buttons[0]:
            return None
        return buttons
