#!/usr/bin/env python

import json
from pprint import pprint as pp

with open('projectproposal.json') as data_file:
    data = json.load(data_file)
pp(data)
