myTable=[4,10,3,15,9,0]
for i in range(1,len(myTable)):
    if(myTable[i-1]>myTable[i]):
        myTable[i-1],myTable[i]=myTable[i],myTable[i-1]
                                                   
print(myTable)
