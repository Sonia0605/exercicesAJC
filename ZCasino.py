import random
import math

# 1 joueur mise un numéro entre 0 et 49 et dépose une somme
#numero[50]
# la roulette est constituée de 50 cases entre 0 et 49
#case[50]
# numéro pair = noire, numéro impair = rouge

# numéro gagnant = somme*3
# numéro même couleur = somme*50%
# numéro différent et couleur différente = somme perdue

mise = 0
argent = 0

print(" ")
print("----------BIENVENUE AU CASINO----------")
print(" ")

mise = input("Saisissez votre mise : ")
mise = int(mise)
print("-----> Vous avez misé : ", mise, "$")
print(" ")

numero = input("Saisissez un numéro entre 0 et 49 : ")
numero = int(numero)
print("-----> Vous avez choisi le numero : ", numero)
print(" ")

roulette = random.randrange(50)
print("La roulette tourne et le numéro gagnant est : ", roulette)
print(" ")

if roulette == numero:
	argent += mise * 3
	print("-----> Vous avez gagné ", argent, "$ ! WINNER!!")
elif roulette != numero:
	if roulette%2 == numero%2:
		argent = mise * 0.5
		print("-----> Vous avez remporté ", argent, "$ !")
	else:
		argent = 0
		print("-----> Vous avez perdu! LOOSER!!")

print(" ")

