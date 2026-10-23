#!/usr/bin/python3
import json
import os

with open(os.path.join(os.path.dirname(__file__) , 'vitaminsMinerals.json') , encoding = 'utf-8') as f:
    data = json.load(f)

def ageGroup(age):
    if age <= 13:
        return '9-13'
    elif age <= 18:
        return '14-18'
    elif age <= 30:
        return '19-30'
    elif age <= 50:
        return '31-50'
    elif age <= 70:
        return '51-70'
    else:
        return '71+'

def needs(gender , age):
    group = ageGroup(age)
    result = {}
    for name , info in data['nutrients'].items():
        entry = info[gender][group]
        result[name] = {'target' : entry['target'] , 'unit' : info['unit'] , 'kind' : entry['kind'] , 'max' : entry['max'] , 'maxNote' : info['maxNote'] , 'group' : info['group']}
    return result

def notes(gender , age):
    group = ageGroup(age)
    result = []
    for name , info in data['nutrients'].items():
        if info['note'] and group in info['noteFor'][gender]:
            result.append(f'{name} : {info["note"]}')
    return result
