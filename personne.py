#!/usr/bin/python3

class Personne:
    #Constructeur de la classe Personne
    def __init__(self,cin,nom,prenom,numtel):

        #Il faut faire un controle sur les attributs de la classe:
            #numtel doit etre une str contenant uniquement des chiffres
            #meme chose pour cin

        assert type(numtel)==str, "Le numéro de télephone doit etre de type str"
        assert numtel.isdigit()==True, "Le numéro de télephone  ne doit contenir que des chiffres"
        assert type(cin)==str, "Le numéro de carte d'identite doit etre de type str"

        self.cin=cin#numéro de carte d'identité
        self.nom=nom
        self.prenom=prenom
        self.numtel=numtel#numéro de télephone
    
    #Méthode affichant les informations d'une Personne         
    def __str__(self):
        return"Informations sur la personne:\ncin: {} \nPrénom:{} \nNom: {}\nnuméro de télephone:{}".format(self.cin,self.prenom,self.nom,self.numtel) 
