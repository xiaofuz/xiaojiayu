# for i in range(0, 10, 2):
#     print('I Love FishC')
# for i in range(10):
#     print(i)

# while True:
#     while True:
#         break
#         print(1)
#     print(2)
#     break
# print(3)


# for i in range(1,11):
#     print('今日学习了Python {} 节课'.format(i))

# x=1
# y=2
# z=3
# print(x,y,z)
# x=z
# print(x)
# y=x/z
# print(int(y))
# z= x-y
# print(int(z))

# x,y,z=z,y,x


# x = int(input())
# if 90<x<=100:
#   print('A')
# elif x>=80:
#   print('B')
# elif x>=60:
#   print('C')
# elif x<60:
#   print('B')
# else:
#   print('输入错误') 


# a = 3
# password = 'ke'
# while a:
#     passwor = input('请输入密码')
#     if password == passwor:
#         print('密码正确')
#         break
#     elif '*' in passwor:
#         print("密码中不能包含'*'号！您还有",a,'次机会！',end = ' ')
#         continue
#     else:
#         print('密码输入错误！您还有',a-1,'次机会！',end = ' ')
#     a -= 1


# print('red\tyellow\tgreen')
# for red in range(0,4):
#     for yellow in range(0,4):
#         for green in range(2,8):
#             if red + yellow + green == 8:
#                 print(red,'\t',yellow,'\t',green)

#每次要那8个球，再怎么样，就算红球和黄球都拿出来了，也只是有6个，
#所以无论如何，至少都要拿两个绿球出来

# for i in range(100,1000):
#     sum = 0
#     temp = i
#     while temp:
#         sum = sum + (temp%10) ** 3
#         temp //= 10
#     if sum == i:
#         print(i)


# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']

# count = 0

# length = len(member)

# while count < length:

#     print(member[count],member[count+1])

#     count += 2

def min(x):

  least = x[0]

  for each in x:

    if each < least:

      least = each

  return least

print(min('123456789'))