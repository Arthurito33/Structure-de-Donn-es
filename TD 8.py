# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:48:08 2024

@author: arthu
"""
import struct


f = open('the_wall.wav', "rb")
data = f.read()
print((len(data)-44)/4)
print(data[0:44])


struct.unpack_from("I",data,40)
p=struct.unpack_from("HH",data,44)
#data.size.struct.unpack_from("I",data,4)

#EXERCICE 1
def extract(data):
    canal1=[]
    canal2=[]
    for i in range(int((len(data)-44)/4)):
        canal1.append(struct.unpack_from("hh",data,44+4*i)[0]) #4*i pour avoir le pas des 4 octets
        canal2.append(struct.unpack_from("hh",data,44+4*i)[1])
    return canal1, canal2

canal1,canal2=extract(data)

#EXERCICE 2

#nv_file=open("test.wav", "wb")


def write(canal1,canal2):
    taille1=len(canal1)*4+44-8
    taille2=len(canal1)*4
    with open("test.wav", "wb") as f:     
        f.write(b"RIFF")
        f.write(struct.pack("I", taille1))
        f.write(b"WAVE")
        f.write(b"fmt ")
        f.write(struct.pack("I", 16))
        f.write(struct.pack("H", 1))
        f.write(struct.pack("H", 2))   
        f.write(struct.pack("I", 44100))
        f.write(struct.pack("I", 176400))
        f.write(struct.pack("H", 4))
        f.write(struct.pack("H", 16))
        f.write(b"data")
        f.write(struct.pack("I",taille2))
        for i in range(int(len(canal1))):
            f.write(struct.pack("h",canal1[i]))
            f.write(struct.pack("h",canal2[i]))
      
        
#EXERCICE 3

def write2(canal1,canal2):
    taille1=len(canal1)*4+44-8
    taille2=len(canal1)*4
    with open("test.wav", "wb") as f:
        f.write(b"RIFF")
        f.write(struct.pack("I", taille1))
        f.write(b"WAVE")
        f.write(b"fmt ")
        f.write(struct.pack("I", 16))
        f.write(struct.pack("H", 1))
        f.write(struct.pack("H", 2))   
        f.write(struct.pack("I", 44100))
        f.write(struct.pack("I", 176400))
        f.write(struct.pack("H", 4))
        f.write(struct.pack("H", 16))
        f.write(b"data")
        f.write(struct.pack("I",taille2))
        for i in range(int(len(canal1)/2)): #On prend 2 fois moins de d'échantillons d'ou la division par 2
            f.write(struct.pack("h",canal1[2*i])) #i prend les valeur 0,2,4,....
            f.write(struct.pack("h",canal2[2*i]))          

