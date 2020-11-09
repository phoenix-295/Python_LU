class PokerPlayer:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(self.name, "Wants card")


pok = PokerPlayer()

pok("Nikhil")
