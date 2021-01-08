#!/usr/bin/python3

from compte import *

class CompteEpargne(Compte):
    def __init__(self, numcompte,depots,retraits,client,taux_interet):
        super().__init__(numcompte,depots,retraits,client)
        self.taux_interet=taux_interet
    def calculerInterets(self):
        return self.taux_interet*self.getSolde()
