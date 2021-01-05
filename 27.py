s1=raw_input("enter string:")
s2=s1[: : -1]
print s2
if s1 == s2:
    print "palindrome"
else:
    print "not a palindrome"
