#!/usr/bin/python3

from goal_calculator import Goal


""" water_ml = 2000 (men) or 1600 (women) -- EFSA 2010 : the adequate intake of total water is 2.5 L / 2.0 L , about 80% of it comes from drinks 
adding 350ml each 30min of exercise (an estimate , ACSM says to measure your own sweat loss) -- water_ml = base + (exercise_minutes // 30) * 350 
 passing self.gender , and self.activity_Level """


class Water(Goal):
    def __init__(self, name , age, gender , workoutSplit , weight , height , activity , GOAL = 'Maintenance'):
        super().__init__(name, age, gender , workoutSplit , weight , height , activity , GOAL)

    def calc(self):
        minutes = 80
        if self.GOAL in {'dirty bulk', 'dirtybulk'}:
            minutes = 130
        water_ML = 2000
        if self.gender.lower() == 'female':
            water_ML = 1600
        if self.activity >= 1:
            return water_ML + ((minutes // 30)*350)
        else:
            return  water_ML

    def __str__(self):
        return f'you need {self.calc()} ml per day'
