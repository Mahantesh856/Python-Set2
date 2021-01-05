lst=[]
num=int(input("enter number:"))
for n in range(num):
    number=int(input("enter values:"))
    lst.append(number)
new=[]
while lst:
    low=lst[0]
    for x in lst:
        if x<low:
            low=x
    new.append(low)
    lst.remove(low)
print new
