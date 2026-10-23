#!/usr/bin/python3
from pd import Person , TDEERMB
from goal_calculator import Goal
from macros import Macro , ketoCarb
from Water_in import Water
from units import convert , fromMetric
from splits import splits
from vitamins import needs , notes
from cli import banner , paint , frame , cyan , red , yellow
from time import sleep
import json
import string

def Ask(question , kind = str):
    while True:
        try:
            return kind(input(question))
        except ValueError:
            print(paint('invalide input' , red))

def Choose(question , options):
    print(question)
    for i , option in enumerate(options , 1):
        print(paint(f' ► {i} - {option}' , cyan))
    while True:
        pick = Ask(' > ' , int)
        if 1 <= pick <= len(options):
            return options[pick - 1]
        print(paint('unknown input' , red))

def AskNum(question , kind , low , high):
    while True:
        number = Ask(question , kind)
        if low <= number <= high:
            return number
        print(paint(f'it should be between {low} and {high}' , red))

def AskName(question):
    while True:
        name = Ask(question).strip()
        if name != '' and all(c in string.ascii_letters + ' ' for c in name):
            return name
        print(paint('use only letters (a-z) and spaces' , red))


print(banner)
name = AskName('enter your name : ')
system = Choose(' units (metric = kg and cm , US = lb and ft/in) : ' , ['metric' , 'US'])
age = AskNum('enter your age : ' , int , 12 , 100)
while True:
    gender = Choose(' male or female? : ' , ['male' , 'female' , 'banana'])
    if gender != 'banana':
        break
    Choose("you can fool a Banana whenever, but you can't Fool all bananas forver" , ['ok'])
    print(paint('GO FIGHT FOR YOUR RIGHT BANANA!' , yellow))
ws = Choose(' what is your split : ' , list(splits))
days = splits[ws]['days']
if ws == 'Custom (personal)':
    ws = Ask(' name your split : ')
if system == 'US':
    weight = convert(AskNum('enter your weight in lb : ' , float , 66 , 660) , 'lb')
    feet = AskNum('enter your height - feet : ' , int , 4 , 8)
    inches = AskNum('enter your height - inches : ' , int , 0 , 11)
    height = convert(feet , 'ft') + convert(inches , 'in')
else:
    weight = AskNum('enter your weight in kg : ' , float , 30 , 300)
    height = AskNum('enter your height in cm :  ' , float , 100 , 250)
useDays = 'no'
if days > 0:
    useDays = Choose(f' your split trains {days} days a week , use {days} ? ' , ['yes' , 'no'])
if useDays == 'yes':
    activity = days
else:
    activity = AskNum(' how many times you exercice per week :  ' , int , 0 , 14)
g = Choose('enter you goal :  ' , ['maintenance' , 'cut' , 'minicut' , 'gain' , 'dirty bulk'])
#UserTDEERMB = TDEERMB(name , age , gender , ws , weight , height , activity , g)
User = Water(name , age , gender , ws , weight , height , activity , g)
Calories = User.adj_cal()
bmr = User.BMR()
maintenance = User.maintenance()
UserMacro = Macro(Calories , User.weight , User.GOAL)
macros = UserMacro.allMacros()
water = User.calc()
report = {
        'name' : name ,
        'goal' : User.GOAL ,
        'split' : ws ,
        'BMR' : round(bmr , 2) ,
        'maintenance' : round(maintenance , 2) ,
        'goal_calories' : round(Calories , 2) ,
        'protein_g' : round(UserMacro.protein()[0] , 2) ,
        'carb_g' : round(UserMacro.carb()[0] , 2) ,
        'fat_g' : round(UserMacro.fat()[0] , 2) ,
        'total_kcal' : round(UserMacro.protein()[1] + UserMacro.carb()[1] + UserMacro.fat()[1] , 2) ,
        'water_ml' : round(water)
        }
vita = needs(gender , age)
report['vitamins'] = {}
for nutrient , v in vita.items():
    report['vitamins'][nutrient] = {'target' : v['target'] , 'unit' : v['unit'] , 'kind' : v['kind'] , 'max' : v['max']}


print(f'-----------------------welcome {name}---------------------------')
def Clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        print(paint(frame([' 1 - calculate BMR' , ' 2 - calculate your maintenance Kcal' , ' 3 - calculate Macros' , ' 4 - Water intake/day' , ' 5 - Vitamins and minerals' , ' 0 - exit']) , cyan))
        choice = int(input(' > '))
        if choice == 1 :
            print(f'Your BMR is: {bmr:.2f}')
        elif choice == 2 :
            print(f'Your Maintenance Calories: {maintenance:.2f}')
        elif choice == 3 :
            protein = UserMacro.protein()
            carb = UserMacro.carb()
            fat = UserMacro.fat()
            print(' Macros :')
            print(f' protein        {protein[0]:>8.2f} g   {protein[1]:>9.2f} kcal')
            print(f' Carbohidrate   {carb[0]:>8.2f} g   {carb[1]:>9.2f} kcal')
            print(f' Fat            {fat[0]:>8.2f} g   {fat[1]:>9.2f} kcal')
            print(f' total calories {protein[1] + carb[1] + fat[1]:>24.2f} kcal')
            if User.GOAL in {'minicut' , 'supercut'} and carb[0] < ketoCarb:
                print(paint(' low carb (keto range) : the first 7 days are the hardest , it gets easier after that' , cyan))
                print(paint(' if you have a medical condition , talk to your doctor first' , cyan))
        elif choice == 4 :
            if system == 'US':
                print(f'Water : {fromMetric(water , "floz"):.0f} fl oz')
            else:
                print(f'Water : {water:.0f} ml')
        elif choice == 5 :
            print(f'Vitamins and minerals for a {age} y {gender} :')
            lastGroup = ''
            for nutrient , v in vita.items():
                if v['group'] != lastGroup:
                    print(paint(f' -- {v["group"]}s --' , cyan))
                    lastGroup = v['group']
                star = '*' if v['kind'] == 'AI' else ' '
                if v['max'] is None:
                    limit = 'no max set'
                else:
                    limit = f'max {v["max"]:,} {v["unit"]}'
                    if v['maxNote']:
                        limit += f' - {v["maxNote"]}'
                print(f' {nutrient:<30} {v["target"]:>6,} {v["unit"]:<7}{star}  {limit}')
            print(' * = adequate intake (an estimate , less certain than an RDA)')
            for line in notes(gender , age):
                print(' note - ' + line)
        elif choice == 0 :
            print(f' Bye fat_ass')
            break
        else:
            print(paint('unknown input' , red))
        if choice in {1 , 2 , 3 , 4 , 5}:
            after = Choose(' what now ? ' , ['go back' , 'export json report'])
            if after == 'export json report':
                with open(f'{name}_raport.json' , 'w') as f:
                    json.dump(report , f , indent = 4)
                print(paint(f'saved : {name}_raport.json' , cyan))
                sleep(2)
        else:
            sleep(2)
        Clear()
    except ValueError:
        print(paint('invalide input' , red))

with open(f'{name}_raport.txt', 'w') as f:
    f.write(f'name : {name}, \n BMR : {bmr:.2f}, \n Maintenance : {maintenance:.2f}, \n Macros : {macros}')
