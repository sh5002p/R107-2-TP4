n = float(input("Vous cherchez la table de multiplication de quel nombre ?\n" ))
L1 = [n,n,n,n,n,n,n,n,n,n,]
for i in range(10):
    x = round(L1[i] * i, 1)
    print(n,"*",i,"=",x)