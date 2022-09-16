from lib2to3.pgen2.pgen import generate_grammar
from locale import normalize
from select import select
import tkinter as tk
from tkinter import *
from tkinter import ttk
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


def identify_string(word):
    trig_functions=['cos','sin','tan','sec','csc','cot', 'sqrt', 'pi']
    i = 0
    j = 0
    while i < len(trig_functions):
        result = word.find(trig_functions[i])
        while result != -1:
            j = result
            word = word[:j] + 'np.' + word[j:] 
            result = word.find(trig_functions[i], j+4)
        i += 1
    return word


def generate_graph(function1, function2, function3):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x, y , z = np.meshgrid(np.arange(-2, 15, 2),
                            np.arange(-2,15, 2),
                            np.arange(-2, 15, 2))
    u = eval(function1)
    v = eval(function2)
    w = eval(function3)    
    ax.quiver(x, y, z, u, v, w, length=1.0, alpha=0.8, normalize=True)
    plt.show()

       
def create_window():
    win = Tk()
    win.title("3D Vector Fields")
    win.geometry("400x300")
    win.configure(background="pink")
  
    def graph_system():
        global entry
        generate_graph(identify_string(entry0.get()),identify_string(entry2.get()),identify_string(entry3.get()))
    U = Label(win, text="i\u0302 as x,y,z", font=("Courier 15"), bg="black", fg="pink", pady="2")
    V = Label(win, text="j\u0302 as x,y,z", font=("Courier 15"), bg="black", fg="pink", pady="2")
    W = Label(win, text="k\u0302 as x,y,z", font=("Courier 15 "), bg="black", fg="pink", pady="2")


    U.place(x=10, y=20)
    U.configure()
    V.place(x=10,y=95)
    V.configure
    W.place(x=10,y=170)
    W.configure()

    entry0 = Entry(win, width=15)
    entry2 = Entry(win, width=15)
    entry3 = Entry(win, width=15)

    entry0.insert(-1,'sin(x)')
    entry2.insert(-1,'cos(y)')
    entry3.insert(-1, '-1 * pi')


    entry0.pack()
    entry0.place(x=250, y=20)
    entry2.place(x=250, y=95)
    entry3.place(x=250, y=170)

    but = ttk.Button(win, text="Generate Graph", width=20, command=graph_system)
    but.place(x=10, y=220)

    exit_button = Button(win, text="Exit", command=win.destroy, width=15)
    exit_button.place(x=250,y=250)
    win.mainloop()
