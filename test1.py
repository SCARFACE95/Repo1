class Cafea:
    def __init__(self, tip, intensitate, aroma, cantitate):
        self.tip = tip
        self.intensitate = intensitate
        self.aroma = aroma
        self.cantitate = cantitate

    def fierbere(self):
        print("Fierbe bagamias pl")


cafea_arabica = Cafea("Arabica", "Forte", "Chill", "350g")

print(cafea_arabica.tip)
cafea_arabica.fierbere()

