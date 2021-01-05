l1=["Mysore","bangaloree","Rajastan","goa","manali"]
l2=["mumbai","pune","pondi","kerala","tamilnadu"]
l3=["abcde","efghitt","muigtf","ghhhjhj","llllllll"]
for i in l1:
    print i,len(i)

for i in l2:
    print i,len(i)

for i in l3:
    print i,len(i)


res1=(max(l1,key=len))
res2=(min(l1,key=len))
print res1,len(res1)
print res2,len(res2)


res3=(max(l2,key=len))
res4=(min(l2,key=len))
print res3,len(res3)
print res4,len(res4)

res5=(max(l3,key=len))
res6=(min(l3,key=len))
print res5,len(res5)
print res6,len(res6)

if(len(res1)>len(res3) and len(res1)>len(res5)):
    print "biggest",res1,len(res1)
elif(len(res3)>len(res1) and len(res3)>len(res5)):
    print "biggest",res3,len(res3)
else:
    print "biggest",res5,len(res5)


if(len(res2)<len(res4) and len(res2)<len(res6)):
    print "smallest",res2,len(res2)
elif(len(res4)<len(res2) and len(res4)<len(res6)):
    print "smallest",res4,len(res4)
else:
    print "smallest",res6,len(res6)


del l1[0]
del l1[-1]
print l1

del l2[0]
del l2[-1]
print l2

del l3[0]
del l3[-1]
print l3
