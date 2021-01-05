import base64
s1="hi"
val='base64'
s2=s1.encode(val)
print "hello",s2
print "decoded message"
s3=s2.decode(val)
print s3
