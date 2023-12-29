#python program to find the maximum sum such that no three are consequetive
#returns maximum subsequence sum such that no three elements are consequetive
def maxSumOfThreeConsNum(arr, n):
    #stores result for sub array arr[0...i], i.e. maximum possible sum in subarray of arr[0...i]
    #such that no three elements are consecutive
    sum = [0 for k in range(n)]
    