##购物车小程序
####这是用Python3写的一款模拟购物车的小程序.

####使用说明:
- 登录
	- 用户输入登陆信息,若用户名在user_list中,则用户输入的密码需要与文档中一致, 否则报错,需重输密码
	- 若用户名不在其中, 视为新用户. 用户还需要输入工资信息,用户信息将被记录在user_list中
- 购物
	- 登陆成功后, 系统会打印在售商品列表. 用户需选择正确商品索引,若工资余额不小于商品价格,则购买成功. 该商品会被添加到用户购买清单中. 工资会相应扣减.
	- 若用户选择的商品索引不正确, 需要重新输入
	- 若用户输入quit,则结束整个程序   