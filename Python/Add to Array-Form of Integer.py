#https://leetcode.com/problems/add-to-array-form-of-integer/submissions/

def addToArrayForm(A, K):
    i=""
    for s in A:
        i=i+str(s) #converting to a single word
    val=K+int(i)   # finding the sum and storing it as int
    return list(str(val)) # returning str of list

print(addToArrayForm( [1,2,0,0], 34))        
