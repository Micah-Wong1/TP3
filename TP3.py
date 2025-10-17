"""
Nom = Micah
Gr = 406
Ce code cree une scenario ou le jouer doit combattre des monstres une apres l'autre,
et  chaque 3 victoires, un boss de haut difficulte apparaitre,
le but du jeu est dele de survie le plus longtemps possible avec 30 HP au depart
"""
import random
jeu = True

dice_throw = 0
second_throw = 0
force_ennemi = 0
boss_appear = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nbr_victoire_consecutive = 0
combat_statut = "-"
nbr_vie = 30
showed_rules = False


def force_pers(low, high):
    force = random.randint(low, high)
    return force


while jeu:
    if not showed_rules:
        if boss_appear % 3 == 0 and boss_appear != 0:
            force_ennemi = force_pers(9, 24)
            print(f"Vous tombez face à face avec un boss de haut difficulté : {force_ennemi}")
        else:
            force_ennemi = force_pers(2, 11)
            print(f"Vous tombez face à face avec un adversaire de difficulté : {force_ennemi}")
    else:
        if boss_appear % 3 == 0 and boss_appear != 0:
            print(f"Vous tombez face à face avec un boss de haut difficulté: {force_ennemi}")
        else:
            print(f"Vous tombez face à face avec un adversaire de difficulté : {force_ennemi}")
    showed_rules = False

    rep = int(input("""Que voulez-vous faire ?
    1- Combattre cet adversaire
    2- Contourner cet adversaire et aller ouvrir une autre porte
    3- Afficher les règles du jeu
    4- Quitter la partie
    """))
    if rep == 1:
        if boss_appear % 3 == 0 and boss_appear != 0:
            dice_throw = force_pers(1, 12)
            second_throw = force_pers(1, 12)
        else:
            dice_throw = force_pers(1, 6)
            second_throw = force_pers(1, 6)
        numero_combat += 1
        print(f"""Combat {numero_combat}: nombre de victores:{nombre_victoires} vs nombres de defaites:{nombre_defaites}
Niveau de vie de l’usager: {nbr_vie}
Force de l’adversaire: {force_ennemi}""")
        print(f"""Lancer du dé : {dice_throw} 
Lancer du deuxieme dé : {second_throw}
Force total du jouer : {dice_throw + second_throw}""")
        if dice_throw + second_throw <= force_ennemi:
            if boss_appear % 3 == 0 and boss_appear != 0:
                boss_appear = 0
            nombre_defaites += 1
            nbr_vie -= force_ennemi
            combat_statut = "defaite"
            nbr_victoire_consecutive = 0
            print(f"Derniere combat = {combat_statut}")
            print(f"Niveau de vie = {nbr_vie}")

        elif dice_throw + second_throw > force_ennemi:
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
            nbr_vie -= 7
            print(f"""Il y a une pénalité de 7 point de vie. 
Niveau de vie = {nbr_vie}""")
            boss_appear = 0
        else:
            nbr_vie -= 2
            print(f"""Il y a une pénalité de 2 point de vie. 
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
        il y a une pénalité de 2 point de vie. Si l'usager evite un boss, il y a une penalite de 7 point de vie
        
        """)

    elif rep == 4:
        print("Merci et au revoir...")
        jeu = False

    if nbr_vie <= 0:
        combat_statut = "-"
        print(f"Vous n'avez plus de vie")
        print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
        reply = str(input("voulez-vous redémarrer? (y/n)"))
        if reply == "y":
            nbr_vie = 30
            nombre_defaites = 0
            nombre_victoires = 0
            numero_combat = 0
            print("vous avez redémarré avec 30 points de vie")
            print(f"Derniere combat = {combat_statut}")
            print(f"Niveau de vie = {nbr_vie}")
        elif reply == "n":
            print("Merci et au revoir...")
            jeu = False
