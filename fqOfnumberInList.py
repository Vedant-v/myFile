dic = {}
print(type(dic))
def fqOfnumberInList(list):
    for i in list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

print(fqOfnumberInList([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))