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
        return self.__label #On change le nom de la fonction pour éviter le 
#problème entre le nom de la fonction et la variable label et children définie au dessus
    
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

    def depth(self):
        if self.is_leaf():
            return 0
        return 1+max([p.depth() for p in self.achildren()])
     
#Exercice 4
               
    def __str__(self):
        if self.is_leaf():
            return self.__label 
        a=str(self.__label)+'('
        for i in range(len(self.achildren())):
            a=a+str(self.achildren()[i].__str__())+','
        a=a[:-1]+')'
        return a
    
    def __eq__(self,__value : object):
        if self.__label!=__value.__label:
            return False
        elif self.achildren()==__value.achildren():
            for i in range(len(self.achildren())):
                if not self.achildren()[i].__eq__(__value.children()[i]):
                    return False
            return True 
        else:
            return False
            
        
        
        
        
if __name__ == '__main__':
    t1=Tree('f',Tree('a'),Tree('b'))  
    t4=Tree('f',Tree('a'),Tree('b'))
    print(t1.achildren()) 
    t2=t1.child(1)
    print(t2.is_leaf())
        
    t1.depth()
    print(t1.depth())
    
    t2.__str__()
    print(t2.__str__())
    t3=Tree('f',Tree('a'),Tree('b',Tree('c'))) 
    t3.__str__()
    print(t3.__str__())
    t1.__eq__(t3)
    print(t1.__eq__(t3))
    print(t1.__eq__(t4))
