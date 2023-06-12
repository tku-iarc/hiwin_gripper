from calendar import c
from operator import mod
import numpy as np
from ctypes import *
import time
import cv2



so_file = "/home/iclab_luis/work/hiwin_gripper_ws/src/hiwin_gripper_api/HIWIN_XEG32/src/controller/Hiwin_API.so"
modbus = CDLL(so_file)


class HIWIN_GRIPPER(object):
    def __init__(self):
        super(HIWIN_GRIPPER, self).__init__()
        #rospy.init_node('move_group_tutorial_ur5', anonymous=True)


    #move
    #功能 : 絕對位置移動模式
    #參數 : 
    #    dis = 位置(0~3200)
    #    speed = 速度(0~4800)
    #    flag = 旗標?(待確定)

    def ON(self):
        modbus.libModbus_Connect(1)
            
        print("modbus on")
        return

    def reset(self):
        modbus.reset()
        time.sleep(25)
        print("gripper reset")
        return

    def move(self, dis, speed, flag):
        state = 1
        modbus.move(dis, speed, flag)
        time.sleep(0.01)
        while state!='2':
            state = str(modbus.read_mode())
            if state!='3':
                break
        print("end move")
        return

    def expert(self, move=0, dis=0, speed=1200, Holding_stroke = 0, Holding_speed = 0, Holding_force = 0, flag=1):
        state = 1
        modbus.expert(move, dis, speed, Holding_stroke, Holding_speed , Holding_force, flag)
        time.sleep(0.01)
        while state!='3':
            state = str(modbus.read_mode())
            if state!='0':
                break
        print("end move")
        return

    def OFF(self, close):
        if close == 1:
            modbus.Modbus_Close()
        print("modbus off")
        return



if __name__ == "__main__":

    modbus.libModbus_Connect(1)

    gripper_api = HIWIN_GRIPPER()
    gripper_api.ON()

    while True:
        mode = input("(1=reset, 2=close, 3=open): ")
        if mode == '1':
            gripper_api.reset()
            time.sleep(25)      # 等待reset時間
        elif mode == '2':
            gripper_api.move(100,4800,1)      # 絕對位置移動 (0~3200)
        elif mode == '3':
            gripper_api.move(3200,4800,1)      # 絕對位置移動 (0~3200)
        elif mode == '4':
            gripper_api.expert(0, 600,6000,2600,500,40,1)      # 絕對位置移動 (0~3200)
        else:
            pass


modbus.Modbus_Close()

