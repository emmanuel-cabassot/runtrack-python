class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        print("je m'appelle " +  self.prenom + " " + self.prenom)

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.nom
    

personne1 = Personne("Emmanuel", "Cabassot")
personne2 = Personne("Jeremy", "Dejoux")
personne3 = Personne("Phillipe", "Lek")

personne1.sePresenter()
personne2.sePresenter()
personne3.sePresenter()

personne1.getNom()
personne1.setNom("pipo")
print(personne1.getNom())