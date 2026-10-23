#goal_calculator.py 
#!/usr/bin/python3 


"""
this is a calculator , if you need a diet , this little program will help you :) 

"""


from pd import Person , TDEERMB

class Goal(TDEERMB): 
    def __init__(self, name , age, gender , workoutSplit , weight , height , activity , GOAL = 'Maintenance'):
        super().__init__(name , age, gender , workoutSplit, weight , height , activity)
        self.GOAL = GOAL.lower()
        
    def adj_cal(self):
        if self.GOAL == 'maintenance' or self.GOAL == '':
            return self.maintenance() 
        elif self.GOAL == 'cut' :
            return self.maintenance() - 400
        elif self.GOAL == 'minicut' or self.GOAL == 'supercut' :
            return (self.maintenance()/ 2) + 300
        elif self.GOAL == 'gain' or self.GOAL == 'bulk' :
            return self.maintenance() + 400
        elif self.GOAL == 'dirty bulk' or self.GOAL == 'dirtybulk' :
            return self.maintenance() + 800
        else :
            raise ValueError('the Goal param is not clear')

