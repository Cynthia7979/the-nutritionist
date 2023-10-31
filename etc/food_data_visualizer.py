import matplotlib.pyplot as plt
import json
import numpy as np

PATH="./food_data.json"
def get_data(path):
    with open(path) as f:
        return json.load(f)
energy=[]
vitamin=[]
mineral=[]
sodium=[]
foods = get_data(PATH)
for food in foods:
    energy.append(food["Energy"])
    vitamin.append(food["Vitamin"])
    mineral.append(food["Mineral"])
    sodium.append(food["Sodium"])

#plt.scatter(vitamin,sodium, color='b', marker='+')
#plt.scatter(energy,mineral, color='g', marker='+')
#plt.scatter(energy,sodium, color='r', marker='+')
#plt.hist(mineral,bins=50)

#plt.show()

for data in (energy,vitamin,mineral,sodium):
    print (np.mean(data))