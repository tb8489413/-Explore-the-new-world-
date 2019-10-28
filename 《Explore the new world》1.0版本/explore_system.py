import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()


def show_menu():
    """显示菜单"""
    print("欢迎使用【新世界探索系统】")
    print("1.使用基础坐标仪")
    print("2.使用基础建造枪")
    print("3.使用基础扫描枪")
    print("4.使用基础帮助功能")
    print("0.退出系统")


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
    scan_start_x = float(input("请输入扫描起始点坐标:x"))
    scan_start_y = float(input("请输入扫描起始点坐标:y"))
    scan_start_z = float(input("请输入扫描起始点坐标:z"))

    scan_end_x = float(input("请输入扫描结束点坐标:x"))
    scan_end_y = float(input("请输入扫描结束点坐标:y"))
    scan_end_z = float(input("请输入扫描结束点坐标:z"))

    # 2.将玩家输入信息添加到程序并执行
    print("扫描开始···")
    mc.getBlocks(scan_start_x, scan_start_y, scan_start_z,
                 scan_end_x, scan_end_y, scan_end_z,)
    print("扫描结束\n")


def basic_help():
    """显示基础帮助"""

    print("游戏窗口中按下 F3 键，调试屏幕")
    print("游戏窗口中按下 F5 键，切换视角")
    print("游戏窗口中按下 / 符号，进入控制台")
    print("白天：time set 1300 9999")
    print("晴天：weather clear 9999\n")


def show_blocks():
    """显示方块类别"""
    pass

