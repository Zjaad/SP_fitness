#!/usr/bin/python3
import json
import os

with open(os.path.join(os.path.dirname(__file__) , 'internationalUnits.json')) as f:
    units = json.load(f)

def convert(value , unit):
    return value * units[unit]['factor']

def fromMetric(value , unit):
    return value / units[unit]['factor']
