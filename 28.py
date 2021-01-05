word=raw_input("enter word:")
c={i:0 for i in 'aeiouAEIOU'}
for char in word:
    if char in c:
        c[char] +=1
for k,v in c.items():
    print(k,v)
    
    


    
