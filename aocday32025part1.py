import csv


filename = 'aocday3input_sample.txt'
filename = 'aocday3input.txt'

def find2bignums(numval:str)->str:
    val1=int(numval[0])
    val2=0
    numval=numval.rstrip("\n")
    l1= len(numval)
    print(repr(numval))
    start=1
    while start < l1-1:
        ns = int(numval[start])
        if ns > val1:
            val1=ns
            val2=0
        elif val2 > 0 and ns > val2:
            val2=ns
        elif val2 ==0:
            val2=ns
        start+=1
    if start <l1 and int(numval[start]) > val2:
        val2 = int(numval[start])
    print(val1,val2)
    return (val1*10)+val2
            
with open(filename, 'r') as fr:
    contents = fr.readlines()
    sumval=0
    for cont in contents:
        if cont!="\n":
            sumval+= find2bignums(cont)

print(sumval)