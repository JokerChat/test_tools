# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/12/9 14:24
# @FileName     :test.py
#IDE            :PyCharm
arr=[]
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a + b + c ==15 and len({a,b,c})==3:
                arr.append([a,b,c])
for a1 in arr:
    for a2 in arr:
        for a3 in arr:
            if len(set(a1+a2+a3))==9:
                sum1=a1[0]+a2[0]+a3[0]
                sum2=a1[1]+a2[1]+a3[1]
                sum3=a1[2]+a2[2]+a3[2]
                sum4=a1[0]+a2[1]+a3[2]
                sum5=a1[2]+a2[1]+a3[0]
                if sum1==sum2==sum3==sum4==sum5:
                    print(a1)
                    print(a2)
                    print(a3)
                    print('---------')