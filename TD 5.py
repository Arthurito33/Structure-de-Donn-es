# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:56:50 2024

@author: arthu
"""
from random import randint
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Tk")

def cercle(x,y,r,couleur,fond):
    can.create_oval(x-r,y-r,x+r,y+r,outline=couleur,fill=fond)

#Je n'avais pas utilisé les classes originellement mais je ne réussissais pas à faire 
#l'application 3 sans ces dernières pour déduire de la rafale le nombre de tir unique fait avant
# J'ai donc repris mes fonctions à l'aide d'une classe qui compte directement le nombre de tir par le self.tir
class Cible:
    def __init__(self):
        self.tir=0
        self.point=0       

    def feu(self):       
        if self.tir<5:
            for i in range(5-self.tir):                
                x=randint(0,400)
                y=randint(0,400)
                cercle(x,y,6,'black','black')   
                self.tir=self.tir+1
                self.point=self.point+score(x,y)
            if self.tir==5:
                feu.config(state=DISABLED)
        lab=Label(root,text=f"Score de {p.point} points")
        lab.grid(row=3,column=0)
        
    def feuuniq(self,f):
        if self.tir<5:
            x=randint(0,400)
            y=randint(0,400)
            cercle(x,y,6,'black','black')   
            self.tir=self.tir+1
            self.point=self.point+score(x,y)
        if self.tir==5:
                feu.config(state=DISABLED)
        lab=Label(root,text=f"Score de {p.point} points")
        lab.grid(row=3,column=0)
            
            
def quitter():
    root.destroy()

def score(x,y):
   def distance(x,y):
        return ((x-200)**2+(y-200)**2)**(1/2) # distance entre le centre et la balle 
   dist=distance(x,y)
   if dist<=30:
       return 6
   elif dist<=60 and dist>30:
       return 5
   elif dist<=90 and dist>60:
       return 4
   elif dist<=120 and dist>90:
       return 3
   elif dist<=150 and dist>120:
       return 2
   elif dist<=180 and dist>150:
       return 1
   else:
       return 0


root.geometry("400x400")
can=Canvas(root,width='400',height='400',bg='red')
can.grid(row=0, column=0)
p=Cible()
#CERCLES :
cercle(200,200,180,'red','ivory')
cercle(200,200,150,'red','ivory')
cercle(200,200,120,'red','ivory')
cercle(200,200,90,'red','ivory')
cercle(200,200,60,'red','red')
cercle(200,200,30,'red','ivory')
#LIGNES PERPENDICULAIRES :
can.create_line(0, 200,400,200,fill='red') 
can.create_line(200, 0,200,400,fill='red')
#CHIFFRES 1 à 6 :
can.create_text(200,35,text='1',font=('Times','20','bold'),fill= 'red')
can.create_text(200,65,text='2',font=('Times','20','bold'),fill= 'red')
can.create_text(200,95,text='3',font=('Times','20','bold'),fill= 'red')
can.create_text(200,125,text='4',font=('Times','20','bold'),fill= 'red')
can.create_text(200,155,text='5',font=('Times','20','bold'),fill= 'ivory')
can.create_text(200,185,text='6',font=('Times','20','bold'),fill= 'red')
#BOUTONS : 

feu=Button(root, text='Feu !', command=p.feu)
feu.grid(row=3,column=0,sticky=W)
quitter=Button(root, text='Quitter', command=quitter)
quitter.grid(row=3,column=0,sticky=E)


#SCORE : (Test de l'affichage)

lab=Label(root,text=f"Score de {p.point} points")
lab.grid(row=3,column=0)

#TIR UNIQUE
root.bind("<f>",p.feuuniq)

root.mainloop()


#VOICI MES ANCIENNES FONCTIONS SANS CLASSES
"""
def score(x,y):
   def distance(x,y):
        return ((x-200)**2+(y-200)**2)**(1/2) # distance entre le centre et la balle 
   dist=distance(x,y)
   if dist<=30:
       return 6
   elif dist<=60 and dist>30:
       return 5
   elif dist<=90 and dist>60:
       return 4
   elif dist<=120 and dist>90:
       return 3
   elif dist<=150 and dist>120:
       return 2
   elif dist<=180 and dist>150:
       return 1
   else:
       return 0
   
def feu1():
    global point
    global compteur
    nbtir=compteur
    point=0
    while nbtir<5:
            x=randint(0,400)
            y=randint(0,400)
            cercle(x,y,6,'black','black')   
            nbtir=nbtir+1
            point=point+score(x,y)
    lab=Label(root,text=f"Score de {point} points")
    lab.grid(row=3,column=0)
    feu.config(state=DISABLED)

def tirunique(f):
    global point
    global compteur
    compteur=0
    point=0
    compteur=compteur+1
    x=randint(0,400)
    y=randint(0,400)
    cercle(x,y,6,'black','black')
    point=point+score(x,y)
    lab=Label(root,text=f"Score de {point} points")
    lab.grid(row=3,column=0)

"""