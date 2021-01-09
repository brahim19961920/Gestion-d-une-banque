#!/usr/bin/python3

from compteEpargne import *
from compteCourant import *

class Banque:
    #Constructeur
    def __init__(self,adresseBanque, nomBanque):
        self.adresseBanque=adresseBanque
        self.nomBanque=nomBanque
        self.comptes=set()

    #ajouter un compte à la banque
    def ajouterCompte(self,compte):
        self.comptes.add(compte)
    
    #vérifier si un compte existe dans une banque
    def estPresentCompte(self,numCompte):
        for compte in self.comptes:

         if compte.num_compte==numCompte:
            return True
        return False

    #verifier si une personne posséde un compte dans la banque
    def estPresentClient(self,cin):
        for compte in self.comptes:
            if cin==compte.client.cin:
                return True
            return False
    
    #méthode retournant le nombre de comptes courant dans la banque 
    def nombreDeComptesCourant(self):
        somme=0
        for compte in self.comptes:
            if isinstance(compte,CompteCourant):
                somme+=1
        return somme
    
    # retourner le nombre de comptes d'epargnes dans la banque 
    def nombreDeComptesEpargne(self):
        somme=0
        for compte in self.comptes:
            if isinstance(compte,CompteEpargne):
                somme+=1
        return somme
    
    #méthode retournat le nombre total de comptes dans la banque
    def nombreDeComptes(self):
        return len(self.comptes)

    #méthode permettant de supprimer un compte d'une banque
    def supprimerCompte(self,numCompte):
        for compte in self.comptes:
            if numCompte==compte.num_compte:
                self.comptes.remove(compte)
                break

    #méthode permettant de retourner le nombre de compte d'un client donné
    def nombreDeComptesClient(self,cin):
        somme=0
        for compte in self.comptes:
            if compte.client.cin==cin:
                somme+=1
        return somme






