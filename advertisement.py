# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:10:39 2020

@author: Miaufs_comp
"""

import numpy as np
from tkinter import *
from PIL import ImageTk, Image

class GUI():
    def __init__(self):
        pass
#        
    def load_image(self, image_source):
        self.plot_window = Tk()
        self.plot_window.title("3D slice")
         #Opening first images
        self.R_img = Image.open("buy.gif")
        self.ref_to_Rimg = ImageTk.PhotoImage(self.R_img)
        width, height = self.R_img.size
        
        # Create a real canvas
        self.fig_R = Canvas(self.plot_window)
        self.fig_R.grid(column=0, row=0, sticky=(N, W, E, S))
        self.fig_R.config(width = width, height = height)
        self.fig_R_Nr = self.fig_R.create_image(0, 0, image=self.ref_to_Rimg, anchor=NW)


GUI1 = GUI()
GUI1.load_image("buy.bmp")
##GUI1.show_image()
GUI1.plot_window.mainloop()
