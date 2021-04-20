#
# https://leetcode.com/problems/container-with-most-water/
#

from typing import List

def maxArea(height: List[int]) -> int:
        max = len(height) - 1
        min = 0
        max_capacity=0
        while min != max:
            if height[min] < height[max]:   
                capacity = height[min] * (max - min)
                temp = min + 1
                while(height[temp] < height[min]):
                    temp += 1
                min = temp
            else:
                capacity = height[max] * (max -min)
                temp = max - 1
                while(height[temp] < height[max]):
                    temp -= 1
                max = temp
            if capacity > max_capacity:
                max_capacity = capacity

        return max_capacity

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))