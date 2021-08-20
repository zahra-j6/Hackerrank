#https://leetcode.com/problems/k-diff-pairs-in-an-array/submissions/
def findPairs(nums, k):
    list=[]
    for i in nums:
        if(i>0):
    #        print(abs(k-i),i)
            if abs(k+i) in nums and [abs(k+i),i] not in list and [i,abs(k+i)] not in list: # check if the value is present in original list and not new list
                #print(list.count(i))
                if abs(k+i)!=i:
                    list.append([abs(k+i),i])
                else:
                    if(nums.count(i) >1): # if abs(k-i)==i ensure that they are duplicate values
                        list.append([abs(k+i),i])
        else:
            if (k+i) in nums and [(k+i),i] not in list and [i,(k+i)] not in list:
                #print(list.count(i))
                if (k+i)!=i:
                    list.append([(k+i),i])
                else:
                    if(nums.count(i) >1):
                        list.append([(k+i),i])            
    return len(list)


print(findPairs([3,1,4,1,5], 2))#2
print(findPairs([3,1,4,1,5], 0))#1
print(findPairs([-1,-2,-3], 1))#2

