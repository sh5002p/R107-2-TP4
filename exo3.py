nMax = 4
v1 = []
v2 = []
prodsca = 0
n = int(input("Quelle est la taille de vos vecteurs [entres 1 et 3] ? : "))
if n < 1 or n > nMax:
    while n < 1 or n > nMax:
        n = int(input("Quelle est la taille de vo vecteurs entres 1 et 3 ? : "))

print("Saisie du premier vecteur :")
for i in range(0, n):
    v1.append(float(input("v1[{}] = ".format(i))))

print("Saisie du second vecteur :")
for i in range(0, n):
    v2.append(float(input("v2[{}] = ".format(i))))

for i in range(0, n):
    prodsca += v1[i] * v2[i]

print("Le produit scalaire de v1 par v2 vaut",prodsca)