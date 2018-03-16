#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

from classess.Transition import Transition
from classess.State import State

class StateConfig:
    def __init__(self, content):
        self._content = content
        self._states = []
        for stateXMLParam in self._content.find_all('state'):
            self._states.append(self.buildState(stateXMLParam))

    def buildState(self, stateXMLParam):
        state = State(stateXMLParam['name'])
        transitions = stateXMLParam.find_all('transition')
        transitionsList = []
        for transitionParam in transitions:
            transitionsList.append(Transition() \
                                   .setText(transitionParam['text']) \
                                   .setInput(transitionParam['input']) \
                                   .setNextState(transitionParam['next_state']) \
                                   .setExecFunction(transitionParam['exec']) \
                                   .setKeyboardBtn(transitionParam['keyboard_btn']))
        state.setTransitions(transitionsList)
        return state

    def getStateByName(self, state_name):
        for state in self._states:
            if state.getName() == state_name:
                return state
