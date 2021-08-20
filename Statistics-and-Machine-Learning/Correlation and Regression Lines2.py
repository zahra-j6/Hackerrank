import statistics, numpy as np
from scipy.stats import pearsonr
p=[15  ,12  ,8   ,8   ,7   ,7   ,7   ,6   ,5   ,3]
h=[ 10  ,25 , 17,  11 , 13 , 17 , 20 , 13,  9,   15]
p_m=statistics.mean(p)
h_m = statistics.mean(h)
num=0
den=0
for i in range(0,10):
    num=num+((p[i]-p_m)*(h[i]-h_m))
    den=den+(p[i]-p_m)**2
print(num/den)