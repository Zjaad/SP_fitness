#!/usr/bin/python3


class Person:
    def __init__(self, name, age, gender, workoutSplit ):
        self.name = name
        self._age = age
        self.__workoutSplit = workoutSplit
        self.gender = gender
        

    def set_new_workoutSplit(self, Nworkout):
        self.__workoutSplit = Nworkout

    def get_new_workoutSplit(self):
        #print (f' {self.name} , {self.__workoutSplit}')
        return f' {self.name} , {self.__workoutSplit}'

class TDEERMB(Person):
    def __init__(self, name , age, gender , workoutSplit , weight , height , activity):
        super().__init__(name, age , gender , workoutSplit)
        self.weight = weight
        self.height = height
        self.activity = activity

    def BMR(self):
        BMR = float(10 * self.weight) + (6.25 * self.height) - (5 * self._age)
        if self.gender.lower() == 'male':
            """BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age(y) + 5"""
            BMR += 5
            #print (BMR)
            return BMR
        elif self.gender.lower() == 'female' :
            """ BMR = 10 * weight + 6.25 * height - 5 * age - 161 """
            BMR -= 161 
            return BMR
        else:
            raise ValueError ('the gender should be male or female')

    def maintenance(self):
        if self.activity <= 1:
            # print(f'{self.name} Lazzy Ass')
            return self.BMR() * 1.2 
        elif self.activity <= 3 :
            #print(f'{self.name} is Lightly active')
            return self.BMR() * 1.375
        elif self.activity <= 5 : 
            # print(f'{self.name} is Moderately active')
            return self.BMR() * 1.55
        elif self.activity <= 7 : 
            #print(f'{self.name} is Very active')
            return self.BMR() * 1.73
        else:
            #print(f'{self.name} has no Life')
            return self.BMR() * 1.9 

    """ 
       maintenance = {
                1: (1.2 , f'{self.name} Lazzy Ass'),
                2: (1.375, f"{self.name} is Lightly active"),
                3: (1.55, f"{self.name} is Moderately active"),
                4: (1.73, f"{self.name} is Very active"),
                5: (1.9, f"{self.name} has no life "),
                6: (2.2, f"{self.name} is an Alien ")
                }
                """
