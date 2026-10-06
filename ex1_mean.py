'''数据科学与大数据技术导论第2章第一题'''
x=[1,3.5,2.7,6,4.8]
inNumber=0                     #使其初始数值为0
for num in x:
    inNumber += num            #循环累加求和
mean_x=inNumber/len(x)         #除以元素个数
print("向量x的平均数为:",mean_x)   #输出答案
