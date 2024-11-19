nbretu = int(input("Donnez le nombre d'étudiants : "))
somme = 0
moy = 0.0
notes = []
for i in range(0, nbretu):
    notes.append(float(input("Note etudiant {} : ".format(i))))
    if notes[i] < 0 or notes[i] > 20 :
        while notes[i] < 0 or notes[i] > 20 :
            notes[i] = float(input("La note doit être comprise entre 0 et 20: "))
    somme += notes[i]

moy = somme / nbretu
print("Moyenne de classe : ", moy)
print("Numéro de l'Etudiant | note | ecart à la moyenne")
for i in range(0, nbretu):
    print(i,"|",notes[i],"|",notes[i] - moy)