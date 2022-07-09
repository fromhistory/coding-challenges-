
"""
PROBLEM: 1

You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method
to insert Minto N such that M starts at bit j and ends at bit i. You can assume that the bits j through
i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5
bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
fit between bit 3 and bit 2

"""

def updateBits(m, n, j, i):
    
    # 1. create a mask that would look like 1110000111

    # push 1 to i-th position and deduct 1 to make a trail of 1111111s after 0
    right = (1 << i) - 1 

    # push 1 to j-th position, same trail of 111s and then swap it to 0

    left = ~((1 << j) - 1) 

    # combine two parts by ORing them 

    mask = left | right 

    # 2. Apply a mask to n and zero out all bits between j and i

    n_cleared = n & mask 

    # 3. line up m into positions starting from the lowest i 

    m_shifted = m << i

    # Apply m to the cleared-out n 

    return n_cleared | m_shifted


m = 19
n = 1024
i = 2
j = 6 
    
print(updateBits(m, n, j, i))

"""
PROBLEM 2:

Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at
most 32 characters, print"ERROR:'
"""


#Example: 0.5 * 2 = 1, so "." + "1" == "0.1"
# 0.25 * 2 != 1,  "." + "0" == "0.0", then 0.5 * 2 = 1, so ".0" + "1" == "0.01"

def toBinary(num):

    # check if the number is between 0 and 1 
    if num >= 1 or num <= 0:
        return "Error"

    # create a string for binary
    string = "."

    # set to 0, so if it drops below zero we can stop the loop
    while num > 0: 

        # if gets too long, return error
        if len(string) >= 32:
            return "Error"

        # doublt it b/c 0.1 in binary is same as  1 * 1/2
    
        double_num = num * 2
        
        # if more than 1, then add "1" after coma and deduct 1 (in case the result is 0, can end the loop)
        if double_num >= 1:
            string += "1"
            num = double_num - 1

        # else add one and move further 
        else:

            string += "0"
            num = double_num

    return string
        
num = 0.5     
toBinary(num)