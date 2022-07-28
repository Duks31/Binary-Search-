import random 
import time

# Implementation of Binary Search ALgorithm 

# Prove thaat binary search algorithm is faster than naive search

# Naive Search: Scan the entire list and retrun the index of the target, if no then return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i 
    return -1

# Binary Search uses te divide and conquer 
# List has to be sorted in Binary Search 

def binary_search(l, target, low= None, high = None):
    if low is None:
        low = 0 
    if high is None:
        high = len(l) - 1 

    if high < low:
        return -1 
    # example = [1,3,5,10,12] should return 3
    midpoint = (low + high) // 2 

    if l[midpoint] == target:
         return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1 )
    else:
        return binary_search(l, target, midpoint + 1, high )
    
if __name__ ==  '__main__':
    l = [1,3,5,10,12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

    length = 10000
    # Build a sorted list of lenght 10000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-5*length, 5*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()
    # print(f'Naive Search Started : {start} and ended {end} ')
    print('Naive search time: ', (end - start)/length, 'seconds')

    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    # print(f'Binary Search Started : {start} and ended {end} ')
    print('Binary search time: ', (end - start)/length, 'seconds') 

    