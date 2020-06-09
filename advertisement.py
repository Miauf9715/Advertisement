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
        self.current_column = 1
        self.image_height = 0
        self.image_width = 0
        self.cropped_width = 10
        
    def load_image(self, image_source):
        self.plot_window = Tk()
        self.plot_window.title("3D slice")
        
        # Opening first images
        self.R_img = Image.open(image_source)
        self.image_width, self.image_height = self.R_img.size
        self.R_img_cropped = self.R_img.crop((self.current_column,1,self.current_column+self.cropped_width,self.image_height))
        self.ref_to_Rimg = ImageTk.PhotoImage(self.R_img_cropped)
        
        # Create a real canvas
        self.fig_R = Canvas(self.plot_window)
        self.fig_R.grid(column=0, row=0, sticky=(N, W, E, S))
        self.fig_R.create_rectangle(0, 0, 400, 400, fill="black")
        self.fig_R.config(width = 400, height = 400)
        self.fig_R_Nr = self.fig_R.create_image(200, 100, image=self.ref_to_Rimg, anchor=NW)
        
    def show_image(self):
        self.R_img_cropped = self.R_img.crop((self.current_column,1,self.current_column+self.cropped_width,self.image_height))
        self.ref_to_Rimg = ImageTk.PhotoImage(self.R_img_cropped)
        self.fig_R.itemconfigure(self.fig_R_Nr, image=self.ref_to_Rimg)
        if self.current_column <= self.image_width-12:
           self.current_column += 1
        else:
           self.current_column = 1
#        print(self.current_column)
        self.fig_R.after(1,self.show_image)
           
GUI1 = GUI()
GUI1.load_image("buy.bmp")
GUI1.show_image()
GUI1.plot_window.mainloop()
