#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

from classess.Transition import Transition

class State:
    def __init__(self, name):
        self._name = name
        self._transitions = []

    def getName(self):
        return self._name

    def getTransitions(self):
        return self._transitions

    def setTransitions(self, transition_list):
        self._transitions = transition_list

    def getTransitionByText(self, text) -> Transition:
        for transition in self._transitions:
            if re.match(transition.getInput(), text):
                return transition
