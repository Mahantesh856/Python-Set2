l1=[4,5,2,6]
l2=[1,12,10,3]
l3=[17,9,15,20]
l1.sort()
print l1
l2.sort()
print l2
l3.sort()
print l3
##
##a=l1[-2:]
##print a
##
##b=l2[-2:]
##print b
##
##c=l3[-2:]
##print c
##b.extend(c)
##a.extend(b)
##maxlist=a
##print maxlist
##
##sum=0
##for i in (maxlist):
##    sum=sum+i
##avg=sum/len(maxlist)
##print avg


a=l1[:2]
print a

b=l2[:2]
print b

c=l3[:2]
print c
b.extend(c)
a.extend(b)
minlist=a
print minlist

sum=0
for i in (minlist):
    sum=sum+i
avg=sum/len(minlist)
print avg
