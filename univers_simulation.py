from tkinter import *
import numpy as np
from math import *
import random

tk = Tk()
cnv=Canvas(tk, width=1000, height=600, bg="black")
cnv.pack(padx=5, pady=5)

x = 50

fails = 0
sun = cnv.create_oval(475, 275, 525, 325, fill="yellow")
Msun = 1000
Mrock = [100, 50, 75]
G = 0.5
def create_rock(i):
    global rock_x, rock_y, v_rock_x, v_rock_y
    rock_x[i] = random.randint(1, 1000)
    rock_y[i] = random.randint(0, 1)*600
    v_rock_x[i] = random.randint(-100, 100)/10
    v_rock_y[i] = random.randint(-50, 50)/10

def d(i):
    return sqrt((rock_x[i]-500)*(rock_x[i]-500)+(rock_y[i]-300)*(rock_y[i]-300))


rock_x = [random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)]
rock_y = [0, 0, 0]
v_rock_x = [random.randint(-100, 100)/5, random.randint(-100, 100)/5, random.randint(-100, 100)/5]
v_rock_y = [random.randint(0, 100)/5, random.randint(0, 100)/5, random.randint(0, 100)/5]
rock = [0, 0, 0]
i = 0
rock[i] = cnv.create_oval(rock_x[i]-11, rock_y[i]-11, rock_x[i]+11, rock_y[i]+11, fill="brown")
i = 1
rock[i] = cnv.create_oval(rock_x[i]-7, rock_y[i]-7, rock_x[i]+7, rock_y[i]+7, fill="brown")
i = 2
rock[i] = cnv.create_oval(rock_x[i]-9, rock_y[i]-9, rock_x[i]+9, rock_y[i]+9, fill="brown")

def move():
    global rock_x, rock_y, v_rock_x, v_rock_y, rock, G, Msun, Mrock, fails, sun, x
    
    for i in range(0,3):
        cnv.delete(sun)

        a_rock = (G*Msun*Mrock[i])/(d(i)*d(i))

        if(d(i)<x):
            cnv.delete(rock[i])
            create_rock(i)
            fails += 1
        elif(rock_x[i]>1000 or rock_x[i]<0 or rock_y[i]>600 or rock_y[i]<0):
            cnv.delete(rock[i])
            create_rock(i)
            fails += 1
        if(rock_x[i] >= 500):
            v_rock_x[i] -= a_rock*sqrt((500-rock_x[i])*(500-rock_x[i]))/d(i)
        
        else:
            v_rock_x[i] += a_rock*sqrt((500-rock_x[i])*(500-rock_x[i]))/d(i)
        
        if(rock_y[i] >= 300):
            v_rock_y[i] -= a_rock*sqrt((rock_y[i]-300)*(rock_y[i]-300))/d(i)
        
        else:
            v_rock_y[i] += a_rock*sqrt((rock_y[i]-300)*(rock_y[i]-300))/d(i)
        
        rock_x[i] += v_rock_x[i]
        rock_y[i] += v_rock_y[i]
        cnv.delete(rock[i])
        rock[i] = cnv.create_oval(rock_x[i]-8, rock_y[i]-8, rock_x[i]+8, rock_y[i]+8, fill="brown")
        sun = cnv.create_oval(450, 250,550, 350, fill="yellow")
        print(fails)
    
    tk.after(50, move)

move()

tk.mainloop()