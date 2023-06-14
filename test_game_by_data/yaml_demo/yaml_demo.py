

import yaml

# data = {
#     "client": {"default-character-set": "utf8"},
#     "mysql": {"user": 'root', "password": 123},
#     "custom": {
#         "user1": {"user": "张三", "pwd": 666},
#         "user2": {"user": "李四", "pwd": 999},
#     }
# }
#
# # 直接 dump 可以把 python 对象转为 YAML 文档
# with open('./my.yaml', 'w', encoding='utf-8') as f:
#     yaml.dump(data, f, allow_unicode=True)

# 读取yaml文件中的内容，转化为python对象
with open('../my.yaml', 'r', encoding='utf8') as f:
    data = yaml.safe_load(f)

print(data)
print(data['custom']['user1']['user'])
