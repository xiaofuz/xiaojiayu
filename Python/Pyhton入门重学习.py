# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
# for each in range(len(member)):
#     if each%2 == 0:
#         print(member[each], member[each+1])

# list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]

# list1[1][2] = '小鱿鱼'
# print(list1)

# list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]

# list5 = []
# for x in range(10):
#     for y in range(10):
#         if x%2==0:
#             if y%2!=0:
                
#                 print((x,y))
#                 list5.append((x,y))
# print(list5)
# 0.我觉得会打印 [6]，上机后操作，发现，打印出来的是[1，2，3，4，5]
# 1.del list1[1][2]，刚开始想的太复杂了，想着先用del先把列表里面的给删除了，然后再添加，后来发现怎么都添加不进去了，之后看到了del 后面的删除的语句，想起了，可以直接用这种修改方式修改：list1[1][2] = '小鱿鱼'
# 2.list.sort()  这个就更难受了，单词记错了，怎么也执行不了，找了好多，怎么看没有这个函数，又去查了菜鸟编程，发现，原来列表排序方法，原来是叫sort(),真的是sourt()打习惯了。
# 3.list.sort(reverse=True)
# 4.这两个英文我熟悉，copy,翻译过来是复制的意思，也就是拷贝一个列表，list5 = list.copy()
# clear() 清除列表，成了一个空的列表了。
# 5.0，1，4，9，16，……
# 6.

list1 = ['1.Jost do It','2.一切皆有可能','3.让变成改变世界','4.Impossible is Nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼c工作室','1.耐克']
'list3 = (list2[3],':',list1[0],list2[1],list1[1],list2[2],list1[2],list2[0],list2[3])'
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
for each in list3:
    print(each)

