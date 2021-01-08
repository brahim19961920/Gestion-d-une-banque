#!/usr/bin/python3

from compte import *

class CompteCourant(Compte):
    def __init__(self,num_compte,depots,retraits, client, decouvert):
        super().__init__(num_compte,depots, retraits, client)
        self.decouvert=decouvert
    
    def retirer(self,somme):
        if(self.getSolde()+self.decouvert>=somme):
            self.retraits.append(somme)

































