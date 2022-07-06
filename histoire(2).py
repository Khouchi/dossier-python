# Écrire une fonction qui reçoit 3 informations en entrée : un nom, un nombre de points de vie et un nombre de points de magie. Cette fonction devra afficher un message qui contient ces informations.
# Par exemple :
# afficher_info('Wolverine',100,0) devra afficher :
# Le personnage Wolverine a 100 points de vie et 0 point de magie
# def personnage(name, life, magic):
#     print('Nom :',name,'HP :',life ,'et à', magic, 'de magie')
def empty_rectangle(largeur, hauteur, c1, c2):
    s = ""
    s += full_line(largeur, c1)

    for n in range(hauteur-2):
        s+="\n" 
        s += empty_line(largeur, c1, c2)
    s+="\n" 

    if hauteur > 1 : 
        s += full_line(largeur, c1) 
    return s
# # Le premier personnage s'appelle Bob.
# name1 = 'Bob'
# # Il a 100 points de vie (hp)
# hp1 = 100
# # et 50 points de magie (mana).
# mana1 = 50
# # Quand il attaque, il fait perdre 12 points de vie.
# atk1 = 12

# print('Premier personnage')
# print('Nom :',name1,'HP : ',hp1)

# # Le deuxième personnage s'appelle Patrick.
# name2 = 'Patrick'
# # Il a 60 points de vie
# hp2 = 60
# # et 60 points de magie.
# mana2 = 60
# # Quand il attaque, il fait perdre 20 points de vie.
# atk2 = 20

# print('Deuxième personnage')
# print('Nom :',name2,'HP : ',hp2)

# # Bob attaque Patrick.
# # Comment vont évoluer les points de vie de Patrick ?
# print(name1,'attaque',name2,'.')
# hp2 = hp2 - atk1
# print(name2,'a',hp2,'points de vie.')

# # Patrick attaque Bob.
# print(name2,'attaque',name1,'.')
# hp1 = hp1 - atk2
# print(name1,'a',hp1,'points de vie.')

# # Bob lance un sort qui :
# # - lui coûte 5 mana
# mana1 = mana1-5
# # - fait perdre 8 points de vie à Patrick
# hp2 = hp2-8
# print(name1,'lance un sort. Il lui reste',mana1,'points de magie.')
# print(name2,"n'a plus que",hp2,'points de vie.')

# # Patrick lance un sort qui :
# # - lui coûte 40 mana
# mana2 = mana2-40
# # - lui fait perdre la moitié de sa vie
# hp2 = hp2 - hp2//2
# # - fait perdre 50 points de vie à Bob
# hp1 = hp1-50

# print(name2,'lance un sort. Il lui reste',hp2,'points de vie, et',mana2,'points de magie.')
# print(name1,"n'a plus que",hp1,'points de vie.')

# # Bob attaque Patrick
# print(name1,'attaque',name2,'.')
# hp2 = hp2 - atk1
# print(name2,'a',hp2,'points de vie.')

# # Patrick médite et récupère 20 points de mana.
# mana2 = mana2+20
# print(name2,'médite, il a maintenant',mana2,'points de magie.')

# # Bob boit un jus d'ananas : il récupère 20 points de vie.
# hp1 = hp1+20
# print(name1,"boit un jus d'ananas, il a maintenant",hp1,'points de vie.')

# # Patrick lance un sort qui :
# # - lui coûte 15 points de mana
# mana2 = mana2-15
# # - échange les points de vie des deux personnages
# hp1_save = hp1
# hp1 = hp2
# hp2 = hp1_save
# # hp1,hp2 = hp2,hp1
# print(name1,'a',hp1,'points de vie.')
# print(name2,'a',hp2,'points de vie.')

# # Bob lance un sort qui :
# # - lui coûte 30 mana
# mana1 = mana1-30
# # - équilibre les points de vie entre les deux personnages
# hp_mid = (hp1+hp2)//2
# hp1 = hp_mid
# hp2 = hp_mid
# print(name1,'lance un sort. Il lui reste',mana1,'points de magie.')
# print(name1,"a",hp1,'points de vie.')
# print(name2,"a",hp2,'points de vie.')

# mana2 = 10000 # Cheat code ?

# # Patrick essaye de lancer un sort qui :
# if mana2>=2000:
# 	# - lui coûte 2000 mana
# 	mana2 = mana2-2000
# 	# - qui enlève 200 points de vie à Bob
# 	hp1 = hp1-200
# 	print(name2,'lance un sort. Il lui reste',hp2,'points de vie, et',mana2,'points de magie.')
# 	print(name1,"n'a plus que",hp1,'points de vie.')
# else:
# 	print(name2,"n'a pas réussi à lancer son sort !")
	
# if hp1 > 0:
# 	print(name1,'a survécu au combat !')
# else:
# 	hp1 = 0
# 	print(name1,"n'a plus de point de vie (",hp1,").")