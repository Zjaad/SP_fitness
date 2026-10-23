#!/usr/bin/python3 



vitamins = {
        'A': '900 µg',
        'C': '90 mg',
        'D': '15 µg (600 IU)',
        'E': '15 mg',
        'K': '120 µg',
        'B1': '1.2 mg',
        'B2': '1.3 mg',
        'B3': '16 mg',
        'B5': '5 mg',
        'B6': '1.3 mg',
        'B7': '30 µg',
        'B9': '400 µg',
        'B12': '2.4 µg',
        }

print('your Daily intake of vitamins is : ')

for i in vitamins:
    print ( '->    ' 'vitamin' , i, ':' ,   vitamins[i]) #, vitamins[i].values())
