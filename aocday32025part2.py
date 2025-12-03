import csv


filename = 'aocday3input_sample.txt'
filename = 'aocday3input.txt'


def find2bignums(numval:str,start=0,end=0)->int:
    val1=int(numval[start])
    finalpos=start
    while start <= end:
        ns = int(numval[start])
        if ns > val1:
            val1=ns
            finalpos=start
        start+=1
    return finalpos
            
with open(filename, 'r') as fr:
    contents = fr.readlines()
    sumval=0
    
    for cont in contents:
        finalstr=""
        cont=cont.rstrip("\n")
        l1=len(cont)
        prevpos=currpos=0
        for i in range(12,0,-1):
            if l1 -i <= prevpos:
                finalstr+=cont[prevpos:]
                break
            currpos=find2bignums(cont,start=prevpos,end=l1-i)
            finalstr+=cont[currpos]
            prevpos=currpos+1
            currpos=0
        print(cont,finalstr)
        sumval+= int(finalstr)

print(sumval)

#987654321111111
#
#811111111111119
#234234234234278
#818181911112111