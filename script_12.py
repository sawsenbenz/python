def PairImpair(liste):
	listePairs = []
	listeImpairs = []
	for i in liste:
		if ( i%2 == 0):
			listePairs.append(i)
		else:
			listeImpairs.append(i)
	
	print(" la liste de nombre pairs est : ", listePairs)
	print(" la liste de nombre impairs est : ", listeImpairs)		



liste = ['0','1','2','3','4','5','6','7','8','9']

PairImpair(liste)