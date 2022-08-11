# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]
l_2 = []

def less(nums):
    for i in range(len(nums)):
        if nums[i]<10:
            l_2.append(nums[i])
    print(l_2)
            
less(l_1)