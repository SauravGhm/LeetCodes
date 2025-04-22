import heapq

def deleteGreatestValue(grid):
    #First we sort every row so that the largest element is at the end of each row
    for row in grid:
        row.sort()

    m, n = len(grid), len(grid[0]) # 'm' becomes the row and 'n' becomes the column
    result = 0

    #Iterate over columns from rightmost(largest values in each row) to leftmost.
    for col in range(n-1, -1, -1):
        max_heap = []
        for row in range(m):
            val = grid[row][col]
            #push the negative value to simulate a max heap using python's min heap
            heapq.heappush(max_heap, -val)
            #pop the smallest negative value, which corresponds to the largest actual value
        result+= -heapq.heappop(max_heap)
        
    return result

if __name__ == "__main__":
    #Grid example
    grid = [
        [1,2,4],
        [3,3,1]
    ]
    result = deleteGreatestValue(grid)
    print("The greatest value addition is:", result)


    
