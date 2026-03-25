n = [1,2,0,3,4]

#n[i] = n[i] + n[n[i]] * len(n)
# output = [2,0,1,4,3]

l = len(n)

for i in range(l):
    temp = n[n[i]] % l
    n[i] = (n[i] + (temp * l)) 

for i in range(l):
    n[i] //= l




print(n)
    
        
