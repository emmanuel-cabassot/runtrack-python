import Auteur

class Livre(Auteur):
    def __init__(self, reference, titre):
        Auteur.__init__(reference)
        self.titre = titre

    
        
          