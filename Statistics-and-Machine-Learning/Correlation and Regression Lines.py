import statistics, math
s=[15  ,12  ,8   ,8   ,7   ,7   ,7  , 6   ,5   ,3]
t=[10 , 25,  17,  11,  13,  17,  20,  13,  9,   15]
s_m=statistics.mean(s)
t_m=statistics.mean(t)
num=0
den1=0
den2=0
for i in range(0,10):
    num=num+(s[i]-s_m) * (t[i]-t_m)
    den1=den1+(s[i]-s_m)**2
    den2=den2+(t[i]-t_m)**2

den=math.sqrt(den1) * math.sqrt(den2)
print(num/den)
