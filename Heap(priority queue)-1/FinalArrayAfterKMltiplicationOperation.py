import heapq

def multiply_smallest_k_times(nums, k, multiplier):
    #step 1: Build the heap of (value, index) from nums
    heap = [(val, idx) for idx, val in enumerate(nums)]
    for _ in range(k):
        val, idx = heapq.heappop(heap) #Get the smallest  (value, index)
        nums[idx]*=multiplier
        heapq.heappush(heap, (nums[idx], idx))
    return nums

nums = [2, 1, 3, 5, 6]
k = 3
multiplier = 2
print(multiply_smallest_k_times(nums, k, multiplier))

