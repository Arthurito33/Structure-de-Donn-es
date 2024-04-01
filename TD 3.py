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
        elif self.nb_children()==__value.nb_children():
            for i in range(len(self.achildren())):
                if not self.achildren()[i].__eq__(__value.achildren()[i]):
                    return False   
            return True 
        else:
            return False
            
        
#Exercice 5   
# Ma fonction dérivée n'est pas finie j'ai un problème avec l'opérateur * que je ne comprends pas
    """def deriv(self,var: str):
       Tree_list=[]
       for i in range(self.nb_children()):
           if self.child(i).is_leaf():
              Tree_list.append(Tree('0')) 
           elif self.child(i).alabel()==var:
               if self.child(i).is_leaf():
                   Tree_list.append(Tree('1'))
               else:
                    a=self.child(i).child(0).nb_children()
                    A=[Tree(var)]*(a)
                    Tree_list.append(Tree(str(a+1),Tree('*',*A)))
           else:
                if self.child(i).child(0).nb_children()==1:
                    Tree_list.append(Tree(self.child(i).get_label()))
                else:
                    a=self.child(i).child(0).nb_children()
                    A=[Tree(var)]*(a-1)
                    Tree_list.append(Tree(str(int(self.child(i).alabel())*(a)),Tree('*',*A)))

       return Tree('+',*Tree_list) """
                   
                   
               
        
        
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
    t5=Tree('+',Tree('*',Tree('3'),Tree('X'),Tree('X')),Tree('*',Tree('5'),Tree('X')),Tree('7'))
    print(t5.__str__())
    #print(t5.deriv('X'))