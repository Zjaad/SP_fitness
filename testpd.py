#!/usr/bin/python3
from pd import Person , TDEERMB
from goal_calculator import Goal
from macros import Macro 
""" name , age, gender , workoutSplit , weight , height , activity , GOAL = 'Maintenance' """

#adolf  = TDEERMB('adolf' , 35 , 'Einzwei', 70 , 170 , 4)
#adolf.BMR()
#print(adolf.maintenance())
#adolf.TDEERMB(70 , 170 , 4)
#manal = TDEERMB('manalmanalmanal' , 90 , 'lbka' ,90 , 150 , 2)
#manal.BMR()
#print(manal.maintenance())

#adolf.get_new_workoutSplit()
#adolf.set_new_workoutSplit('bro split')
#adolf.get_new_workoutSplit()
manal = Goal('manal' , 20 ,'female',  'Upper Lower' , 70 , 150 , 5 , 'gain')
#calories = manal.adj_cal()
#bmr = manal.BMR()
#maintenance  = manal.maintenance()

#Macro = (energy , weight , goal = 'maintenance')
#cPerson = Macro(calories , manal.weight , manal.GOAL)
#print(cPerson)
#print(f"BMR: {bmr}")
#print(f"Maintenance Calories: {maintenance}")
#print(f"Calories: {calories}")
#macros = cPerson.allMacros()
#print(macros)
from time import sleep
li = ['gain' , 'dirty bulk' , 'minicut']
for i in li : 
    Zakaria = Goal('zakaria' , 27 , 'male' , 'Arnold_Split' , 90 , 177 , 6 , i)
    calories = Zakaria.adj_cal()
    bmr = Zakaria.BMR()
    maintenance = Zakaria.maintenance()
    MZ = Macro(calories , Zakaria.weight , Zakaria.GOAL)
    Macros = MZ.allMacros()
    print( f' {Macros} \n BMR : {bmr} \n Maintenance Calories: {maintenance} \n Calories: {calories}')
    sleep(3)

