example_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
other = []
# output  = [10,-65] 

def combine(x):
    if bool(x) == True:
        posNums = 0
        neg = 0
        answer = []
        for i in range(len(x)):
            if x[i] > 0:
                posNums += 1
            else:
                neg += x[i]

        answer.append(posNums)
        answer.append(neg)
        return(print(answer))
    else:
        answer = []
        return(print(answer))
            
combine(example_input)
combine(other)