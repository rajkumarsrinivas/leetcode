from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    map = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in map:
            return [map.get(y), i]
        else:
            map[x]=i

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))