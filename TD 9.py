# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:49:29 2024

@author: arthu
"""
from random import *

class Polynomial :
        def __init__(self,liste,n,q):
            assert type(liste)==list
            self.coef=liste
            self.n=n
            self.q=q
            for i in self.coef:
                assert 0<i<q
                
        def modulo(self): # J'avais intialement mis cette fonction directement dans __init__ mais cela posait problème pour la fction add 
            for i in range(len(self.coef)): # en effet, L'ajout des 2 polynomes n'était pas mis sous modulo
                if i>=self.n:
                    self.coef[i%self.n]=((-1)**(i//self.n))*self.coef[i]+self.coef[i%self.n]
                    self.coef[i]=0
            for j in range(len(self.coef)):
                self.coef[j]=self.coef[j]%self.q
        
            
        
        def __str__(self):
            nbrcoef=len(self.coef)
            pol=str()           
            for i in range(nbrcoef):                  
                if i == nbrcoef-1:
                    pol=pol+str(self.coef[i])+'*x**'+str(i)
                else :
                    pol=pol+str(self.coef[i])+'*x**'+str(i)+'+'
            return pol

#EXERCICE 2

        def add(self,poly2):
            assert self.n==poly2.n
            assert self.q==poly2.q
            t1=len(self.coef)
            t2=len(poly2.coef)
            mini=min(t1,t2) # pour éviter les problèmes de longueurs j'effectue les ajouts de 0 sur la liste la plus petite
            if mini==t1: #comme mes polynomes sont déjà sous la forme de l'ex 1 le reste des coeffs de la liste plus longue seront nuls
                self.coef=self.coef+[0 for i in range(t2-t1)] 
            if mini==t2:
                poly2.coef=poly2.coef+[0 for i in range(t1-t2)] 
            for i in range(mini):
                self.coef[i]=self.coef[i]+poly2.coef[i]   
            self.modulo()
            
#EXERCICE 3

        def mul(self,poly2):
            assert self.n==poly2.n
            assert self.q==poly2.q
            t1=len(self.coef)
            t2=len(poly2.coef)
            pdev=[0 for i in range(t1+t2)]
            for i in range(t1):
                for j in range(t2):
                    pdev[i+j]=pdev[i+j]+self.coef[i]*poly2.coef[j]               
            self.coef=pdev    
            self.modulo()
                    
            
            
            
#EXERCICE 4

        def scalar(self, c):
            for i in range(len(self.coef)):
                self.coef[i]=(c*self.coef[i])%self.q
                
        def rescale(self,r):
            P=Polynomial(self.coef, self.n, r)
            P.modulo()
            
        def fscalar(self, r , alpha):
            Q=[0 for i in range(len(self.coef))]
            for i in range(len(self.coef)):
                Q=round(self.coef[i]*alpha)%r
    
            
        
            
            
if __name__ == '__main__':
    p1=Polynomial([1,2,3,4,5],2,6)
    p2=Polynomial([2,2,3,4],2,6)
    p1.modulo()
    print(p1)
    p1.add(p2)
    print(p1 ,"Test addition")
    p3=Polynomial([1,2],2,6)
    p3b=Polynomial([2,2],2,6)
    p3.mul(p3b)
    print(p3,"Test Mutliplication")
    p2.scalar(3)
    print(p2)
    p4=Polynomial([1,2,3,4,5,1],2,6)
    p4.fscalar(3,2)
    print(p4, "Test Fscal")
