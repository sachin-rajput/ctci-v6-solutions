# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Create a hashtable to keep 
    # track of sums calculated. We
    # will save the difference for each value as key 
    # in the hash table
    sumsHash = {}
    
    # Loop over each value in input
    for i, value in enumerate(nums):
        # check if the difference exist as a key
        # in hash table. If yes means we found our two sum as
        # we only have one solution in the input
        if target - value in sumsHash:
            return [sumsHash[target-value], i]
        else:
            sumsHash[value] = i
        

nums = [2,7,11,15]  
target = 9
print(twoSum(nums, target))

points = [[1,3],[-2,2]]

points.sort(key = lambda point: point[0]**2 + point[1]**2)

print(points[:1])

x = 3
x = x ** 2
print(x)