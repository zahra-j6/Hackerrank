#https://www.hackerrank.com/challenges/stat-warmup/problem

import math
import operator
from statistics import stdev

n=int(input()) #number of integers
list=input().split()

#converting str to int
list=[int(i) for  i in list]

#finding and printing mean
mean=0
for i in list:
    mean=mean+int(i)
print('{:.1f}'.format(mean/n))


# finding and printing median
med=0
median=sorted(list)
if n%2==0:
    v1 = median[n // 2]
    v2 = median[(n // 2) - 1]
    med = (v1 + v2) / 2
    print('{:.1f}'.format(med))
else: # if number of elements are odd
    print('{:.1f}'.format(median[(n//2)+1]))


#finding mode
dict={}
for i in list:
    if i not in dict:
        dict[i]=1
    else:
        val=dict[i]
        dict[i]=val+1
# sort on the basis of keys
dict=sorted(dict.items(), key=operator.itemgetter(0))
mode,m=0,0
for key,value in dict:
    if mode>=value:
        continue
    else:
        mode=value
        m=key
print(m)

#std deviation
std=0
mean=mean/n
for i in range(0,n):
     std=std+(list[i]-mean)**2
s=math.sqrt(std/(n))
print('{:.1f}'.format(s))

#Lower and Upper Boundary of the 95% Confidence Interval for the mean
lower=mean-(1.96*(s/math.sqrt(n)))
higher=mean+(1.96*(s/math.sqrt(n)))
print('{:.1f} {:.1f}'.format(lower,higher))
