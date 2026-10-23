#!/usr/bin/python3

from goal_calculator import Goal


""" water_ml = weight_kg * 35 
adding 350ml each 30min -- water_ml = (weight_kg * 35) + (exercise_minutes // 30) * 350 
 passing self.weight , and self.activity_Level """


class Water(Goal):
    def __init__(self, name , age, gender , workoutSplit , weight , height , activity , GOAL = 'Maintenance'):
        super().__init__(name, age, gender , workoutSplit , weight , height , activity , GOAL)

    def calc(self):
        minutes = 80
        if self.GOAL in {'dirty bulk', 'dirtybulk'}:
            minutes = 130
        water_ML = self.weight * 35
        if self.activity >= 1:
            return water_ML + ((minutes // 30)*350)
        else:
            return  water_ML

    def __str__(self):
        return f'you need {self.calc()} ml per day'
