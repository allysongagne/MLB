import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\Users\Allyson\Desktop\data.csv")
df.plot(kind = 'line', x= "Year", y= "Oakland A's") 

plt.title("Oakland A's Game Wins 2000 - 2007")
plt.xlabel("Year")
plt.ylabel("Wins")

#adapted from https://stackoverflow.com/questions/29096948/plot-a-vertical-line-using-matplotlib  (T. McKinney, 2020)
plt.axvline(x=2002, color='b',ls='--', lw=2,label= 'Moneyball Season')
plt.legend()

plt.grid(ls='--', lw=0.5) 


plt.show()


