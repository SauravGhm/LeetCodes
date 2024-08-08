def subsets(nums):
    def backtrack(start, path):
        #Append the current subset (path) to the result:
        result.append(path[:]) #Use a copy of path to avoid aliasing issues
        #Try to include each element starting from 'start' index to the end of the nums array
        for i in range(start, len(nums)):
            #Include nums[i] in the current subset and proceed to the next element
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop() #Backtrack, remove nums[i]

        
    result = []
    backtrack(0, [])
    return result
    

#Example usage
nums = [1,2,3]
print(subsets(nums))

