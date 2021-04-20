from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i,val in enumerate(nums[:-2]):
        if i == 0 or val != nums[i-1] :
            l , r = i+1, len(nums)-1
            while l < r :
                sum = val + nums[l]+nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    result.append([val,nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
    return result

if __name__ == "__main__":
    #print(threeSum([-2,-7,-11,-8,9,-7,-8,-15,10,4,3,9,8,11,1,12,-6,-14,-2,-1,-7,-13,-11,-15,11,-2,7,-4,12,7,-3,-5,7,-7,3,2,1,10,2,-12,-1,12,12,-8,9,-9,11,10,14,-6,-6,-8,-3,-2,14,-15,3,-2,-4,1,-9,8,11,5,-14,-1,14,-6,-14,2,-2,-8,-9,-13,0,7,-7,-4,2,-8,-2,11,-9,2,-13,-10,2,5,4,13,13,2,-1,10,14,-8,-14,14,2,10]))
    print(threeSum([0,0,0]))