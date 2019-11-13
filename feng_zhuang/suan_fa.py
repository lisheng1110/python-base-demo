# 冒泡排序
a = [9, 2, 35, 4, 5, 10, 1, 0, 7]
length = len(a)
for i in range(length - 1, 0, -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "x", i, "=", i * j, '\t', end='')  # print(j,"x",i,"=",i*j,end='\t')
    print()

# 字符串格式化
# s=''
# for i in range(1,10):
#     for j in range(1,i+1):
#         s+='{}x{}={}\t'.format(j,i,i*j)
#     s+='\n'
# print(s)
