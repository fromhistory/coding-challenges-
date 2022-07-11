"""
556. Next Greater Element III
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1

"""




def nextGreaterElement(n: int) -> int:

    # convert a number to a list of integers 
    n = list(map(int, str(n)))
    
    # say, the num is 18976231
    # start from the smallest units and see if there is a descending order 
    # the logic is that you can't reverse 321 to a larger number anyway, so see if there is any number
    # in the sequence that is not in a descending order and mark its index. Start with one prior to the last element
    
    index = len(n) - 2

    # see if the number under under this index is larger then the one before, if so check the next one
    while index >= 0 and n[index] >= n[index + 1]:
        index -= 1
    
    # if your index is -1, it means you reached the limit and the whole number is in descending order
    if index == -1:
        return -1 

    # Good job finding the first index! In this case, it represents 2 in the end
    # Now find the number larger than it and swap them
    
    # set the second index from the end
    index2 = len(n) - 1
    
    while n[index] >= n[index2]:
        index2 -= 1 
   
    n[index], n[index2] = n[index2], n[index]
    
    # reverse all numbers after the one you swaped to achieve the smallest number
    n[index + 1:] = reversed(n[index+1:])
    
    # convert back to a number 
    res = ""
    for num in n:
        res += str(num)
    res = int(res)
    
    # make sure this number is less than the power to 31
    if res >= pow(2, 31):
        return -1 
    else:
        return res