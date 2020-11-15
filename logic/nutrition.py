from util import *
import util.json_parse as json_parse


class Person:
    def __init__(self, energy=100, sodium=100, mineral=100, vitamin=100,
                 age=18, health=3, size=1):
        self.state = {
            "Energy": energy,
            "Sodium": sodium,
            "Mineral": mineral,
            "Vitamin": vitamin,
        }
        self.apr = {
            "Age": age,  # 18-80
            "Health": health,  # 1,2,3
            "Size": size  # 0,1,2
        }

    # Check events(?) and update appearance
    def check_state(self):
        # Update size
        if self.state["Energy"] < 50:
            self.apr["Size"] = 0
        elif self.state["Energy"] > 200:
            self.apr["Size"] = 2
        else:
            self.apr["Size"] = 1

        # Update age
        self.apr["Age"] += 1/6

        # Update health
        self.apr["Health"] = 3
        
        if self.state["Energy"] < 25 or self.state["Energy"] > 200 or\
            self.state["Sodium"] > 175 or self.state["Sodium"] < 25 or\
            self.state["Mineral"] < 25 or self.state["Vitamin"] < 25:
                self.apr["Health"] = 1

        if self.state["Energy"] < 50 or self.state["Energy"] > 150 or\
            self.state["Sodium"] > 150 or self.state["Sodium"] < 50 or\
            self.state["Mineral"] < 50 or self.state["Vitamin"] < 50:
                self.apr["Health"] = 2


        if self.state["Sodium"] > 200:
            return 1  # Die of heart attack
        
        if self.state["Mineral"] < 0 or self.state["Vitamin"] < 0:
            return 2  # Die of lack of essencials, maybe illusion
        
        if self.state["Energy"] > 300:
            return 3  # Die of obesity

        if self.state["Energy"] < 0:
            return 4  # Starve to death

        if self.state["Sodium"] < 0:
            return 5  # Die of nervous system breakdown, maybe illusion

        if self.apr["Age"]>80:
            return 6  # Die for living too long

        return 0

    # Eat and update states
    def eat(self, foods=()):
        if foods == ():
            render_text("You give up eating and go back to work")
        else:
            render_text("You enjoyed your food very much")
        for food in foods:
            self.state["Energy"] += 5/300 * food["Energy"]
            self.state["Vitamin"] += 1/100 * food["Vitamin"]
            self.state["Mineral"] += 1/3000 * food["Mineral"]
            self.state["Sodium"] += 1/100 * food["Sodium"]
            # TODO:fine-tune the parameters
        return self.check_state()

    def time_pass(self):
        self.state["Energy"] -= 5
        self.state["Vitamin"] -= 1
        self.state["Mineral"] -= 1
        self.state["Sodium"] -= 3
        render_text("You feel hungry and start ordering food.")
        return self.check_state()
    

class FoodList:
    foods = {}

    def __init__(self, path):
        foods = json_parse.get_data(path)
        for food in foods:
            self.foods[food['name']] = food

    class Food:
        def __init__(self,):
            pass

#class
