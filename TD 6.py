# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:51:56 2024

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

root.geometry("400x400")
graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

WIDTH=400
HEIGHT=400

pos = np.array([(random()*WIDTH, random()*HEIGHT) for i in range(len(graph))])

vit = np.array([((random()-0.5)*10, (random()-0.5)*10) for i in range(len(graph))])

can=Canvas(root,width='400',height='400')
can.grid(row=0, column=0)

class Graph:
    def __init__(self):
        self.graph=graph
        self.pos=pos
        self.vit=vit
        self.Funitx=0
        self.Funity=0
        self.bary=0
        self.force_frott=0
    def draw(self, can, graph, pos):
        can.delete(ALL)
        number=0
        for i in range(len(self.graph)):
            for j in self.graph[i]:  # sucs de i a j
                can.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for (x, y) in self.pos:
            can.create_oval(x-10,y-10,x+10,y+10,fill="#f3e1d4")
            can.create_text(x,y,text=str(number), font=('Times','9','bold'))
            number+=1
        
#EXERCICE 2/3




    def norm(self, pos,i,j):
        return sqrt((self.pos[i][0]-self.pos[j][0])**2+(self.pos[i][1]-self.pos[j][1])**2)
    
    
    def ressort(self, pos): 
        for i in range(len(self.graph)):
            self.Funitx=0
            self.Funity=0
            adj=self.graph[i] #tous les sommets adjacents
            for j in adj:                                             
                self.Funitx = self.Funitx -k*(self.norm(pos, i, j)-l0)*((self.pos[i][0]- self.pos[j][0])/self.norm(pos,i,j))  
                self.Funity = self.Funity -k*(self.norm(pos, i, j)-l0)*((self.pos[i][1]- self.pos[j][1])/self.norm(pos,i,j))
                
            self.force_frott = -k2*self.vit[i] #Une force de frottement pour ralentir le mouvement
            self.bary=sum((self.pos-200)/len(self.pos))   #Pour garder le graphe au milieu   
            self.vit[i]=vit[i]+(tau*(self.Funitx+self.force_frott[0]),tau*(self.Funity+self.force_frott[1]))
            self.pos[i] = (self.pos[i][0] + self.vit[i][0]*tau - self.bary[0], self.pos[i][1] + self.vit[i][1]*tau- self.bary[1])    
        self.draw(can, self.graph, self.pos)
            

#CONSTANTES
tau=0.1
k=1
k2=1
l0=100
#EXECUTION
p=Graph()
p.draw(can,graph,pos)
root.bind("<f>", p.ressort)
root.mainloop()