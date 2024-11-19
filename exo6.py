def tri_par_selection(tab):
    n = len(tab)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        if min_index != i:
            tab[i], tab[min_index] = tab[min_index], tab[i]


        print(tab)


tab = [5, 2, 4, 8, 1, 3]
print("Évolution du tri :")
tri_par_selection(tab)