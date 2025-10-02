"""
Nom = Micah
Gr = 406
Ce code
"""
import random
jeu = True


def encounter():
    while jeu:
        numero_adversaire = 0
        numero_combat = 0
        nombre_victoires = 0
        nombre_defaites = 0
        nbr_victoire_consecutive = 0
        combat_statut = "victoire"
        force_ennemi = random.randint(1, 5)
        nbr_vie = 20
        print(f"Vous tombez face à face avec un adversaire de difficulté : {force_ennemi}")
        rep = int(input("""Que voulez-vous faire ?
        1- Combattre cet adversaire
        2- Contourner cet adversaire et aller ouvrir une autre porte
        3- Afficher les règles du jeu
        4- Quitter la partie"""))
        if rep == 1:
            numero_adversaire += 1
            numero_combat += 1
            dice_throw = random.randint(1, 6)
            print(f"""Adversaire: {numero_adversaire}
            Force de l’adversaire: {force_ennemi}
            Niveau de vie de l’usager: {nbr_vie}
            Combat {numero_combat}: {nombre_victoires} vs {nombre_defaites}""")
            print(f"Lancer du dé : {dice_throw} ")
            if dice_throw <= force_ennemi:
                nombre_defaites += 1
                combat_statut = "defaite"
                print(f"Derniere combat = {combat_statut}")
                print(f"Niveau de vie = {nbr_vie}")
            elif dice_throw > force_ennemi:
                nombre_victoires += 1
                print(f"Derniere combat = {combat_statut}")
                print(f"Niveau de vie = {nbr_vie}")
                print(f"Nombre de victoires consécutives : {nbr_victoire_consecutive}")

        elif rep == 2:

        elif rep == 3:

        elif rep -- 4:


