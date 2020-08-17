class lieferrand:
    def __init__(self,name,artikel,preis):
        self.name= name
        self.artikel = artikel
        self.preis = preis

    def get_all(self):
        alles=[self.name, self.artikel ,self.preis]
        return alles
    
    def get_name(self):
            return self.name
    
    def get_artikel(self):
            return self.artikel
    
    def get_preis(self):
            return self.preis
