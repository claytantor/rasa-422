#!/usr/bin/env python
#coding: utf-8

import argparse
import logging
import sys
import json

from dronzecore.rasa import RasaPyClient

def main():
    print "starting."

    parser = argparse.ArgumentParser()
    parser.add_argument('--modeldir', type=str, required=True,
                       help='the name of the model dir.')
    parser.add_argument('--config', type=str, required=True,
                       help='the config file to be used for startup.')
    parser.add_argument('--text', type=str, required=True,
                       help='which user should the session start with.')

    args = parser.parse_args()

    rasa = RasaPyClient(args.modeldir, args.config)

    print json.dumps(rasa.parse(args.text), indent=4)

if __name__ == '__main__':
    main()
