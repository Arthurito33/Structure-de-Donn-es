# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:50:11 2024

@author: arthu
"""
#Exercie 1
from math import gcd, pi
class Fraction:
    

#Méthode permettant d'initialiser la classe :



    def __init__(self,num,denom):
        self.num=num
        assert denom!=0
        self.denom=denom
    def __str__(self):
        return f"{self.num}/{self.denom}" #Nouvelle fonction qui écrit la fraction ex:3/4
        

#
#Exercice 2
    def add(self,fraction):
        self.num=self.num*fraction.denom+self.denom*fraction.num # formule ad+bc/bd
        self.denom=self.denom*fraction.denom
        
    def mult(self,fraction):
        self.num=self.num*fraction.num
        self.denom=self.denom*fraction.denom
        
    def simplify(self):
        assert gcd(self.num, self.denom)
        b=gcd(self.num,self.denom)
        self.num=int(self.num/b)
        self.denom=int(self.denom/b)
        
if __name__ == '__main__':
    fraction1=Fraction(3,4)
    fraction2=Fraction(1,4)
    print(fraction1)
    print(fraction2)
    fraction1.add(fraction2)
    print(fraction1)
    fraction1.mult(fraction2)
    print(fraction1)
    fraction1.simplify()
    print(fraction1)

#Exercice 3
def H(n):
    f1=Fraction(0,1)
    for i in range(1,n+1):
        f2=Fraction(1,i) #on crée une variable f2 pour que ce ne soit pas un objet dans le add d'après
        f1.add(f2)
        f1.simplify()
    return f1

print(H(10000))

#Exercice 4

def leibniz(n):
    f1=Fraction(0,1)
    for i in range(n+1):
        f2=Fraction((-1)**i,2*i+1) #le (-1)**i détermine le signe devant la fraction
        f1.add(f2)
        f1.simplify()
    return f1

print(leibniz(10000))
print(float(leibniz(10000)))

#Exercice 5

class Polynomial :
        def __init__(self,liste):
            assert type(liste)==list()
            self.coef=liste
            
        def __str__(self):
            nbrcoef=len(self.coef)
            for i in range(nbrcoef):
                pol=str(self.coef[i]+'x'**(n-i+1))
                

        
    





