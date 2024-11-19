def est_bissextile(annee):
    """Retourne True si l'année est bissextile, False sinon"""
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    return False


def verifier_date(date):
    """Vérifie si la date au format jjmmaaaa est valide"""


    if len(date) != 8 or not date.isdigit():
        print("Erreur : la date doit être au format jjmmaaaa avec 8 chiffres.")
        return


    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])


    if mois < 1 or mois > 12:
        print(f"Erreur : le mois {mois} n'est pas valide.")
        return


    jours_par_mois = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }


    if est_bissextile(annee):
        jours_par_mois[2] = 29


    if jour < 1 or jour > jours_par_mois[mois]:
        print(f"Erreur : le jour {jour} n'est pas valide pour le mois {mois}.")
        return


    print("Date valide :", date)



dates_test = [
    "3102199",  # Incorrecte (date invalide, mois de février n'a pas 31 jours)
    "31041000",  # Incorrecte (année n'existe pas)
    "32052020",  # Incorrecte (février n'a pas 32 jours)
    "30032021",  # Correcte (date valide)
    "29022022"  # Incorrecte (2022 n'est pas bissextile, donc février n'a pas 29 jours)
]

for date in dates_test:
    print(f"Test de la date : {date}")
    verifier_date(date)
    print()