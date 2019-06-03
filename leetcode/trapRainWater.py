# Given n non-negative integers representing an elevation map where 
# the width of each bar is 1, 
# compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution():
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        leftMax = 0
        rightMax = 0

        left = 0
        right = len(height) - 1

        ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax: leftMax = height[left] 
                else: ans += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax: rightMax = height[right] 
                else: ans += rightMax - height[right]
                
                right -= 1
        
        return ans

T = Solution()

i = [0,1,0,2,1,0,1,3,2,1,2,1]

print(T.trap(i))