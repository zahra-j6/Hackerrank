class Solution(object):
    def makeGood(self, s):
        array=[]
        array=list(s)
        i=0
        while i in range(0, len(array)-1):
            if array[i].isupper() and array[i].lower()==array[i+1] or array[i+1].isupper() and array[i+1].lower()==array[i]:  #checking condition mentioned
                del array[i]
                del array[i]
                if i!=0:
                    i=i-1
            else:
                i=i+1
        x=""
        for i in array:
            x=x+i
        return x
                    
   
        
