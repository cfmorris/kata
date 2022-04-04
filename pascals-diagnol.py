# Author:cfmorris
# Source: Codewars 
# Title: Pascals Triangle.
# Challenge: Generate the (n)th diagnol of Pascal's triangle to the (l)th position.
# https://www.codewars.com/kata/576b072359b1161a7b000a17
# https://en.wikipedia.org/wiki/Pascal%27s_triangle


# This solution leverages the fact that the lth value of the nth diagnol can be 
# calculated by taking the sum all values [0:l] in the (n-1) diagnol.

def generate_diagonal(n, l):
    diagnol=[]
    for i in range(l):  #first loop builds a list of all 1s
        diagnol.append(1)
    if n==0:                
        return diagnol[0:l]  
    
    else:               #second loop iterates over previous loops.
        for item in range(n):
            nextdiag=[]
            for i in range(l+n):
                wkdiag = sum(diagnol[0:i])
                nextdiag.append(wkdiag)
            del nextdiag[0]
            diagnol=nextdiag    
    return nextdiag[0:l]


# Testing code below

print(generate_diagonal(0,10))
print(generate_diagonal(1,10))
print(generate_diagonal(7,10))
