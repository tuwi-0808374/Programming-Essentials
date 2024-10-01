class Auto():
    def __init__(self, merk, prijs, km):
        self.merk = merk
        self.prijs = prijs
        self.kilometers_jaar = km

    def geef_info(self):
        print(f"Merk auto: {self.merk}")
        print(f"Prijs: {self.prijs}")
        print(f"Km: {self.kilometers_jaar}")

# auto = Auto("Opel", 20000, 1259643)

while True:
    merk = input("Voer merk in:")
    print()
    prijs = input("Voer prijs in:")
    print()
    kilometers = input("Voer kilometers in:")
    print()

    auto = Auto(merk, prijs, kilometers)
    # print(f"Auto: {auto.merk}, {auto.prijs}, {auto.kilometers_jaar}")
    auto.geef_info()

    break
