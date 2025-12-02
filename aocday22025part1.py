import csv

filename = "aocday2input_sample.txt"
filename = "aocday2input.txt"
sumofval=0
ranges=[]
with open(filename , 'r') as fr:
    content = fr.readlines()
    for con in content:
        ranges=con.split(",")
print(ranges)
subrange=[]
invalidid=[]
for ran in ranges:
    subrange= ran.split("-")
    val1=int(subrange[0])
    val2=int(subrange[1])
    for val in range(val1, val2+1):
        sval = str(val)
        l1 = len(sval)//2
        if sval[0:l1] == sval[l1:]:
            invalidid.append(int(sval))

print(invalidid)
print(f"Sum of Invalid ids - {sum(invalidid)}")

