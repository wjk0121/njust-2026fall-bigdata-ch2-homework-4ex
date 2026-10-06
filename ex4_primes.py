'''数据科学与大数据技术导论第2章第四题'''
primes = []                     #定义一个空的列表，用来盛装素数
for num in range(2,101):        #因为1不是素数，且range左开右闭，因此到101结束
    isPrime = True
    for a in range(2,num):      #随机一个a用于试除
        if num % a == 0:
            isPrime = False     #排除非素数数字
            break
    if isPrime:
        primes.append(num)
print(primes)
