dict1={'name':'ramakrishna','age':25}
dict2={'empid':1234,'salary':5000}
print dict1
print dict2
dict1.update(dict2)
print dict1

sal=(0.1)*dict1.get('salary')
s=dict1.get('salary')+sal
dict1.update({'salary':int(s)})

dict1.update({'age':26})
dict1.update({'grade':'B1'})
print dict1
print "keys:",dict1.keys()
print "values:",dict1.values()
dict1.pop('age')
print dict1
