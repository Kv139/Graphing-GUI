from select import select
import tkinter as tk
from tkinter import *
from tkinter import ttk
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


# This is for my project:::
# https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# ^^ Thank you for the code ^^ 
# Sources! 
def create_system(mass, sK, damping):
        if mass == 0:
            mass = 0.0001
        myMatrix = np.array([[1, 0], [(-1 * damping / mass), (-1 * sK / mass)]])
        return myMatrix
def graph_system_1(myMatrix, initx, finx, inity, finy):
    bounds = test_bounds(initx,finx,inity,finy)
    x, y = np.meshgrid(np.linspace(bounds[0], bounds[1], 20), np.linspace(bounds[2], bounds[3], 20))
    u = y * myMatrix[0][0] + x * myMatrix[0][1]
    v = y * myMatrix[1][0] + x * myMatrix[1][1]
    color = (u + v)
    fig1,ax = plt.subplots(figsize=(7, 7))
    ax.quiver(x, y, u, v, color, alpha=0.9)
    ax.set_aspect('equal')
    ax.set_title('Model 1')
    plt.show()       
def graph_system_3(myThing, initx, finx, inity, finy):
    mass = myThing[0]
    sk = myThing[1]
    alpha = myThing[3]
    if mass == 0:
        mass = 0.0001 # no division by zero/
    bounds = test_bounds(initx,finx,inity,finy)
    x, y = np.meshgrid(np.linspace(bounds[0], bounds[1], 30), np.linspace(bounds[2], bounds[3], 20))
    u = y
    v = ((x ** 2 - alpha) / mass) * y + (sk / mass * x)
    color = (u + v)
    fig3,ax = plt.subplots(figsize=(7, 7))
    ax.quiver(x, y, u, v, color, scale=None, alpha=0.9)
    ax.set_aspect('equal')
    ax.set_title('Model 3')
    plt.show()
def graph_system_2(myThing, initx, finx, inity, finy):
        bounds = test_bounds(initx,finx,inity,finy)
        mass = myThing[0]
        sk = myThing[1]
        damping = myThing[2]
        if mass == 0:
            mass = 0.0001  # no division by zero/
        x, y = np.meshgrid(np.linspace(bounds[0], bounds[1], 20), np.linspace(bounds[2], bounds[3], 20))
        u = y
        v = (x * (-1 * (sk / mass))) + ((abs(y) * y)) * (-1 * (damping / mass))
        color = (u + v)
        fig2,ax = plt.subplots(figsize=(7, 7))
        ax.quiver(x, y, u, v, color, alpha=0.9)
        ax.set_aspect('equal')
        ax.set_title('Model 2')
        plt.show()
def graph_model1(myThing):
        mass = myThing[0]
        sk = myThing[1]
        damping = myThing[2]

        if mass == 0:
            mass = 0.0001

        def model1(y, x):
            dvdt = (x * (-1 * (sk / mass))) + ((abs(y) * y)) * (-1 * (damping / mass))
            return dvdt

        z0 = [0, 0]
        t = np.linspace(0, 5)

        V = odeint(model1, z0, t)

        plt.figure(4)
        plt.plot(t, V[:, 0], 'b-', label='We do math here')
        # plt.plot(t,z[:,1],'r--',label='#ODE')
        plt.ylabel('dy/dt')
        plt.xlabel('time')
        plt.legend(loc='best')
        plt.show()
def graph_model2(myThing):
        mass = myThing[0]
        sK = myThing[1]
        damping = myThing[2]
        alpha = myThing[3]

        def model2(y, x):
            dvdt = x * (-1 * damping / mass) + y * (-1 * sK / mass)
            return dvdt

        if mass == 0:
            mass = 0.0001  # no division by zero/

        z0 = [0, 0]
        t = np.linspace(0, 5)
        K = odeint(model2, z0, t)

        plt.figure(2)
        plt.plot(t, K[:, 0], 'b-', label=':)')
        plt.ylabel('dy/dt')
        plt.xlabel('time')
        plt.legend(loc='best')
        plt.show()
def graph_model3(myThing):
        mass = myThing[0]
        sk = myThing[1]
        alpha = myThing[3]

        def model3(y, x):
            dvdt = ((x ** 2 - alpha) / mass) * y + (sk / mass * x)
            return dvdt

        if mass == 0:
            mass = 0.0001  # no division by zero/

        z0 = [0, 0]
        t = np.linspace(0, 5)
        z = odeint(model3, z0, t)


        plt.figure(3)
        plt.plot(t, z[:, 0], 'b-', label='This is so cool')
        plt.ylabel('dy/dt')
        plt.xlabel('time')
        # plt.legend(loc='best')
        plt.show()    
def test_bounds(initx,finx,inity,finy):
    xs = initx
    xf = finx
    ys = inity
    yf = finy
    if (xs > xf):
        xs = -2
        xf = 2
    if (ys > yf):
        ys = -2
        yf = 2
    return[xs,yf,ys,yf]

