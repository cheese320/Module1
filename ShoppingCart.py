#!/usr/bin/python
# -*- coding: utf-8 -*-

prod_list = [
      ["iphone", 5000],
      ["Mac Pro", 12000],
      ["Starbucks", 31],
      ["alex", 81],
      ["Bike", 800]]


user_list = open('user_list', 'r+', encoding='utf-8')

name = input('请输入用户名: ')
password = input('请输入密码')

user = eval(str(user_list.read()))

while True:
    # 判断用户名是否存在
    if name in user.keys():  # 非初次登录用户
        # 判断用户登陆信息是否正确
        if password in user[name]:  # 用户名密码正确
            salary = int(user[name][password])
            print('您的工资余额是\033[31;1m%s\033[0m' % salary)
            break
        else:
            password = input('密码错误,请重输:')
            continue
    else:  # 首次登陆,将用户信息添加入user_list
        new_user = {}
        salary = input('salary: ')
        if salary.isdigit():
            salary = int(salary)
            new_user[password] = salary
            user[name] = new_user
            user_list.seek(0)
            user_list.write(str(user))
            break
        else:
            print('请重输')
            continue


# 打开已购买清单
shopping_list = open('shopping_list', 'r+', encoding='utf-8')
history = eval(str(shopping_list.read()))

if name not in history:
    history[name] = []  # 首次登陆用户,历史清单为空
shopping_history = history[name]  # 非首次登陆用户的历史购物信息
shopping_new = []  # 本次购物信息
print_hisotry = input('是否打印历史购物清单 =?')
if print_hisotry == 'Y':
    print('-------- 历史购物清单 --------')
    print(shopping_history)
    print('-------- The End --------')

while True:
    print('-------- 在售商品列表 --------')
    for index, item in enumerate(prod_list):
        print(index, item)
    print('-------- The End --------')

    choice = input('请选择购买哪个商品')
    if choice == 'quit':  # 退出时,将更新的用户信息存入user_list, 并打印本次购买商品清单
        user[name][password] = str(salary)
        user_list.seek(0)
        user_list.write(str(user))
        print('-------- 您已成功购买商品清单 --------')
        print(shopping_new)
        print('您的工资余额是\033[31;1m%s\033[0m' % salary)
        print('-------- The End --------')
        # 将本次购物清单与历史购物信息合并
        shopping_history.extend(shopping_new)
        history[name] = shopping_history
        shopping_list.seek(0)
        shopping_list.write(str(history))
        exit(0)
    elif not choice.isdigit():
        print('请输入有效的商品索引')
    elif len(prod_list) > int(choice) >= 0:  # 用户选择未超出商品列表范围
        p_item = prod_list[int(choice)]
        if salary >= p_item[1]:
            salary -= p_item[1]
            shopping_new.append(p_item)
            print('-------- 本次购物清单 --------')
            print(shopping_new)
            print('您的工资余额是\033[31;1m%s\033[0m' % salary)
            print('-------- The End --------')
        else:
            print('余额不足')
    else:
        print('请输入有效的商品索引')
