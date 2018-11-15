import math
import numpy.random as nprand

def get_rand_list(alist, th=.5):
    """
    Breaks down the input list into two lists by randomly moving elements

    Input: threshold is used

    example: [list1, list2] = get_rand_list([1,2,3,4,5,6,7,8,9], 0.2);\\
    list1 = 0.8, list2 = 0.2
    """
    nlist = []
    counter = math.ceil( len(alist)*th )
    
    while(counter):
        num = nprand.randint(0,len(alist))
        assert num < len(alist)
        nlist.append( alist[num] )
        alist.pop(num)
        # del alist[num]
        counter = counter - 1
    
    return [alist, nlist]

