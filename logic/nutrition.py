from util import *
import util.json_parse as json_parse


class Person:
    # States vars TODO:
    state={
<<<<<<< HEAD
        "Energy":100,
        "Sodium":100,
        "Mineral":100,
        "Vitamin":100,
    }
    apr={
        "Age":18,#18-80
        "Health":3,#1,2,3
        "Size":1#0,1,2
    }

    # Check events(?) and update appearence
=======

>>>>>>> a810f880b8cf4b2734caaacf6dc0ea6d70fe7375
    def check_state(self):
        # Update size
        if self.state["Energy"]<50:
            self.apr["Size"]=0
        elif self.state["Energy"]>200:
            self.apr["Size"]=2
        else:
            self.apr["Size"]=1

        # Update age
        self.apr["Age"]+=1/6

        # Update health
        self.apr["Health"]=3
        
        if self.state["Energy"]<25 or self.state["Energy"]>200 or\
            self.state["Sodium"]>175 or self.state["Sodium"]<25 or\
            self.state["Mineral"]<25 or self.state["Vitamin"]<25:
                self.apr["Health"]=1

        if self.state["Energy"]<50 or self.state["Energy"]>150 or\
            self.state["Sodium"]>150 or self.state["Sodium"]<50 or\
                self.state["Mineral"]<50 or self.state["Vitamin"]<50:
                self.apr["Health"]=2




            
        if self.state["Sodium"]>200:
            return 1 #Die of heart attack
        
        if self.state["Mineral"]<0 or self.state["Vitamin"]<0:
            return 2 #Die of lack of essencials, maybe illusion
        
        if self.state["Energy"]>300:
            return 3 #Die of obesity

        if self.state["Energy"]<0:
            return 4 #Starve to death

        if self.state["Sodium"]<0:
            return 5 #Die of nervous system breakdown, maybe illusion

        return 0

    # Eat and update states
    def eat(self, foods=()):
        for food in foods:
            pass  # TODO:update state
        return self.check_state()

    def time_pass(self):
        # TODO:update state
        return self.check_state()
    

class FoodList:
    foods = {}

    def __init__(self, path):
        foods = json_parse.get_data(path)
        for food in foods:
            self.foods[food['name']]=food

    class Food:
        def __init__(self,):
            pass

#class 