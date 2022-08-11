l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
l_3 = []

print(type(l_1[1]))

def join(x, y):
    x = set(x)
    y = set(y)
    l_3 = x.union(y)
    print(sorted(l_3))
join(l_1, l_2)