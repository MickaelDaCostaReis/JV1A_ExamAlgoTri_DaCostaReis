myTable=[4,10,3,15,9,0]
echange_fait=True
while(echange_fait):
    echange_fait=False
    for i in range(1,len(myTable)):
        if(myTable[i-1]>myTable[i]):
            myTable[i-1],myTable[i]=myTable[i],myTable[i-1]
            echange_fait=True
                                                    
print(myTable)