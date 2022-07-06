# 1) Créer une liste l1 de 6 cases, qui contient les nombres 144, 202, 216, 216, 222 et 64.
l1 = [144,202,216,216,222,64]
print(l1)
# 2) Ajouter le nombre 0 à la fin de la liste l1.
l1.append(0)
print(l1)
# 3) Afficher *un par un* tous les éléments de la liste l1.
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[5])
print(l1[6])
# 4) Retirer le dernier élément de la liste l1.
l1.pop()
print(l1)

# 5) Créer une liste l2 qui contient les nombres 238, 222, 228, 216, 200.
l2=[238, 222, 228, 216, 200]
print(l2)
# 6) Ajouter le nombre 58 à la fin de l2.
l2.append(58)
print(l2)
# 7) Ajouter *un par un* tous les éléments de la liste l2 à la fin de la liste l1.
l1.append(238)
l1.append(222)
l1.append(228)
l1.append(216)
l1.append(200)
print(l1)

# 8) Afficher *un par un* tous les éléments de la liste l1.
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[5])
print(l1[6])
print(l1[7])
print(l1[8])
print(l1[9])
print(l1[10])


# 9) Retirer et stocker dans la variable ma_variable le dernier élément de la liste l1.
ma_variable=l1.pop()
print(l1)

# 10) Afficher la taille de la liste l1.
len(l1)
# 11) Ajouter le nombre 66 à la fin de la liste l1.
l1.append(66)
print(l1)

# 12) Diviser par 2 toutes les variables contenues dans la liste l1.
l1[0,1,2,3,4,5,6,7,8,9,10]=72,101,108,108,111,32,

# 13) Tester le code suivant pour vérifier si vous avez le bon résultat à la fin (le but n'est pas de chercher à comprendre ce code) :
# from functools import reduce
# print(reduce(lambda x,y:x+chr(int(y)),l1,""))
# print(chr(ma_variable)+chr(ma_variable-17))