#
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#


from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        tot_len = len1+len2
        i=0 
        j=0
        l=0
        med_array=[]
        if(len1 == 0 and len2 == 0):
            return 0.0

        if(len2 == 0):
            while(l <= int((tot_len/2))):
                med_array.append(nums1[l])
                l+=1
        if(len1 == 0):
            while(l <= int((tot_len/2))):
                med_array.append(nums2[l])
                l+=1

        while(l <= int((tot_len/2))):
            if((i < len1) and ((j >= len2) or (nums1[i] < nums2[j]))):
                med_array.append(nums1[i])
                i+=1
                l+=1
            else:
                med_array.append(nums2[j])
                j+=1
                l+=1
        result = 0.0
        print(med_array)
        print("tot_len ="+str(tot_len))
        result += med_array[-1]
        if( tot_len%2 == 0):
            result += med_array[-2]
            result /=2
        print("result ="+str(result))
        return result

if __name__ == "__main__":
    print(findMedianSortedArrays([1,2], [3,4]))
