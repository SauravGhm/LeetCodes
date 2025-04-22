import heapq

def play_game(nums):
    arr = []
    heapq.heapify(nums)

    while nums:
        alice_pick = heapq.heappop(nums)
        bob_pick = heapq.heappop(nums)

        arr.append(bob_pick)
        arr.append(alice_pick)
    return arr

nums = [5, 3, 1, 4, 2, 6]
print(play_game(nums))  # Output: [2, 1, 4, 3, 6, 5]
