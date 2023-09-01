from random import randint

data = {
    "element": ["papier", "pierre", "ciseaux"],
    1: "Le papier enveloppe la pierre !",
    2: "Les ciseaux coupent le papier !",
    3: "La pierre casse les ciseaux !",
    "winner": ["10", "21", "02"] }

while True:
    joueur = input("pierre, papier ou ciseaux: ")
    if (joueur in data["element"]):
        choix, joueur = randint(0, 2), data["element"].index(joueur)

        if choix != joueur: break
        print("Égalité, recommencez...")

    else: print("Faute de frappe !")

print(f'Vous avez {"gagné" if (str(choix) + str(joueur)) in data["winner"] else "perdu"} ! {data[choix + joueur]}')