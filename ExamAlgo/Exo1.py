myTable=[4,10,3,9,15]
premiereValeur=int(input("Indice de la première valeur à échanger ?"))
secondeValeur=int(input("Indice de la seconde valeur ?"))
myTable[premiereValeur], myTable[secondeValeur] = myTable[secondeValeur] ,myTable[premiereValeur]

print(myTable)