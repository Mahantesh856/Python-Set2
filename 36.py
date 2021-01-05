t1=(1,2,3,4,5)
t2=(11,12,13,14,15)
if cmp(t1,t2)==1:
    print "t1 is greater:",t1
elif cmp(t2,t1)==2:
    print "t2 is greater:",t2
else:
    print "equal"

print "len of t1:",len(t1)
print "len of t2:",len(t2)

print "max of t1:",max(t1)
print "max of t2:",max(t2)

print "max of t1:",min(t1)
print "max of t2:",min(t2)

l1=[10,40,50]
print "list",l1
print "convert list to tuple",tuple(l1)
