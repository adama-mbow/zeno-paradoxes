# Distance totale que la flèche doit parcourir (en mètres)
distance_totale = 10

# Position initiale de la flèche (en mètres)
position_fleche = 0

# Vitesse de la flèche (en mètres par seconde)
vitesse_fleche = 2

# Intervalle de temps entre chaque mise à jour de la position (en secondes)
intervalle_temps = 1

# Temps total écoulé (en secondes)
temps_total = 0

# Simulation du vol de la flèche
while position_fleche < distance_totale:
    # Afficher la position de la flèche par rapport à la cible
    print(f"Temps écoulé : {temps_total} secondes, Position de la flèche : {position_fleche} mètres par rapport à la cible")

    # Mettre à jour la position de la flèche en fonction de sa vitesse et de l'intervalle de temps
    position_fleche += vitesse_fleche * intervalle_temps

    # Mettre à jour le temps total écoulé
    temps_total += intervalle_temps

# Résultat final
print(f"La flèche a atteint la cible en {temps_total} secondes.")