def create_window():
    def graph_system():
        global entry
        myInitCond = [float(entry0.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()),
                    float(init_x.get()), float(fin_x.get()), float(init_y.get()), float(fin_y.get())]
        myThing = create_system(myInitCond[0], myInitCond[1], myInitCond[2])
        graph_system_1(myThing, myInitCond[4], myInitCond[5], myInitCond[6], myInitCond[7])

    def graph_system2():
        global entry
        myInitCond = [float(entry0.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()),
                    float(init_x.get()), float(fin_x.get()), float(init_y.get()), float(fin_y.get())]
        graph_system_2(myInitCond, myInitCond[4], myInitCond[5], myInitCond[6], myInitCond[7])
    
    def graph_system3():
        global entry
        myInitCond = [float(entry0.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()),
                    float(init_x.get()), float(fin_x.get()), float(init_y.get()), float(fin_y.get())]
        graph_system_2(myInitCond, myInitCond[4], myInitCond[5], myInitCond[6], myInitCond[7])

    def graph_system3vT():
        global entry
        myInitCond = [float(entry0.get()), float(entry2.get()), float(entry3.get()), float(entry4.get())]
        graph_model3(myInitCond)

    def graph_system2vT():
        global entry
        myInitCond = [float(entry0.get()), float(entry2.get()), float(entry3.get()), float(entry4.get())]
        graph_model2(myInitCond)

    def graph_system1vT():
        global entry
        myInitCond = [float(entry0.get()), float(entry2.get()), float(entry3.get()), float(entry4.get())]
        graph_model1(myInitCond)
    #initialize tinkter frame
    win = Tk()
    win.geometry("500x400")
    win.configure(background="pink")
    win.title("ODE Grapher")
    #label Window
    mass = Label(win, text="Mass", font=("Courier 22"), bg="black", fg="pink", pady="2", justify="left")
    sK = Label(win, text="Spring Const", font=("Courier 22"), bg="black", fg="pink", pady="2")
    Damping = Label(win, text="Dampening", font=("Courier 22 "), bg="black", fg="pink", pady="2")
    Alpha = Label(win, text="Alpha", font=("Courier 22 "), bg="black", fg="pink", pady="2")
    initialx = Label(win, text="Init-x", font=("Courier 22", 12), bg="black", fg="pink", pady="2", justify="left")
    finalx = Label(win, text="Final-x", font=("Courier 22", 12), bg="black", fg="pink", pady="2", justify="left")
    initialy = Label(win, text="Init-y", font=("Courier 22", 12), bg="black", fg="pink", pady="2", justify="left")
    finaly = Label(win, text="final-y", font=("Courier 22", 12), bg="black", fg="pink", pady="2", justify="left")

    #Create field boxes and initialize values
    entry0 = Entry(win, width=10)
    entry2 = Entry(win, width=10)
    entry3 = Entry(win, width=10)
    entry4 = Entry(win, width=10)
    entry0.insert(-1, '2')
    entry2.insert(-1, '.5')
    entry3.insert(-1, '2.2')
    entry4.insert(-1, '4')
    init_x = Entry(win, width=5)
    fin_x = Entry(win, width=5)
    init_y = Entry(win, width=5)
    fin_y = Entry(win, width=5)
    init_x.insert(-1,"-1")
    fin_x.insert(-1, "1")
    init_y.insert(-1,"-1")
    fin_y.insert(-1,"1")

    #Place && focus buttons
    mass.place(x=10, y=12)
    entry0.focus_set()
    entry0.place(x=10, y=52)
    sK.place(x=200, y=12)
    entry2.focus_set()
    entry2.place(x=200, y=52)
    Damping.place(x=10, y=110)
    entry3.focus_set()
    entry3.place(x=10, y=150)
    Alpha.place(x=200, y=110)
    entry4.focus_set()
    entry4.place(x=200, y=150)
    initialx.place(x=10, y=300)
    entry0.focus_set()
    init_x.place(x=10, y=330)
    finalx.place(x=80, y=300)
    entry0.focus_set()
    fin_x.place(x=80, y=330)
    initialy.place(x=150, y=300)
    entry0.focus_set()
    init_y.place(x=150, y=330)
    finaly.place(x=230, y=300)
    entry0.focus_set()
    fin_y.place(x=230, y=330)

    but = ttk.Button(win, text="Graph System 1", width=20, command=graph_system)
    but.pack(side=LEFT)
    but2 = ttk.Button(win, text="Graph System 2", width=20, command=graph_system2)
    but2.pack(side=LEFT)
    but3 = ttk.Button(win, text="Graph System 3", width=20, command=graph_system3)
    but3.pack(side=LEFT)
    but4 = ttk.Button(win, text="Time versus dV/dt 1", width=20, command=graph_system1vT)
    but4.place(x=0, y=250)
    but4 = ttk.Button(win, text="Time versus dV/dt 2", width=20, command=graph_system2vT)
    but4.place(x=130, y=250)
    but4 = ttk.Button(win, text="Time versus dV/dt 3", width=20, command=graph_system3vT)
    but4.place(x=260, y=250)

    exit_button = Button(win, text="Exit", command=win.destroy, width=15)
    exit_button.place(x=350,y=350)
    win.mainloop()
