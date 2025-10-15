"""
Nom = Micah
Gr = 406
Ce code cree une scenario ou le jouer doit combattre des monstres
"""
import random
jeu = True

force_ennemi = 0
boss_appear = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nbr_victoire_consecutive = 0
combat_statut = "-"
nbr_vie = 20
showed_rules = False


def force_pers(low, high):
    force = random.randint(low, high)
    return force


while jeu:
    if not showed_rules:
        if boss_appear % 3 == 0 and boss_appear != 0:
            force_ennemi = force_pers(7, 12)
            dice_throw = force_pers(1, 12)
            print(f"Vous tombez face à face avec un boss de haut difficulté : {force_ennemi}")
        else:
            force_ennemi = force_pers(1, 5)
            print(f"Vous tombez face à face avec un adversaire de difficulté : {force_ennemi}")

    rep = int(input("""Que voulez-vous faire ?
    1- Combattre cet adversaire
    2- Contourner cet adversaire et aller ouvrir une autre porte
    3- Afficher les règles du jeu
    4- Quitter la partie
    """))
    if rep == 1:
        numero_combat += 1
        dice_throw = force_pers(1, 6)
        print(f"""Combat {numero_combat}: nombre de victores:{nombre_victoires} vs nombres de defaites:{nombre_defaites}
Niveau de vie de l’usager: {nbr_vie}
Force de l’adversaire: {force_ennemi}""")
        print(f"Lancer du dé : {dice_throw} ")
        if dice_throw <= force_ennemi:
            if boss_appear % 3 == 0 and boss_appear != 0:
                boss_appear = 0
            nombre_defaites += 1
            nbr_vie -= force_ennemi
            combat_statut = "defaite"
            nbr_victoire_consecutive = 0
            print(f"Derniere combat = {combat_statut}")
            print(f"Niveau de vie = {nbr_vie}")

        elif dice_throw > force_ennemi:
            boss_appear += 1
            nombre_victoires += 1
            nbr_vie += force_ennemi
            combat_statut = "victoire"
            nbr_victoire_consecutive += 1
            print(f"Derniere combat = {combat_statut}")
            print(f"Niveau de vie = {nbr_vie}")
            print(f"Nombre de victoires consécutives : {nbr_victoire_consecutive}")

    elif rep == 2:
        if boss_appear % 3 == 0 and boss_appear != 0:
            nbr_vie -= 8
            print(f"""Il y a une pénalité de 8 point de vie. 
Niveau de vie = {nbr_vie}""")
            boss_appear = 0
        else:
            nbr_vie -= 1
            print(f"""Il y a une pénalité de 1 point de vie. 
Niveau de vie = {nbr_vie}""")

    elif rep == 3:
        showed_rules = True
        print("""
        Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  
        Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
            
        une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de 
        l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

        La partie se termine lorsque les points de vie de l’usager tombent sous 0.

        L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, 
        il y a une pénalité de 1 point de vie. Si l'usager evite un boss, il y a une penalite de 5 point de vie
        
        """)

    elif rep == 4:
        print("Merci et au revoir...")
        jeu = False

    if nbr_vie <= 0:
        combat_statut = "-"
        print(f"Vous avez {nbr_vie} de vie")
        print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
        reply = str(input("voulez-vous redémarrer? (y/n)"))
        if reply == "y":
            nbr_vie = 20
            numero_combat = 0
            print("vous avez redémarré avec 20 points de vie")
            print(f"Derniere combat = {combat_statut}")
            print(f"Niveau de vie = {nbr_vie}")
        elif reply == "n":
            print("Merci et au revoir...")
            jeu = False
