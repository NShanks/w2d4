example = [19, 5, 42, 2, 77]
#output = 7


def addLow(x):
    small1 = min(x)
    x.pop(small1)
    small2 = x[-1]
    for i in range(len(x)):
        if small2 > x[i] and x[i] != small1:
            small2 = x[i]
    return(print(small1 + small2))
addLow(example)