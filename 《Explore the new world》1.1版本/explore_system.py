import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

# 定义已知方块列表
block_list = []

# 定义未知方块列表
unblock_list = []

# 定义已知方块基数
num = 0

# 定义未知方块基数
unnum = 0



def show_menu():
    """显示菜单"""

    print("✦" * 23)
    print("欢迎使用【新世界探索系统】")
    print("1.使用基础坐标仪")
    print("2.使用基础建造枪")
    print("3.使用基础扫描枪")
    print("4.使用方块记录仪")
    print("5.显示所有方块记录")
    print("6.使用方块信息搜索")
    print("7.使用基础帮助功能")
    print("close.关闭系统")
    print("✦" * 23)

def basic_gps():
    """显示玩家坐标"""

    player_gps = mc.player.getTilePos()
    print("玩家当前坐标点：",
          "X:"+str(player_gps.x), " Y:"+str(player_gps.y), " Z:"+str(player_gps.z), "\n")


def build_size():
    """建造尺寸"""

    # 1.提示玩家输入建造尺寸信息
    build_start_x = int(input("请输入建造起始点坐标:x"))
    build_start_y = int(input("请输入建造起始点坐标:y"))
    build_start_z = int(input("请输入建造起始点坐标:z"))

    build_end_x = int(input("请输入建造结束点坐标:x"))
    build_end_y = int(input("请输入建造结束点坐标:y"))
    build_end_z = int(input("请输入建造结束点坐标:z"))

    build_block_ID = int(input("请输入方块的ID:"))
    build_block_Data_ID = int(input("请输入方块的Data ID:"))

    # 2.将玩家输入信息添加到程序并执行
    print("建造生成开始···")
    mc.setBlocks(build_start_x, build_start_y, build_start_z,
                 build_end_x, build_end_y, build_end_z,
                 build_block_ID, build_block_Data_ID)
    print("建造生成结束\n")


def scan_size():
    """扫描范围"""

    # 1.提示玩家输入扫描范围信息
    scan_start_x = int(input("请输入扫描起始点坐标:x"))
    scan_start_y = int(input("请输入扫描起始点坐标:y"))
    scan_start_z = int(input("请输入扫描起始点坐标:z"))

    scan_end_x = int(input("请输入扫描结束点坐标:x"))
    scan_end_y = int(input("请输入扫描结束点坐标:y"))
    scan_end_z = int(input("请输入扫描结束点坐标:z"))

    # 2.将玩家输入信息添加到程序并执行
    print("扫描开始···")
    all = mc.getBlocks(scan_start_x, scan_start_y, scan_start_z,
                 scan_end_x, scan_end_y, scan_end_z,)
    print(all)
    print(len(all))

    # 3.遍历方块列表
    # 将未知方块信息保存到字典
    unblock_dict = {"名称": "*", "ID": "*", "Data ID": "*", "数量": unnum}

    # 将字典添加到方块列表
    unblock_list.append(unblock_dict)



    # 定义逗号数量
    n1 = 0

    # 定义非存储方块数量
    n2 = 0

    for i in all:
        if len(block_list) != 0:
            for block_dict in block_list :
                if i == ",":
                    n1 += 1

                if i == block_dict["ID"] :
                    block_dict["数量"] += 1

                if block_dict["ID"] != i :
                    n2 += 1


            # 打印表头
            for j in ["名称", "ID", "Data ID", "数量"]:
                print(j, end="\t")

            print("")
            # 打印分割线
            print("-" * 23)
            print("%s\t%s\t%s\t\t%s" % (block_dict["名称"],
                                      block_dict["ID"],
                                      block_dict["Data ID"],
                                      block_dict["数量"]))

            unblock_dict["数量"] = n2 - n1

            print("-" * 23)
            print("%s\t%s\t%s\t\t%s" % (unblock_dict["名称"],
                                      unblock_dict["ID"],
                                      unblock_dict["Data ID"],
                                      unblock_dict["数量"]))

        else:
            for unblock_dict in unblock_list :
                if i == ",":
                    n1 += 1

                if i == unblock_dict["ID"] :
                    unblock_dict["数量"] += 1

                if unblock_dict["ID"] != i :
                    n2 += 1

            unblock_dict["数量"] = n2 - n1

            # 打印表头
            for j in ["名称", "ID", "Data ID", "数量"]:
                print(j, end="\t")

            print("")

            # 打印分割线
            print("-" * 23)
            print("%s\t%s\t%s\t\t%s" % (unblock_dict["名称"],
                                      unblock_dict["ID"],
                                      unblock_dict["Data ID"],
                                      unblock_dict["数量"]))

    print("扫描结束\n")


def new_block():
    """新添加方块"""

    # 提示玩家输入方块信息
    block_name = input("请输入方块的名称：")
    block_ID = input("请输入方块的ID:")
    block_Data_ID = input("请输入方块的Data ID:")



    # 将方块信息保存到字典
    block_dict = {"名称": block_name, "ID": block_ID, "Data ID": block_Data_ID, "数量":num}

    # 将字典添加到方块列表
    block_list.append(block_dict)

    # 提示成功添加信息
    print('成功添加方块【'+block_dict["名称"]+"】的信息")


def basic_help():
    """显示基础帮助"""

    print("游戏窗口中按下 F3 键，调试屏幕")
    print("游戏窗口中按下 F5 键，切换视角")
    print("游戏窗口中按下 / 符号，进入控制台")
    print("白天：time set 1300 9999")
    print("晴天：weather clear 9999\n")


def show_block():
    """显示方块类别"""

    # 判断是否存在方块记录，如果没有，提示用户并返回
    if len(block_list) == 0:
        print("当前没有任何方块记录，请使用方块记录仪添加方块")
        return

    # 打印表头
    for i in ["名称", "ID", "Data ID"]:
        print(i, end="\t")

    print("")
    # 打印分割线
    print("=" * 23)

    for block_dict in block_list:
        print("%s\t%s\t%s" % (block_dict["名称"],
                                  block_dict["ID"],
                                  block_dict["Data ID"]))


def search_block():
    """搜索方块"""

    # 提示要搜索的方块名称
    find_name = input("请输入要搜索的方块名称：")

    # 遍历字典
    for block_dict in block_list:
        if block_dict["名称"] == find_name:
            # 打印表头
            for j in ["名称", "ID", "Data ID"]:
                print(j, end="\t")

            print("")
            # 打印分割线
            print("-" * 23)
            print("%s\t%s\t%s" % (block_dict["名称"],
                                      block_dict["ID"],
                                      block_dict["Data ID"]))

            # 根据找到的字典进行后续操作：修改/删除
            deal_block(block_dict)
            break
    else:
        print("没有找到：【"+find_name+"】方块")


def deal_block(find_dict):
    """方块信息修改"""

    action_str = input("请选择要执行的操作"
                       "[1]修改 [2]删除 [0]返回上级菜单")
    if action_str == "1":
        find_dict["名称"] = input("方块名称：")
        find_dict["ID"] = input("方块ID:")
        find_dict["Data ID"] = input("方块Data ID")

        print("修改方块信息成功")
    elif action_str == "2":
        block_list.remove(find_dict)

        print("删除方块信息成功")
