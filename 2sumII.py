from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l , r = 0, len(numbers)-1
    while l < r :
        sum = numbers[l] + numbers[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l+1,r+1] 

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))