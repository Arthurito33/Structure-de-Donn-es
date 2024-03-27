# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:48:13 2024

@author: arthu
"""

#Exercice 2
class Tree:
    
    def __init__(self, label, *children):
        assert type(label) is str
        self.__label = label
        self.__children = tuple(children)
        
    def alabel(self):
        return self.__label #On change le nom de la fonction pour éviter le problème entre le nom dela fonction et la variable label et children définie au dessus
    
    def achildren(self):
        return self.__children
    
    def nb_children(self):
        return len(self.__children) #La taille du tuple correspond aux nombres d'enfants (noeuds)
    
    def child(self, i : int):
        return self.__children[i] #On prend le ième tuple pour avoir le ième sous arbre
    
    def is_leaf(self):
        if self.__children==() : #Si le tuple est vide c'est bon c'est une feuille
            return True
        else:
            return False
        
#Exercice 3
    """
    def depth(self):
        dept=0
        if self.__children!=():
            dept=dept+1
        
     """

    def depth(self):
        if self.is_leaf():
            return 0
        return 1+max([p.depth() for p in self.achildren()])
     
#Exercice 4

    def __str__(self):
        if self.is_leaf():
            return self.__label 
        a=str(self.__label)
        for i in self.achildren():
            a=a+'('+str(i)+')'
        return a
              
    def __str__(self):
        n=len()
        if self.is_leaf():
            return self.__label 
        a=str(self.__label)
        for i in self.achildren():
            
        return a
    
t1=Tree('f',Tree('a'),Tree('b'))  
print(t1.achildren()) 
t2=t1.child(1)
print(t2.is_leaf())
    
t1.depth()
print(t1.depth())

t2.__str__()
print(t2.__str__())
t1.__str__()
print(t1.__str__())
#if __name__ == '__main__':
    #t1=Tree("f",[Tree('a'),Tree('b')])