# S = 11
# m = input()
# if 20<m<=100:
#     while S <= m:
#         S++
#     sum = S
# else
#     print("请输入大于20小于等于100的数")
# print("sum = ")



# m = input()
# while (range(11,m)):
#     s = 
#     sum += s
    

# while True:
#     dec = int(input('请输入一个整数(输入Q结束程序):'))
#     if dec == ['q','Q']:
#         break
#     elif not float(dec)>0:
#         print('请输入一个整数(输入Q结束程序):')
#     else:
#         print('十进制 -> 十六进制：%d -> '% dec,hex(dec))


# q = True        #变量q复制为真

# while q:        #循环为真

#   num = input('请输入一个整数(输入Q结束程序)：')    #输入一个数

#   if num != 'Q':    #如果输入的数，不等于Q，那么将执行下面的语句，如果输入的是Q，则执行else里的，q为假，终止循环

#     num = int(num)  #先将输入的语句转化为整数，int

#     print('十进制 -> 十六进制 : %d -> 0x%x' % (num, num))   #输出，%d 为整数格式化类型，%x为格式化十六进制数，双引号后面不用加逗号什么的，加 % 后面加一个括号

#     print('十进制 -> 八进制 : %d -> 0o%o' % (num, num))     #输

#     print('十进制 -> 二进制 : %d -> ' % num, bin(num))      #二进制没有字符串格式化的符号，bin是转化为二进制

#   else:

#     q = False   



# nmae = input('请输入待查找的用户名：')
# score = [['迷途',85],['黑夜',80],['小不丁',65],['福禄娃娃',95],['意境',90]]
# IsFind = False
# for each in score:
#     name in each
#     print(name + '的得分是：',score[score.find(name)][1])
#     IsFind = True
#     break

# # is IsFind:
# #     print('查找的数据不存在')


# name = input('请输入待查找的用户名：')
# score = [['迷途', 85], ['黑夜', 80], ['小布丁', 65], ['福禄娃娃', 95], ['怡静', 90]]
# IsFind = False

# for each in score:
#     if name in each:
#         print(name + '的得分是：', each[1])
#         IsFind = True
#         break
    
# if IsFind == False:
#     print('查找的数据不存在！')
# def gcd(x,y):
#     if y == 0:
#         print(x)
#     else:
#         gcd(y,x%y)
# gcd(16,12)

# def gic(x,y):
#     x = int(x)
#     y = int(y)
#     c = x%y
#     if c != 0:
#         c = x%y
#         x = y
#         y=c
#         print(y)

#     else:
#         print(c)


# def bing(x):
#     blist = []
#     y = x/2
#     while y < 1:
#         y = x/2
#         c = x%2
#         x = y
#         blist.append(c)
#     print(blist)

# bing(10)

#如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。
# for i in range(100,1000):
#     Hundred = int(i/100) #百位数
#     ten = int(i%100/10) #十位
#     ge = i%10  #个位
#     sum = (Hundred**3)+(ten**3)+(ge**3)
#     if sum == i:
#         print(i)

'''编写一个函数 findstr()，
 该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
 例如：假定输入的字符串为
 “You cannot improve your past,but you can improve your future. Once time is wasted, life is wasted.”，
 子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。'''
# def findstr():
#     '统计输入的字符串中包含的子字符串个数'
#     x = input('请输入目标字符串：')
#     y = input('请输入子字符串（两个字符）:')

#     print( '子字符串再目标字符串中共出现 %d 次' % x.count(y))
# var = ' Hi '

# def fun1():
#     global var
#     var = ' Baby '
#     return fun2(var)

# def fun2(var):
#     var += 'I love you'
#     fun3(var)
#     return var

# def fun3(var):
#     var = ' 小甲鱼 '

# print(fun1())

'''编写一个函数，判断传入的字符串参数是否为“回文联”
（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）'''
def hui():
    x = input('请输入一句话：')
    length = len(x)    #计算输入的长度，赋值给length
    length = length//2  #地板除 取一半的整数
    fornt = x[:length+1]    #length+1，取前面的数
    behind = x[length:]     #取后面的数
    behind = behind[::-1]   #反转
    if fornt == behind:     #如果前面的数，和后面的数一样
        print('是回文联!')  
    else:
        print('不是回文联！')

