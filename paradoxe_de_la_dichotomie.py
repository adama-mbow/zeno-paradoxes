# la distance de lancé de pierre
distance_totale = 8
#position initiale de la pierre
position_pierre = 0
# la distance parcourue à chaque étape
position_pierre_par_etape = distance_totale/2

#definir le nombre d'étape de lancer
nombre_etape = 0

for i in range(int(input("mettez le nombre d'étape souhaité! "))):
      #reduire la distance de moitié à chaque étape parcourue
    position_pierre_par_etape /=2
    # avancer la pierre d'une distnce reduite
    position_pierre += position_pierre_par_etape    
    #incrementé le nombre d'etape de 1
    nombre_etape += 1 
    if position_pierre < distance_totale:
        print (f"étape {nombre_etape}: Position de la pierre = {position_pierre} unité par rapport à l'arbre")
    
    else:
    
        print(f"La pierrre a atteint l'arbre en {nombre_etape} étapes")
