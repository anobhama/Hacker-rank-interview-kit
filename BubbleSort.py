"""
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps.,numSwaps where  is the number of swaps that took place.
First Element: firstElement, where firstElement,  is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.
Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

For example, given a worst-case but small array to sort: a= [6,4,1] we go through the following steps:

swap    a       
0       [6,4,1]
1       [4,6,1]
2       [4,1,6]
3       [1,4,6]
It took 3 swaps to sort the array. Output would be

Array is sorted in 3 swaps.  
First Element: 1  
Last Element: 6  
Function Description

Complete the function countSwaps in the editor below. It should print the three lines required, then return.

countSwaps has the following parameter(s):

a: an array of integers .
Input Format

The first line contains an integer ,n , the size of the array a.
The second line contains n space-separated integers a[i] .


Output Format

You must print the following three lines of output:

Array is sorted in numSwaps swaps., numSwaps where  is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.
Sample Input 0

3
1 2 3
Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    no_swap = 0
    for i  in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                (a[j], a[j + 1]) = (a[j + 1], a[j])
                no_swap += 1
    print('Array is sorted in ' + str(no_swap) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
