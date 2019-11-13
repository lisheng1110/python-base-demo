# a=input("你瞅啥：")
# print("我瞄了一眼：",a)
import json
a="""
{"name":"李胜","sex":null}
"""
print(json.loads(a))#json转字典
b={"name":"李胜","sex":None}#字典转json
print(json.dumps(b))



