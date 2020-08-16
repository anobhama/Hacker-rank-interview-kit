"""
Consider an array of integers,arr=[arr[0],arr[1],...,arr[n-1]] . We define the absolute difference between two elements, a[i] and a[j] (where i !=j), to be the absolute value of a[i]-a[j].

Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array arr=[-2,2,4] we can create 3 pairs of numbers: [-2,2],[-2,4] and [2,4]. The absolute differences for these pairs are |(-2)-2|=4,|(-2)-4|=6  and |2-4|=2. The minimum absolute difference is 2.

Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

n: an integer that represents the length of arr
arr: an array of integers
Input Format

The first line contains a single integer n , the size of arr.
The second line contains n space-separated integers arr[i].


Output Format

Print the minimum absolute difference between any two elements in the array.

Sample Input 0

3
3 -7 0
Sample Output 0

3
"""
#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_dif = float("inf")
    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])
        if dif < min_dif:
            min_dif = dif
    return min_dif

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
