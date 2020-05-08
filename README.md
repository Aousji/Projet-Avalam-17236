# AIGameRunner

## Stratégie utilisé:

tout d'abord je cherche la position de mes pions, les pions de l'adversaire  et je les places dans des listes. 

Il existe 8 liste : - 4 pour mes pions 
					- 4 pour les pions de l'adversaire 

Les 4 listes sont organisé en fonction du nombre de pion superposé 

et aprés je fais une petite recherche dans les liste et je mets des condtion concernant les postions pour avoir juste les positions atuour du pion recherché ( les 8 déplacements possibles ).

Par exemple  il existe un niveau 4 est le pion dans le top n'est pas le mien, la je cherche premiérement dans la liste des nivveaux 1 de mes pions qui sont autour et je trouve pas je passe et cherche un niveau 3 et si je ne trouve aucun pion autour je passe jusqu'au trouver le move le moins risqué .

 



