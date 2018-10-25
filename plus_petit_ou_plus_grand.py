#Importation de la librairie contenant plusieurs fonctions aléatoires
import random 
# on initialise nos différentes variables
entree =-1
reponse = random.randrange(100) # on utilise la fonction randrange qui permet de choisir un nombre entre 0 et le nombre entre (), ici 100
compteur = 10 
# Tant que entree est différente de reponse et que compteur est plus grand que 0 ...
while entree != reponse and compteur > 0 :
  # On change la valeur de entree avec celle tapée au clavier. Attention, convertion en int
  entree =int( input("entre un nombre entre 0 et 100") )
  
  if entree < reponse :
    print("la reponse est plus grande")
  elif entree > reponse :
        print("la réponse est plus petite")
  else : 
    print("bravoo")   
    #Attention a changer la valeur du compteur pour eviter une boucle infinie  

  compteur = compteur -1  
