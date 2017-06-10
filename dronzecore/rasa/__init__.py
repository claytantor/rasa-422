#!/usr/bin/env python
# coding: utf-8

from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

class RasaPyClient():

    def __init__(self, metadata_path, config_path):
        # get the metadata config from the package data
        metadata = Metadata.load(metadata_path)
        self.interpreter = Interpreter.load(metadata, RasaNLUConfig(config_path))

    def parse(self, text):
        response = self.interpreter.parse(unicode(text.strip(),encoding="utf-8"))
        return response

    def get_statement(self, intent_name):
        return self.intents[intent_name]
