import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np
columns = ["Pitcher","RelSpeed" ]
df=pd.read_csv("20231028-19510020-681313.csv", usecols=columns)
plt.scatter(df.RelSpeed, df.Pitcher)
plt.show()