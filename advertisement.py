# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:10:39 2020

@author: Miaufs_comp
"""

from PIL import Image
from PIL import ImageTk
import numpy as np
import tkinter as tk

class GUI():
    def __init__(self):
        self.plot_window = tk.Tk()
        
    def load_image(self, image_source):
        self.image = Image.open("buy.bmp")
#        self.image.show()
#        self.source = np.array(self.image)
        print(self.image.height)
        self.advertisement_poster = tk.Canvas(self.plot_window, width=self.image.width, height=self.image.height)
        self.advertisement_poster.grid(row = 0, column = 0)
        ph = ImageTk.PhotoImage(self.image)
        print(ph)
        pointer_to_image = self.advertisement_poster.create_image(0, 0, image=ph, anchor=tk.NW)
        
    def show_image(self):
#        im1 = self.image.crop((50, 0, 51, 29)) 
#        img = Image.fromarray(self.source[0,:], 'RGB')
#        self.advertisement_poster.
        ph = ImageTk.PhotoImage(self.image)
        print(ph)
        self.advertisement_poster.create_image(0, 0, image=ph, anchor=tk.NW)
#        im1.show() 
#        print(im1)
#        self.fig_A_Nr = self.fig_A.create_image(0, 0, image=self.ref_to_Aimg, anchor=NW)
#        self.image_on_the_screen = MapNr
#        self.R_img = Image.open(self.input_folder_figures+"R"+str(self.image_on_the_screen)+".jpg")
#        self.ref_to_Rimg = ImageTk.PhotoImage(self.R_img)
#        self.fig_R.itemconfig(self.fig_R_Nr, image = self.ref_to_Rimg)
#        


GUI1 = GUI()
GUI1.load_image("buy.bmp")
#GUI1.show_image()
GUI1.plot_window.mainloop()