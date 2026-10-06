'''数据科学与大数据技术导论第2章第二题'''
x=[1,3.5,2.7,6,4.8]
n=len(x)
for a in range(n-1):
    for b in range(0,n-a-1):
        if x[b]>x[b+1]:
            x[b],x[b+1]=x[b+1],x[b]
print("排序后的结果为：",x)
