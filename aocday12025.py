import csv

filename = 'AOCDay12025_sample.txt'
filename = 'AOCDay12025.txt'

lc=0
rc=100
st=50
res=0
with open(filename, 'r') as fr:
    contents = fr.readlines()
    for cont in contents:
        if cont == "":
            continue
        print(cont,end="")
        dir=cont[0]
        num=int(cont[1:])
        while num > rc:
            num-=rc
        temp=0
        print(f"direction- {dir} , steps = {num}")
        if dir == 'L':
            if st - num == lc:
                st=0
                res+=1
            elif st - num < lc:
                temp = num-st
                st= rc-temp
            else:
                st-=num
        else:
            if st+num ==rc:
                st=0
                res+=1
            elif st + num > rc:
                st =(num +st) - rc
            else:
                st+=num
        print(f"Direction - {dir} start value - {st}")

print( res)