'''数据科学与大数据技术导论第2章第三题'''
def new_sort(x):            #一个方法
    x = list(x)
    y = len(x)
    for a in range(y-1):
        for b in range(y-1-a):
            if x[b]>x[b+1]:
                x[b],x[b+1]=x[b+1],x[b]
    return x
print(new_sort([3,2,5,6.7,8.9,9,23]))
