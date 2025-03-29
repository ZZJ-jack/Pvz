from data.src.const import *
import math

def click(thingPos, thingSize, mousePos):
        # 判断鼠标点击的x坐标是否在物体的x坐标范围内
        if mousePos[0] > thingPos[0] and mousePos[0] < thingPos[0] + thingSize[0]:
            # 判断鼠标点击的y坐标是否在物体的y坐标范围内
            if mousePos[1] > thingPos[1] and mousePos[1] < thingPos[1] + thingSize[1]:
                # 如果在范围内，返回True
                return True
        # 如果不在范围内，返回False
        return False

def collision_detection(thing1, thing2):
        # 碰撞检测
        if thing1.pos[0] < thing2.pos[0]:
            if thing2.pos[0] > thing1.pos[0] + thing1.size[0]:
                if thing1.pos[1] < thing2.pos[1]:
                    if thing2.pos[1] > thing1.pos[1] + thing1.size[1]:
                        return True
                elif thing1.pos[1] > thing2.pos[1]:
                      if thing1.pos[1] < thing2.pos[1] + thing2.size[1]:
                           return True
        elif thing1.pos[0] > thing2.pos[0]:
             if thing1.pos[0] < thing2.pos[0] + thing2.size[0]:
                if thing1.pos[1] < thing2.pos[1]:
                    if thing2.pos[1] > thing1.pos[1] + thing1.size[1]:
                        return True
                elif thing1.pos[1] > thing2.pos[1]:
                      if thing1.pos[1] < thing2.pos[1] + thing2.size[1]:
                           return True
            
        # 如果没有交集，返回False
        return False

def collision_Plant_and_Zombie_detection(plant, zombie):
        # 碰撞检测
        if zombie.pos[0] <= plant.pos[0] + plant.size[0] - 45:
            if zombie.posY == plant.grid[1]:
                return True
        # 如果没有交集，返回False
        return False

def collision_Pea_add_Zombie_detection(zombie, pea):
    # 碰撞检测
    if zombie.pos[0] < pea.pos[0] + pea.size[0] - 30:
        if zombie.posY == pea.posY:
            return True
    # 如果没有交集，返回False
    return False

def getGrid(xy):
    # 获取网格坐标
    pos = list(xy) 
    grid = [0, 0]
    pos[0] -= GRID_LEFT_X
    pos[0] /= GRID_SIZE[0]
    pos[1] -= GRID_TOP_Y
    pos[1] /= GRID_SIZE[1]
    grid[0] = math.ceil(pos[0])
    grid[1] = math.ceil(pos[1])
    return grid

def getGridPos(xy):
    if not CheckInGarden(xy):
        return False
    grid = getGrid(xy)
    if grid[0] > 9 or grid[1] > 5:
        return False
    return[GRID_X[grid[0]], GRID_Y[grid[1]]]

def CheckInGarden(pos):
    # 检查坐标是否在花园内
    return pos[0] > GRID_LEFT_X and pos[0] < GRID_RIGHT_X and pos[1] > GRID_TOP_Y and pos[1] < GRID_DOWN_Y