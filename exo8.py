personne = {
    'firstname': 'VotrePrénom',  # Remplacer par votre prénom
    'name': 'VotreNom',          # Remplacer par votre nom
    'promo': 'VotrePromo',       # Remplacer par votre promotion
    'group': 'VotreGroupe'       # Remplacer par votre groupe de TP
}


print(f"votre nom est '{personne['name']}', prénom est '{personne['firstname']}', vous faites partie de la promo '{personne['promo']}' et votre groupe est '{personne['group']}'")
print("\nLes clés du dictionnaire sont :")
for key in personne.keys():
    print(f"- {key}")

print("\nLes valeurs du dictionnaire sont :")
for value in personne.values():
    print(f"- {value}")

print("\nLes tuplets du dictionnaire sont :")
for item in personne.items():
    print(f"- {item}")