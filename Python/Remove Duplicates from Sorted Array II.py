#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/

def removeDuplicates(nums):
    i=1
    length=len(nums)
    while i in range(0,length-1):
        if nums[i]==nums[i-1] and nums[i]==nums[i+1] and i-1>=0: # check if element before and after are the same
            del nums[i] # if so delete the element
            i=i-1
            length=length-1
        else:
            i=i+1
    return nums

print(removeDuplicates( [1,1,1,2,2,3]))      #[1, 1, 2, 2, 3]
print(removeDuplicates( [0,0,1,1,1,1,2,3,3])) #[0, 0, 1, 1, 2, 3, 3]
print(removeDuplicates( [1,1,1,1])) #[1,1]
print(removeDuplicates( [1,1,1])) #[1,1]
