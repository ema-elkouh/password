import hashlib
import json

boucle = True

while boucle==True:

    mdp = input ("Veuillez entrez un mot de passe : " )

#placer les conditions 

    if not len(mdp) > 8 :
        print ("Mot de passe trop court, 8 caractères min" )
   

    if sum(1 for x in mdp if x.isalpha()) :
        alpha_present = True
    else:
        print ("Il vous manque une miniscule ")
        
    if sum(1 for x in mdp if x.isupper()) :
        maj_presente = True
    else:
        print ("Il vous manque une majuscule ")
    
    if sum(1 for x in mdp if x.isdigit()) :
        digit_present = True
    else:
        print ("Il vous manque un chiffre ")

    if sum(1 for x in mdp if x.isdecimal()) :
        punctuation_present = True
    else:
        print ("Il vous manque un caractère spécial ") 



          #sécuriser le mot de passe avec Hashlibz

    if len(mdp) > 8 and alpha_present == True and maj_presente == True and digit_present == True and punctuation_present == True:
        y = hashlib.sha256 (mdp.encode('utf-8')).hexdigest()
        print ("Bravo ! Voici votre mot de passe crypté : ", y)
   
        break   



#test pour le "aller plus loin "

notes = {'input = False'}
# Enregistrer le dictionnaire dans un fichier :
with open('mdp.txt', 'w') as file:
    json.dump(mdp, file)
 
# Charger le dictionnaire depuis un fichier :
with open('mdp.txt', 'r') as file:
    mdp = json.load(file)


