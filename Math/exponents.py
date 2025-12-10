# Given a list: [2, 4, 6, 8], create a list where each number is raised to the power of its index.

new_ls = []


def givenLsExp(ls):
    for i,val in enumerate(ls):
        print(val ** i)
        new_ls.append(val ** i)
    return 1

# givenLsExp([2,3,4,5])



# Without using ** or pow(), implement your own exponent function using loops.

# I will do the same like above but without using pow() or **

# multiply each number by itself until the index



def givenMyExp(ls):
    for i, val in enumerate(ls):
        result = 1 
        for k in range(i):
            result = result * val
        print(result)
    return result 


givenMyExp([1,2,3,4])