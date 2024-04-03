# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:48:38 2024

@author: arthu
"""

import matplotlib.pyplot as plt

#Exercice 2 :
      
def h(x):
    return sum(ord(c) for c in x)

class Hashtable:
    
    def __init__(self, h, N):
        self.h=h
        self.taille=N
        self.table=[None for i in range(N)]

# fonction entière avec le cas d'index pour les collisions (mauvaise compréhension de la question)
    """
    def put(self, key : str, value : int):
        index=self.h(key) % self.taille
        if self.table[index]==None:
            self.table[index]=(key,value)
        elif self.table[index][0]==key:
            self.table[index]=(key,value)
        else:
            index=(index+1)%self.taille
            while index!=self.h(key) % self.taille :
                if self.table[index]==None:
                    self.table[index]=(key,value)
                    break
                elif self.table[index][0]==key:
                    self.table[index]=(key,value)
                    break
                
    """
    def put(self, key : str, value : int):
            index=self.h(key) % self.taille
            a=[]
            if self.table[index]==None:
                self.table[index]=[(key,value)]
            else:
                for i in range(len(self.table[index])):
                    a.append(self.table[index][i][0])
            if key in a :
                for j in range(len(a)):
                    if a[j]==key:
                        self.table[index][j]=(key,value)            
            elif a!=[]:
                self.table[index].append((key,value))

#Exercice 3 :    

    def get(self,key): 
        for i in range(self.taille):
            if not self.table[i]==None :    
                for j in range(len(self.table[i])):             
                    if key==self.table[i][j][0]:
                        return self.table[i][j][1]
        else:
            return None

#Exercice 4

    def repartition(self):
        y=[]
        for i in range(self.taille):
            if self.table[i]==None:
                y.append(0)
            else:
                y.append(len(self.table[i])-1) #le -1 permet d'enlever les couples seuls qui ne forment donc pas de collision
        N = self.taille               # Autrement dit les couples seuls par case
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

#Exercice 5

liste=[]
f=open("frenchssaccent.dic",'r')
for ligne in f:
    liste.append(ligne[0:len(ligne)])
f.close()

#Modification hachage :

def h2(x):
    somme=0
    for lettre in x :
        somme=somme*33 + ord(lettre)
    return somme

if __name__ == '__main__':
    print(h('abc'))
    p=Hashtable(h,97)
    p.put('abc', 3)
    p.put('a', 12)
    p.put('aaa',4)
    p.put('aab',4)
    p.put('a',13)
    p.get('aaa')
    print(p.table)
    print(p.get('aaa'))
    print(p.get('abc'))
#Ex5 Tests
    t1=Hashtable(h,320)
    for mot in liste:
        t1.put(mot,len(mot))
    print(t1.table)
    t1.repartition()
    t2=Hashtable(h,10000)
    for mot in liste:
        t2.put(mot,len(mot))
    t2.repartition() #Le modulo  "maintient" un hachage assez bas donc la répartition n'est pas idéale
    t3=Hashtable(h2,320)
    for mot in liste:
        t3.put(mot,len(mot))
    t3.repartition()