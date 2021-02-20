import tkinter

inpute = ''
#创建一个空字典，用来存放
data1 = {}  


#创建一个新建用户函数
def user():
    username = input('请输入用户名：')
    while username  in data1:
        username = input('此用户名已经被使用，请重新输入：')
            
    password = input('请输入密码：')
    
    data1[username] = password
    print('注册成功，赶紧试试登陆吧^_^')

#创建 登录账号函数
def sign():
    name = input('请输入用户名：')
    while name  not in data1.keys():
        name  = input('您输入的用户名不存在，请重新输入：')
    sign_password = input('请输入密码：')
    if data1[name] == sign_password:
        print('欢迎进入XXOO系统，请点右上角的x结束程序！')
        top = tkinter.Tk('diddd')
        top.mainloop()


#主体调用
while True:
    print('|--- 新建用户：N/n ---|')
    print('|--- 登录账号：E/e ---|')
    print('|--- 退出程序：Q/q ---|')
    inpute = input('|--- 请输入指令代码：')
    if inpute == 'N' or inpute == 'n':
        user() 
    elif inpute == 'E' or inpute == 'e':
        sign()
    elif inpute == 'Q' or inpute == 'q':
        break