def play_game(nums):
    arr = []
    nums.sort()  # Sort to simulate minimum removal
    while nums:
        alice_pick = nums.pop(0)  # Alice removes min
        bob_pick = nums.pop(0)    # Bob removes next min

        arr.append(bob_pick)      # Bob appends first
        arr.append(alice_pick)    # Alice appends next
    return arr

nums = [5, 4, 2, 3]
print(play_game(nums))  # Output: [2, 1, 4, 3, 6, 5]
