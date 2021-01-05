import time
start=time.time()
time.clock()
val=0
while val<60:
    print time.asctime(time.localtime(time.time()))
    time.sleep(5)
    val=(time.time())-start
    

strt=time.time()
l1=["Mysore","bangaloree","Rajastan","goa","manali"]
l2=["mumbai","pune","pondi","kerala","tamilnadu"]
l3=["abcde","efghitt","muigtf","ghhhjhj","llllllll"]
for i in l1:
    print i,len(i)

for i in l2:
    print i,len(i)

for i in l3:
    print i,len(i)

end=time.time()
print "cpu time:",end-strt
