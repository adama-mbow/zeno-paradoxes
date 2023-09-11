#la vitesse pour l'Achille et la tortue en unité

vitesse_achille = 10
vitesse_tortue = 5

# position initiale des coureurs
position_achille = 0
position_tortue =int(input("donner la position initiale de la Tortue! ")) # la tortue est position innitiale x unité par rapport à l'Archille

#le nombre d'étape de la cours par unité
nombre_etape = int(input("mettrer le nombre d'étape de la course! "))

# simulation de la course
for etape in range(nombre_etape):
        # faire avancer les coureurs
        position_achille += vitesse_achille
        position_tortue += vitesse_tortue
        
        #afficher la position actuelle des coureurs
        print(f"Etape{etape+1}: Achille est à la position {position_achille}, Tortue est à la position{position_tortue}")
        
# résultat de la course
if position_achille > position_tortue:
    print("Archille a gagné la course !")
elif position_tortue > position_achille:
    print("La Tortue a gagné la course !")
else:
    print("les deux coureurs sont en égalité")