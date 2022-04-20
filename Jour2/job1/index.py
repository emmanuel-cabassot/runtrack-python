class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Auteur(Personne):
    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self.oeuvre = []
        
    def listeOeuvre(self):
        print(self.oeuvre)

    def ecrireUnLivre(self, titre):
        self.oeuvre.append(titre)
        return self.oeuvre

        
class Livre():
    def __init__(self, titre, Auteur):
        self.titre = titre
        self.auteur = Auteur

    def printLivre(self):
        print(self.auteur.prenom)

A1 = Auteur("jean", "michel")

A1.ecrireUnLivre("fdsfdss")
A1.ecrireUnLivre("mes couilles")
livre = Livre("ca vient du livre", A1)


A1.listeOeuvre()




        
