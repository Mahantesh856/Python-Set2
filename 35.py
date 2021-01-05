tup1=('mon','tue','wed','thur','fri','sat')
print tup1
tup2=('jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec')
print tup2

concat=tup1+tup2
print concat

t1=(1,2,3,4,5,6)
t2=(5,7,8,9)
t3=(1,2,3,4,5,6,7,8)
if(t1>t2 and t1>t3):
    print "t1 is greater:",t1
elif(t2>t1 and t2>t3):
    print "t2 is greater:",t2
else:
    print "t3 is greater:",t3
    
lst=list(tup1)
del lst[0:len(lst)]
tup1=tuple(lst)
del(tup1)
#print tup1

l1=list(t3)
l1.append(20)
print l1
