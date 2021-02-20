file = input('请输入文件名：')      #接受用户输入的文件名，英文单词，翻译  file --> 文件



establish = open('D://%s' % file ,'x')  #establish 翻译  创建     创建一个用户输入的文件

content = input("请输入内容【单独输入':w'保存退出】：")


establish.write(content)



