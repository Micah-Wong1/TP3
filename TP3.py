"""
Nom = Micah
Gr = 406
Ce code
"""
import random
jeu = True


def encounter():
    print(f"Vous tombez face à face avec un adversaire de difficulté : {force_ennemi}")
    global rep
    rep = input("""Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie""")


while jeu:
    force_ennemi = random.randint(1, 5)
    nbr_vie = 20
