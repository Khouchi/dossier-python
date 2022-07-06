 Écrire une fonction f7 qui prend deux nombres en entrée et qui retourne le plus grand des deux.
# def f7(a,b):
#     if a> b:
#         return(a)
#     else:
#         return(b)

# f7(7,10)

# Écrire une fonction f8 qui prend trois nombres en entrée et qui retourne le plus grand des trois.

# def f8(a,b,c):
#     if a>b and a>c :
#         return(a)
#     elif b>a and b>c :
#         return(b)
#     else:
#         return(c)

# print(f8(2,5,15))

# (Au moins deux versions possibles : sans utiliser f7, et en utilisant f7).



# Écrire une fonction f9 qui prend un nombre et un mot en entrée, et qui affiche dans la console ce mot ce nombre de fois.

def f9(a,b):
    for _ in range(a):
        print(b)
    
f9(3, "aymen")

Envoyer un message à @aym