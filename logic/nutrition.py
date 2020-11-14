from util import *
class Person:
    # States vars TODO:
    state={
        "Energy":100
        "Sodium":100
        "Mineral":100
        "Vitamin":100
    }
    # Check events(?)
    def check_state(self):
        return 0
    # Eat and update states
    def eat(foods=[]):
        for food in foods:
            pass #TODO:update state
        return self.check_state()

    def time_pass():
        #TODO:update state
        return self.check_state()
    

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