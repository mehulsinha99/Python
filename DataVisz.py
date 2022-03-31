import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("./IPL Matches 2008-2020.csv")
#print(data.head(-5))
#print(data.info())
###Most Wins in IPL
temp = pd.DataFrame({"Winner":data['winner']})
print(temp)
count_wins = temp.value_counts()
print(count_wins)
