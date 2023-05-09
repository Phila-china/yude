# -*- coding: utf-8 -*-

"""
1. 实现英雄的添加功能。
```
请输入数字，选择需要完成的操作：1
请输入英雄的名称：jinx
请输入英雄的血量：20
请输入英雄的攻击力：30
创建成功
```

2. 实现英雄的查询功能
```
请输入需要查询的英雄信息
```

3. 实现英雄的修改功能

4. 实现英雄的删除功能

5. 退出系统

"""

print("""
1. **创建英雄**
2. **查看英雄信息**
3. **修改英雄信息**
4. **删除英雄**
5. **退出系统**
""")


def delete_hero(hero_list, hero_name):
    for i in hero_list:
        if hero_name == i['name']:
            hero_list.remove(i)
            print(f"删除之后所有的英雄数据信息为{hero_list}")
            return hero_list
    print("没有找到要删除的英雄")
    return hero_list


def search_hero(hero_name):
    for i in hero_list:
        if hero_name == i['name']:
            print(f"英雄{res}的信息为{i}")


def update_hero(hero_name):
    for i in hero_list:
        if hero_name == i['name']:
            i['volume'] = input("请问你将血量修改为多少？ ")
            print(f"更新之后所有的英雄数据信息为{hero_list}")
            return hero_list
    print("没有找到要更新的英雄")
    return hero_list


def creat_hero(name, volume, power):
    hero_info = {"name": name, "volume": volume, "power": power}
    print(f"创建成功：英雄的名称为{hero_name},英雄的血量为{hero_volume},英雄的攻击力为{hero_power}")
    hero_list.append(hero_info)


hero_list = []
while True:
    res = input("请输入对应的选项，即可执行对应的操作： ")

    if res == "1":
        hero_name = input("请输入英雄的名称：")
        hero_volume = input("请输入英雄的血量：")
        hero_power = input("请输入英雄的攻击力：")
        creat_hero(hero_name, hero_volume, hero_power)

    elif res == "2":
        hero_name = input("请输入需要查询的英雄信息: ")
        search_hero(hero_name)

    elif res == "3":
        hero_name = input("请输入需要更新的英雄信息: ")
        update_hero(hero_name)

    elif res == "4":
        hero_name = input("请输入需要删除的英雄信息: ")
        delete_hero(hero_list, hero_name)

    else:
        print("退出系统")
        break
