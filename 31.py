
a=[]
for i in range(5):
    n=input("enter numbers:")
    a.append(n)
print a.sort()
key=input("enter key:")
low=0
c=0
high=n-1
while low<=high:
    mid = (low+high)/2
    if (a[mid] == key):
        c=1
        break
    if(a[mid]>key):
        high=mid-1
    else:
        low=mid+1
if c==0:
    print "unsuccess"
else:
    print "successful",mid+1
          
