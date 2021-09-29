import matplotlib.pyplot as plt

#data 
# y1 = number of game wins by team with highest home run count
# y2 = number of game wins by team with highest on base percentage
# y3 = number of game wins by world series champion 
# x = mlb season year
y1 = [83,90,79,83,71,72,73,72]
y2 = [94,97,95,98,95,103,116,90]
y3 = [96,83,99,98,91,99,92,87]
x = [2007,2006,2005,2004,2003,2002,2001,2000]

plt.plot (x, y1, color="y", label='Team with Highest HR')
plt.plot (x, y2, color= "c", label='Team with Highest OBP')
plt.plot (x,y3, color="m", label= 'World Series Champ')

#adapted from https://stackoverflow.com/questions/29096948/plot-a-vertical-line-using-matplotlib  (T. McKinney, 2020)
plt.axvline(x=2002, color='b',ls='--', lw= 2,label= 'Moneyball Season')
plt.legend()

#graph labels 
plt.title("Home Run Count (HR) and On Base Percentage (OBP) Impact on Game Wins")
plt.xlabel("Year")
plt.ylabel("Game Wins")
plt.grid(ls='--', lw=0.5) 

plt.show()
