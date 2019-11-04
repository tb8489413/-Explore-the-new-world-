import explore_system as system

# 序幕
# prologue = "欢迎来到《Explore the new world》1.0 版本," \
#            "这是款基于《Minecraft》1.9.2引擎，通过Python3设计的游戏," \
#            "目前游戏处于开发测试期," \
#            "开发人员名单：石头Teacher"
# for i in prologue:
#     print(i, end="")
#     time.sleep(0.1)
print("游戏开始")

while True:
    system.show_menu()
    action = input("请输入功能编号:")

    # 根据玩家输入后决定后续的操作
    if action in ["1", "2", "3", "4", "5","6","7"]:
        if action == "1":
            print("【基础坐标仪】功能已开启")
            system.basic_gps()

        elif action == "2":
            print("【基础建造枪】功能已开启")
            system.build_size()

        elif action == "3":
            print("【基础扫描仪】功能已开启")
            system.scan_size()

        elif action == "4":
            print("【方块记录仪】功能已开启")
            system.new_block()

        elif action == "5":
            print("【显示所有方块记录】功能已开启")
            system.show_block()

        elif action == "6":
            print("【方块信息搜索】功能已开启")
            system.search_block()

        elif action == "7":
            print("【基础帮助功能】功能已开启")
            system.basic_help()

    elif action == "close":
        print("【新世界探索系统】关闭")
        break

    else:
        print("输入错误，请重新输入：")

    


    
