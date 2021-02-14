#如何使用反斜杠

'''demo = r"c:\\Desktop"

print (demo)


#计算一年有多少秒？

DaysPerYear = 365   #一年有365天
HoursPerDay = 24    #一天有24小时
MinutesPerHour = 60 #一小时有60分钟
SecondPerMinute = 60    #一分钟有60秒

#一小时×一分钟=一个小时多少秒
#一天*


sum = SecondPerMinute*MinutesPerHour*HoursPerDay*DaysPerYear

print (sum)


x = 458

a = ['hello',[1,2,3]]
b = a[:]
 
print([id(x) for x in a])
print([id(x) for x in b])


a[0] = 'world'
a[1].append(4)
print(a)
print(b)



A = int(input("请输入整数a"))
B = int(input("请输入整数b"))
print(A+B)


a,b,c = (input("请输入输入三个数，用空格分开：").split())
a = int(a)
b = int(b)
c = int(c)
print(b*b-4*a*c)

'''



S = 11
m = input()
while S <= m:
    S +=1
sum = S
print("sum = ",sum)