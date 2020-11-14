from util import *
class Person:
    # States vars

    # Check events(?)
    def state(self):
        return 0
    # Eat and update states
    def eat(foods=[]):
        for food in foods:
            pass #update state
        return self.state()

    

class FoodList:
    foods={}
    def __init__(self,path):
        foods=json_parse.get_data(path)
        for food in foods:
            self.foods[food[name]]=food
        

    class Food:
        def __init__(self,):
            pass

#class 