# zeno-paradoxes

## problematique
Ce projet vise à simuler lancer d'une pierre vers un arbre,la course entre le sprinte et la tortue et le vol d'une flèche en prenant en compte les positions à chaque instant. Nous abordons le célèbre paradoxe de Zénon d'Élée, qui remet en question la notion de mouvement en divisant le temps en une série d'instants infiniment petits.

## Contexte

ces paradoxe sont des paradoxes classiques de la philosophie antique, formulé par Zénon d'Élée. Il soulève des questions sur la nature du temps, du mouvement et de la continuité.

Les contextes du projet consiste à résoudre ce paradoxe

1- ce projet consiste à résoudre le paradoxe d'Achille et de la Tortue en créant une simulation réaliste de leur course. Il s'agit de modéliser le mouvement d'Achille et de la Tortue en prenant en compte leurs vitesses respectives, les positions initiales, et la longueur de la course. Nous devons également afficher les positions à chaque étape de la simulation.

2- Zénon soutenait que pour qu'une pierre atteigne un arbre, elle doit d'abord parcourir la moitié de la distance, puis la moitié de la distance restante, puis la moitié de la distance restante après cela, et ainsi de suite, créant une série infinie de divisions. Étant donné que chaque étape prend du temps, il semblait impossible pour la pierre d'atteindre l'arbre, car il y aurait une infinité d'étapes à franchir.
3- en simulant le vol de la flèche et en démontrant que la flèche peut effectivement atteindre sa cible malgré les paradoxes apparents.

## Solutions

Nous avons développé des solutions pour aborder ces problème :

1- Les principales composantes de notre solution sont les suivantes :
Vitesses d'Achille et de la Tortue: Nous avons défini les vitesses respectives d'Achille et de la Tortue, qui sont les paramètres clés de la simulation.

Positions initiales: Nous avons initialisé les positions d'Achille et de la Tortue au début de la course, en donnant à la Tortue une longueur d'avance.
Longueur de la course: Nous avons à l'utilisateur de de donner le nombre d'étape pour la course, c'est-à-dire la distance que les deux doivent parcourir.
Boucle de simulation: Nous avons utilisé une boucle for pour simuler la course. À chaque itération de la boucle, nous avons fait avancer Achille et la Tortue en fonction de leurs vitesses respectives.
Affichage des positions: Nous avons affiché les positions d'Achille et de la Tortue à chaque étape de la course.
Vérification de dépassement: Nous avons vérifié si Achille avait dépassé la Tortue à chaque étape de la simulation.

2- Vitesse d'Achille
Vitesse de la Tortue
Position initiale d'Achille
Position initiale de la Tortue
Longueur de la course
Le programme utilise une boucle while pour faire avancer Achille et la Tortue à chaque itération, en mettant à jour leurs positions. Il affiche ensuite ces positions à chaque étape de la course et vérifie si Achille a dépassé la Tortue.

3- Une simulation simple qui calcule la position de la flèche à chaque instant en fonction de sa vitesse et affiche les résultats dans la console.

## Résultats

1- Les résultats des simulations varient en fonction des paramètres que l'utilisateur a choisi, notamment les vitesses d'Achille et de la Tortue ainsi que la longueur de la course.cela vous a permis avec différentes de voir comment les positions évoluent au fil du temps. 

2-Les résultats des simulations dépendent des paramètres que vous choisissez, en particulier des vitesses d'Achille et de la Tortue ainsi que de la longueur de la course. Vous pouvez expérimenter avec différentes valeurs pour voir comment les positions évoluent au fil du temps.

3-La simulation textuelle démontre que la flèche atteint sa cible en suivant le paradoxe de Zénon. Chaque étape de la simulation affiche la position de la flèche par rapport à la cible, montrant comment la flèche se rapproche progressivement de sa destination malgré la division infinie de la distance.




