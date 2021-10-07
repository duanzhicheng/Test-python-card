
import card_tools
# 提示用户输入操作

# for num_str in ["1", "2", "3"]:
while True:
    # 显示系统菜单
    card_tools.show_menu()

    num_str = input("请输入要执行的操作：")

    print("你执行的操作是【%s】" % num_str)

    if num_str in ["1", "2", "3"]:

        # 新增名片
        if num_str == "1":

            card_tools.new_card()
        # 显示全部
        elif num_str == "2":

            card_tools.show_all()
        # 搜索名片
        elif num_str == "3":

            card_tools.search_card()
    # "0"退出系统
    elif num_str == "0":

        print("欢迎再次使用【名片管理系统】！")

        break

    else:
        print("输入错误！请重新输入！")
