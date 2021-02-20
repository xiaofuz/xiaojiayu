print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

inpute = 0
data1 = {}
while inpute != 4:
    #inpute 输入的相关指令代码放里面的原因是，下面的输入错了，可以返回到这个循环，再重新输入指令
    inpute =  int(input('请输入相关的指令代码：'))          
    if inpute < 0 or inpute >=5:   #查询联系人资料
        print('输入错误，请重新输入')
        continue    
    if inpute == 1:          
        name = input('请输入联系人姓名：')
        if name in data1.keys():
            print(data1[name])
        else:
            print('未查找到此联系人，请插入新的联系人')
            continue
        
        
    if inpute == 2:             #插入新的联系人
        name = str(input('请输入联系人姓名：'))
        
        if name in data1:
            print('您输入的姓名在通讯录中已存在 -->> %s:%d'% (name,data1[name]))
            whether = input('是否修改用户资料（YES/NO）：')
            if whether == 'YES':
                data1[name] = input('请输入联系电话：')
                print('联系人：%s --联系电话：%d 更新成功' % (name,data1[name]))
            elif whether == 'NO':
                print('通讯录未修改')
                
        else:
            telephone = int(input('请输入用户联系电话：'))
            data1[name] = telephone
            print('添加联系人：%s --联系电话：%d 成功' % (name,telephone))

    #删除已有的联系人
    elif inpute == 3:           
        name = input('请输入联系人姓名：')
        if name in data1.keys():
            whether = input('确定删除：YES/NO：')
            if whether == 'YES':
                del data1[name]
                print('删除成功')
            elif whether == 'NO':
                print('联系人未删除……返回中…………')
            else:
                print('输入错误，请重新输入：')
                continue
        else:
            print('未查到该联系人……')        
    

    #退出通讯录程序
    else:                       
        print('|--- 感谢使用通讯录程序 ---|')
        inpute = 4
        
