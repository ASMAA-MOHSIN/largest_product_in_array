#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def solution(inputArray):
    if len(inputArray) < 2:
        return None
    max_product = float('-inf')
    for i in range(len(inputArray)-1):
        c = inputArray[i] * inputArray[i+1]
        max_product = max(max_product , c)
    return max_product