"""
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if prices= [1,2,3,4] and Mark has k=7 to spend, he can buy items [1,2,3] for 6, or[3,4]  for 7 units of currency. He would choose the first group of 3 items.

Function Description

Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.

maximumToys has the following parameter(s):

prices: an array of integers representing toy prices
k: an integer, Mark's budget
Input Format

The first line contains two integers, n and k , the number of priced toys and the amount Mark has to spend.
The next line contains n space-separated integers prices[i] 

A toy can't be bought multiple times.

Output Format

An integer that denotes the maximum number of toys Mark can buy for his son.

Sample Input

7 50
1 12 5 111 200 1000 10
Sample Output

4

"""
#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the maximumToys function below.
def maximumToys(prices, k):
    heapq.heapify(prices)
    no_item = 0
    spent = 0
    while (spent <= k):
        spent = spent + heapq.heappop(prices)
        if spent <= k:
            no_item += 1
    return no_item

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)