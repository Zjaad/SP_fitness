#!/usr/bin/python3 

from goal_calculator import Goal

minCarb = 100
ketoCarb = 50

class Macro:
    
    """
        GAINS : 4KCAL/G
        SUPER BULK : 4KCAL/G
        FATS: 9KCAL/G
    """
    def __init__(self, energy , weight , goal = 'maintenance'):
        self.energy = energy
        self.weight = weight
        self.goal = goal

    def protein(self):
        if self.goal in {'dirty bulk', 'dirtybulk', 'gain', 'bulk'}:
            protg = self.weight * 2
        elif self.goal in {'maintenance', ''}:
            protg = self.weight * 2.2
        elif self.goal in {'minicut', 'supercut'}:
            protg = 2.6 * self.weight  #  wash minicut aggressive wla la? 2.4~2.6
        elif self.goal == 'cut' :
            protg = 2.4 * self.weight
        else:
            raise ValueError(' there is only 5 options at the moment, try 1 of em')
        protCal = protg *4 
        return protg, protCal

    def carb(self):
        carbCal = self.energy - ( self.protein()[1] + self.fat()[1])
        carbg = carbCal/ 4
        if carbg < minCarb and self.goal not in {'minicut', 'supercut'}:
            carbg = minCarb
            carbCal = carbg * 4
        elif carbg < 0:
            carbg = 0
            carbCal = 0
        return carbg,  carbCal

    def fat(self):
        if self.goal in {'cut', 'minicut', 'supercut'}:
            fatg = 0.9 * self.weight
        elif  self.goal in {'maintenance', ''}:
            fatg = 1.2 * self.weight
        elif self.goal in {'gain' , 'bulk', 'dirty bulk', 'dirtybulk'}:
            fatg = 1.35 * self.weight
        else:
            raise ValueError(' there is only 5 options at the moment, try 1 of em')
        fatCal = fatg * 9 
        return  fatg , fatCal
    
    def call(self):
        #the total_cal method
        pass

    def allMacros(self):
        k = 'kcal'
        g = 'g' 

        total_cal = self.protein()[1] + self.carb()[1] + self.fat()[1]
        AllCalories = {
                'protein' : f'{self.protein()[1]:.2f} {k}',
                'Carbohidrate': f'{self.carb()[1]:.2f} {k}',
                'Fat' : f'{self.fat()[1]:.2f} {k}',
                'total calories' : f'{total_cal:.2f} {k}'
                }
        AllAmou = {
                'protein' : f'{self.protein()[0]:.2f} {g}',
                'Carbohidrat' : f'{self.carb()[0]:.2f} {g}',
                'Fat': f'{self.fat()[0]:.2f} {g} '
                }

                 
        return AllCalories , AllAmou


