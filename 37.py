d1={'a':1,'b':2,'c':3}
d2={'ab':1,'bc':2,'cd':3}
d3={'ad':1,'bd':2,'cd':3}
if cmp(d1,d2)==1:
    print "d1 is greatest :",d1
elif cmp(d2,d1)==1:
    print "d2 is greatest :",d2
else:
    print "equal"


d1.update({'m':10})
d2.update({'n':20})
print "updated d1:",d1
print "updated d2",d2

print "length of d1:",len(d1)
print "length of d2:",len(d2)
print "length of d3:",len(d3)

s1=str(d1)+str(d2)+str(d3)
print s1
print type(s1)
