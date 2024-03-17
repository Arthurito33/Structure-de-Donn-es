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

#On peut utiliser un Dictionnaire ou une liste. Le plus adapté reste le dictionnaire dans ce cas à mon avis.
#En TD, j'avais effectué mes fonctions score et maxscore sans utiliser de dictionnaire,mais dans la partie 4 que j'ai repris chez moi je vais utiliser ddes dictionnaires pour faciliter la lecture et l'usage
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
#Uilisons donc les dictionnaires cette fois avec le joker
valeurlettre= {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'd': 2, 'g': 2, 'm': 2, 'b': 3, 'c': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'j': 8, 'q': 8, 'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}
def scrabbles2(tirage):
    motposs=[]
    solution=[]
    for i in range(len(liste)):
        lettreparlettre=list(motposs[i])
        joker=0 # on va essayer de faire la différence entre les mots et le joker
        for j in range(len(tirage)):
            if tirage[j] in lettreparlettre :
                lettreparlettre.remove(tirage[j])
        if len(lettreparlettre)==1 :
            if '?' in tirage :
                joker=lettreparlettre[0]
                solution.append((motposs[i],joker)
        if len(lettreparlettre)==0:
                solution.append(motposs[i],joker))
        return solution #si joker=0 pas besoin, sinon c'est la lettre qu'il faut

#On change la fonction score qui est modifiée

def score2(solution):
    scorelist=[]
    for lettreparlettre in solution:
        valeur=0
        lettre=list(lettreparlettre[O])
        joker=lettreparlettre[1]
        for i in lettre:
            valeur=valeur + valeurlettre[i]
        if joker != 0:
            valeur=valeur +valeurlettre[joker]
        scorelist.append(valeur)
    return scorelist
    

          
