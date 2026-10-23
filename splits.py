#!/usr/bin/python3
import json
import os

with open(os.path.join(os.path.dirname(__file__) , 'splits.json')) as f:
    splits = json.load(f)
