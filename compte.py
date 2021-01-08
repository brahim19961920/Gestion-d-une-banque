#!/usr/bin/python3

from personne import *

class Compte:

    #constructeur de cette classe
    def __init__(self,num_compte,depots,retraits,client):
        #on fait un controle sur les attributs:
            #num_compte de type str de 20 chiffres
            #client de type Personne
            #retraits et depots de type list
        if type(num_compte)!=str:
            raise Exception("le numero de compte doit etre de type str")
        if len(num_compte)!=20:
            raise Exception("le numéro de compte doit contenir exactement 20 caractéres")
        if num_compte.isdigit()==False:
            raise Exception("le numéro de compte contient des carcatéres non numériques")
        if type(depots)!=list or type(retraits)!=list:
            raise Exception("les attributs depots et retraits doivent etre de type list")
        if type(client)!=Personne:
            raise Exception(" Le client doit etre de type personne")

        self.num_compte=num_compte
        self.depots=depots
        self.retraits=retraits
        self.client=client
    

    def getSolde(self):
       return sum(self.depots)-sum(self.retraits)

    def __str__(self):
     return("Numéro de compte: "+self.num_compte+"\n"+str(self.client)+"\nSolde: "+str(self.getSolde()))
