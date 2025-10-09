"""
Nom = Micah
Gr = 406
Ce code
"""
import random
jeu = True


def encounter():
    global numero_adversaire
    global numero_combat
    global nombre_victoires
    global nombre_defaites
    global nbr_victoire_consecutive
    global combat_statut
    force_ennemi = random.randint(1, 5)
    global nbr_vie
    print(f"Vous tombez face à face avec un adversaire de difficulté : {force_ennemi}")
    rep = int(input("""Que voulez-vous faire ?
    1- Combattre cet adversaire
    2- Contourner cet adversaire et aller ouvrir une autre porte
    3- Afficher les règles du jeu
    4- Quitter la partie
    """))
    if rep == 1:
        numero_adversaire += 1
        numero_combat += 1
        dice_throw = random.randint(1, 6)
        print(f"""Adversaire: {numero_adversaire}
Force de l’adversaire: {force_ennemi}
Niveau de vie de l’usager: {nbr_vie}
Combat {numero_combat}: nombre de victores:{nombre_victoires} vs nombres de defaites:{nombre_defaites}""")
        print(f"Lancer du dé : {dice_throw} ")
        if dice_throw <= force_ennemi:
            nombre_defaites += 1
            nbr_vie -= force_ennemi
            combat_statut = "defaite"
            nbr_victoire_consecutive = 0
            if nbr_vie <= 0:
                combat_statut = "-"
                print(f"Vous avez {nbr_vie} de vie")
                print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
                reply = str(input("voulez-vous redémarrer? (y/n)"))
                if reply == "y":
                    print("vous avez redémarré avec 20 points de vie")
                    nbr_vie = 20
                elif reply == "n":
                    print("Merci et au revoir...")
                    global jeu
                    jeu = False
            print(f"Derniere combat = {combat_statut}")
            print(f"Niveau de vie = {nbr_vie}")
        elif dice_throw > force_ennemi:
            nombre_victoires += 1
            nbr_vie += force_ennemi
            combat_statut = "victoire"
            nbr_victoire_consecutive += 1
            print(f"Derniere combat = {combat_statut}")
            print(f"Niveau de vie = {nbr_vie}")
            print(f"Nombre de victoires consécutives : {nbr_victoire_consecutive}")

    elif rep == 2:
        nbr_vie -= 1
        print(f"""Il y a une pénalité de 1 point de vie. 
Niveau de vie = {nbr_vie}""")

    elif rep == 3:
        print("""
        Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  
        Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
            
        une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de 
        l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

        La partie se termine lorsque les points de vie de l’usager tombent sous 0.

        L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, 
        il y a une pénalité de 1 point de vie. 
        
        """)

    elif rep == 4:
        print("Merci et au revoir...")
        jeu = False


numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nbr_victoire_consecutive = 0
combat_statut = "-"
nbr_vie = 20

while jeu:
    encounter()
