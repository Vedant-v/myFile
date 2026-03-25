def isPalemdrom(a):
    n = a
    d  = 0 
    while n > 0:
        temp = n % 10;
        d = d * 10 + temp
        n = n // 10        
    if d != a:
        return False
    else:
        return True

n = int(input())
c = 0
k = 10

while c < n:
    if isPalemdrom(k):
        print(k)
        c += 1

    k = k +1
