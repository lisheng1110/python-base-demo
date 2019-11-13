# f=open("D:\\softwaredata\\python\\gy-1910A\\feng_zhuang\\wenjian.txt","r",encoding="utf-8")#r读取文件
# print(f.readlines())#读取全部内容，返回一个列表格式
# f.close()
# f=open("D:\\softwaredata\\python\\gy-1910A\\feng_zhuang\\wenjian.txt","w",encoding="utf-8")#w清空写入
# f.write("你好，师姐!!!\n")#写入字符串格式
# f.writelines(["你好，方便面","我想泡你!"])#写入列表格式
# f.close()#关闭
f = open("D:\\softwaredata\\python\\gy-1910A\\feng_zhuang\\wenjian.txt", "a", encoding="utf-8")  # a追加写入
f.write("你好，方便面\n")  # 写入字符串格式
f.writelines(["你好，方便面！", "我想泡你！"])  # 写入列表格式
f.close()
