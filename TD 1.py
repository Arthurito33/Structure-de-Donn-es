# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:53:39 2024

@author: arthu
"""

#Exercice 1/2

liste=[]
f=open("frenchssaccent.dic",'r')
for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
f.close()

def scrabble(tirage):
    if len(tirage)>8 :
        return "Mot trop long"
    else:
        motposs=[]      
        for i in range(len(liste)):
            g=1
            for lettre in liste[i]:
                if lettre not in tirage :
                    g=0                    
            if g==1 : 
                motposs.append(liste[i]) 
                #print(motposs)
    p=len(motposs)
    solution=motposs[0]
    for i in range(p):
        if len(solution)<=len(motposs[i]):
            solution=motposs[i]
    return solution 
                
            
#Exercice 3

#Dictionnaire ou liste sont possibles

def score(mot):
    score=0
    mot1=list(mot)
    #print(mot1)
    for i in mot1:
        if i in ['a','e','l','i','n','o','r','s','t','u']:
            score=score+1
        if i in ['d','g','m']:
            score=score+2
        if i in ['b','c','p']:
            score=score+3
        if i in ['f','h','v']:
            score=score+4
        if i in ['j','q']:
            score=score+8
        if i in ['k','w','x','y','z']:
            score=score+10
    return score
score('scrabble')

def max_score(plsmots):
    maxmot=plsmots[0]
    for i in range(len(plsmots)) :
        if score(maxmot)<=score(plsmots[i]):
            maxmot=plsmots[i]
    return maxmot,score(maxmot)

max_score(['cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct'])  

#Exercice 4
#On modifie score pour rajouter le '?'
def score1(mot):
    score=0
    mot1=list(mot)
    #print(mot1)
    for i in mot1:
        if i in ['a','e','l','i','n','o','r','s','t','u']:
            score=score+1
        if i in ['d','g','m']:
            score=score+2
        if i in ['b','c','p']:
            score=score+3
        if i in ['f','h','v']:
            score=score+4
        if i in ['j','q']:
            score=score+8
        if i in ['k','w','x','y','z']:
            score=score+10
        if i=='?':
            score=score
    return score
alphabet=['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
          
def scrabble2(tirage):
    if '?' in tirage:
        motposs=[]      
        for j in range(len(alphabet)):
            for k in range(len(tirage)):
                if tirage[k]=='?':
                    tirage[k]=alphabet(j)
            motposs.append(scrabble(tirage))
        for i in range(len(liste)):
            g=1
            for lettre in liste[i]:
                if lettre not in tirage :
                    g=0                    
            if g==1 : 
                motposs.append(liste[i])                    
        p=len(motposs)
        solution=motposs[0]
        for i in range(p):
            if len(solution)<=len(motposs[i]):
                solution=motposs[i]
        return solution    
    else :
        return scrabble(tirage)