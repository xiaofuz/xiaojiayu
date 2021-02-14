str1 = 'I love fishc.com'

print(str1[:6])

str1[:6] + "插入的字符串" + str1[6:]    #字符串和元组一样都是赋值过后就不能再变了，只能通过切片的方法，来进行重新组合

str2 = 'xiaoxie'

str2.capitalize()       #将字符串第一个字母大写

str3 = "XIAOKEzero"

str3.casefold()           #将字符串全部转换为小写

str3.center(50)             #将字符串前面填充50个空格，   
