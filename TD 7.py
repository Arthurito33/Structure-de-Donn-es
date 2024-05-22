# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:50:07 2024

@author: arthu
"""

from tkinter import *
from tkinter import ttk, ALL
import numpy as np
from random import *
from math import sqrt


#EXERCICE 1
root=Tk()
root.title("Tk")
root.geometry("800x800")

graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]
pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])
col_index = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']


class Graph1:
    def __init__(self,pos,graph,col_index):
        self.pos=pos
        self.graph=graph
        self.col=col_index
        self.numcol=[0,1,2,3,4,5,6,7,8,9,10,11]    
        
    def draw(self,can):
        N = len(self.graph)
        for e in can.find_all():
            can.delete(e)
        for i in range(N):
            for j in self.graph[i]:  # sucs de i a j
                can.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for i in range(N):
            x, y = self.pos[i]
            can.create_oval(x-6, y-6, x+6, y+6, fill=self.col[i])
            can.create_text(x-12,y,text=f"{i}")
            
#EXERCICE 2
    
    """def voisins(self,i):
        somvois=self.graph[i]
        for j in range(len(self.graph)):
            if i in self.graph[j]:
                somvois.append(j)
        return somvois"""
        
            

    def min_local(self, i):
        mini=self.col[i]
        for k in self.graph[i] :
            if self.col[k]<mini:
                mini=self.col[k]
        self.col[i]=mini
        for j in self.graph[i]:
            if self.col[j]>mini:
                self.col[j]=mini
                self.min_local(j) #recursivité pour régler le problème sur le graphe en ligne
                #Quand tous les sommets ne sont pas atteints car je parcours dans le sens croissant
                #(ici comme 7 est séparé de 3 et 1 par exemple)
              
#EXERCICE 3        
        
    def connexe(self):
        for s in range(len(self.graph)):
            self.min_local(s)
        self.draw(can)

#EXERCICE 4

def color_generator():
    r, g, b = randint(0,255), randint(0,255),randint(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"

def draw_grille(can):
    #boules de diamètres 5 et qui sont toutes espacées de 3
    #donc le centre de deux boules concécutives est séparé de 8
    for i in range(5,401,8):
        probai= randint(0,1)
        for j in range(5,401,8):
            probaj= randint(0,1)
            can.create_oval(i-(2.5), j-(2.5), i+(2.5), j+(2.5), fill=color_generator())
            if probai<=0.4:
                can.create_line(i,j+2.5,i,j+5.5)
            elif probaj<=0.4:
                can.create_line(i+2.5,j,i+5.5,j)           


graph2 = [[2], [], [4], [1], [6], [3], [7], [5]]
pos2 = [[100, 200], [450, 200], [150, 200], [400, 200], [200, 200], [350, 200], [250, 200], [300, 200]]


can=Canvas(root,width='800',height='800')
can.grid(row=0, column=0)
p=Graph1(pos2,graph2,col_index)
#print(p.voisins(3))
p.draw(can)
p.connexe()
#draw_grille(can)
root.mainloop()