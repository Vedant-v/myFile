n = [[12,6,7],[9,4,3],[2,7,9],[5,8,9]]
sumn = 0
for i in n:
    for j in range(len(i)):
        sumn += i[j]

print(sumn)
