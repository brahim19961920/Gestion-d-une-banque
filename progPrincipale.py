#!/usr/bin/python3
from banque import*

#programme principale
#içi on test les différentes méthodes de chaque class edu projet

b=Banque("14 boulevard carnot, Cannes, 06400","Crédit agricole")
p=Personne("12345678912345678910","Brahim","BEN AMIRA","0767441080")
c=Compte("12356478912345678910",[123],[],p)

p1=Personne("123456789123456789dk10","Brahim","BEN AMIRA","0767441080")
p2=Personne("1234567891234567ig8910","Brahim","BEN AMIRA","0767441080")
c1=Compte("02356478912745678910",[123],[],p)
c2=CompteEpargne("92356478911145678910",[123],[],p1,0.1)
c3=CompteEpargne("12356478912345678910",[123],[],p2,0.2)
c4=CompteCourant("12656478912345678910",[123],[],p,200)
b.comptes.add(c)

b.ajouterCompte(c)
b.ajouterCompte(c1)
b.ajouterCompte(c2)


b.ajouterCompte(c3)
b.ajouterCompte(c4)

b.supprimerCompte("12356478912345678910")
print(b.estPresentCompte("12356478912345678910"))
print(b.estPresentCompte("123i6478912345678910"))


print(b.estPresentClient("12345678912345678910"))
print(b.estPresentClient("10005678912345678910"))

print(b.nombreDeComptes())
print(b.nombreDeComptesCourant())
print(b.nombreDeComptesEpargne())

print(b.nombreDeComptesClient("12345678912345678910"))

print(b.nombreDeComptesClient("12340678912345678910"))




















