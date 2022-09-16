from select import select
import tkinter as tk
from tkinter import *
from tkinter import ttk
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import ODE_grapher_313
import Vector_fields3d



        
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Graph Generator Main')

        ttk.Button(self,
                text='ODE Grapher',
                command=self.open_window).pack(expand=True)
        ttk.Button(self,
            text='3D Vector Field Grapher',
            command=self.open_window2).pack(expand=True)
        ttk.Button(self,
            text='Close',
            command=self.destroy).pack(expand=True)   

        

    def open_window(self):
        window = ODE_grapher_313.create_window()

    def open_window2(self):
        window = Vector_fields3d.create_window()
   
    


if __name__ == "__main__":
    app = App()
    app.mainloop()
    
