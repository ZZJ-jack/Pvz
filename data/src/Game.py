from data.src.const import *  # 导入常量
from data.src.settings import *  # 导入设置
from data.src.zombie import *  # 导入僵尸类
from data.src.sunlight import *  # 导入阳光类
from data.src.Shovel import *  # 导入铲子类
from data.src.ShovelFrame import *  # 导入铲子框类
from data.src.util import *  # 导入工具类
from data.src.ZombieHeadLess import *  # 导入僵尸掉头类
from data.src.DisplayedSelectedCard import *  # 导入已选择卡片类
import pygame  # 导入pygame库
import math  # 导入math库

class Game:
    def __init__(self, game): # 初始化游戏
        # 初始化地图
        self.map = [
            [],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
        # 初始化金币
        self.gold = 200
        
        # 初始化游戏
        self.game = game
        self.screen = self.game.screen

        # 其他初始化
        self.shovel = Shovel(self.screen)  # 铲子
        self.shovelFrame = ShovelFrame(self.screen)  # 铲子框
        self.zombieTime = 0
        self.sunlightTime = 0
        self.zombieMusicPlay = False

        # 加载阳光音乐
        self.sunMusic = pygame.mixer.Sound(settings['game']['bgm']['sunlight'])
        # 设置音乐参数
        self.sunMusic.set_volume(settings['game']['bgm']['sunVolume'])  # 设置音量

        # 加载种植音乐
        self.plantMusic = pygame.mixer.Sound(settings['game']['bgm']['plant'])
        # 设置音乐参数
        self.plantMusic.set_volume(settings['game']['bgm']['plantVolume'])  # 设置音量

        # 加载僵尸啃食音乐
        self.zombieMusic = pygame.mixer.Sound(settings['game']['bgm']['zombieEat'])
        # 设置音乐参数
        self.zombieMusic.set_volume(settings['game']['bgm']['zombieEatVolume'])  # 设置音量

        # 加载土豆地雷爆炸音乐
        self.potatoMineExplodeMusic = pygame.mixer.Sound(settings['game']['bgm']['potatoMineExplode'])
        # 设置音乐参数
        self.potatoMineExplodeMusic.set_volume(settings['game']['bgm']['potatoMineExplodeVolume'])  # 设置音量

        # 初始化坐标
        GRID_X.append(0)
        GRID_Y.append(0)
        for i in range(1, GRID_COUNT[0] + 1):
            GRID_X.append(GRID_LEFT_X + (i - 1) * GRID_SIZE[0])
        for i in range(1, GRID_COUNT[1] + 1):
            GRID_Y.append(GRID_TOP_Y + (i - 1) * GRID_SIZE[1])
        
    def CheckInGarden(self, pos): # 检查坐标是否在花园内
        # 检查坐标是否在花园内
        return pos[0] > GRID_LEFT_X and pos[0] < GRID_RIGHT_X and pos[1] > GRID_TOP_Y and pos[1] < GRID_DOWN_Y

    def CheckPlant_Grid(self, plant_type): # 检查是否可以种植植物
        # 检查是否有足够的金币种植植物
        if self.gold >= settings[plant_type]['gold']:
            self.game.gridPlant.plantType = plant_type
            self.game.gridPlant.preIndexTimeNumber = settings['game']['plantPreIndexTimeNumber'][plant_type]
            self.game.Plant.preIndexTimeNumber = settings['game']['plantPreIndexTimeNumber'][plant_type]
            return True
        else:
            return False

    def CheckAddPlant(self, xy, plant_type): # 检查是否可以种植植物
        # 检查是否可以种植植物
        plant = True
        if not self.CheckInGarden(xy):
            plant = False
            return {'plant': plant,
                    'pos': False
                   }
        grid = self.getGrid(xy)
        if self.map[grid[1]][grid[0]] == 0:
            # 植物坐标
            self.map[grid[1]][grid[0]] = plant_type
            self.gold -= settings[settings['plant_name'][plant_type]]['gold']
            plant = True
            self.plantMusic.play()
        else:
            plant = False
        return {'plant': plant,
                'pos': [GRID_X[grid[0]], GRID_Y[grid[1]]]
               }

    def getGrid(self, xy): # 获取网格坐标
        pos = list(xy)
        grid = [0, 0]
        pos[0] -= GRID_LEFT_X
        pos[0] /= GRID_SIZE[0]
        pos[1] -= GRID_TOP_Y
        pos[1] /= GRID_SIZE[1]
        grid[0] = math.ceil(pos[0])
        grid[1] = math.ceil(pos[1])
        # 新增索引范围限制
        grid[0] = max(1, min(grid[0], GRID_COUNT[0]))
        grid[1] = max(1, min(grid[1], GRID_COUNT[1]))
        return grid
    
    def run(self):# 运行游戏
        self.draw()# 绘制游戏界面
        if self.game.really: # 如果游戏正式开始
            self.RunTimeDetermine()# 游戏信息处理
            self.updata()# 游戏运行
        else:# 游戏未开始
            self.ChooseCardTimeDetermine()# 游戏信息处理

    def draw(self): # 绘制游戏界面
        # 绘制游戏界面
        self.shovelFrame.run()  # 运行铲子框
        self.shovel.run()  # 运行铲子

    def updata(self): # 更新游戏
        self.zombieTime = (self.zombieTime + 1) % ZOMBIE_TIME
        self.sunlightTime = (self.sunlightTime + 1) % SUNLIGHT_TIME
        if self.zombieTime == 0: # 如果僵尸时间到了
            self.game.zombie_list.append(Zombie(self.game))
        if self.sunlightTime == 0: # 如果阳光时间到了
            self.game.sunlight_list.append(Sunlight(self.screen, (random.randint(GRID_LEFT_X, GRID_RIGHT_X), 0)))
        
        if pygame.mouse.get_pressed()[0] and not self.shovel.click: # 如果鼠标左键被按下且铲子上次操作已完成
            if not self.shovel.use:
                if click(self.shovel.pos, self.shovel.size, pygame.mouse.get_pos()):
                    self.shovel.use = True
                    self.shovel.click = True
            else:
                if collision_detection(self.shovel, self.shovelFrame):
                    self.shovel.use = False
                    self.shovel.click = True

        if pygame.mouse.get_pressed()[0] and self.shovel.use:
            if self.CheckInGarden(pygame.mouse.get_pos()):
                grid = getGrid(pygame.mouse.get_pos())
                if self.map[grid[1]][grid[0]] != 0:
                    for peashooter in self.game.peashooter_list:
                        if peashooter.grid == grid:
                            self.map[peashooter.grid[1]][peashooter.grid[0]] = 0
                            self.game.peashooter_list.remove(peashooter)
                            break
                    for sunflower in self.game.sunflower_list:
                        if sunflower.grid == grid:
                            self.map[sunflower.grid[1]][sunflower.grid[0]] = 0
                            self.game.sunflower_list.remove(sunflower)
                            break
                    for nut in self.game.nut_list:
                        if nut.grid == grid:
                            self.map[nut.grid[1]][nut.grid[0]] = 0
                            self.game.nut_list.remove(nut)
                            break
    
    def PlayZombieEatMusicDetermine(self): # 判断僵尸是否在吃植物
        eat = False
        for zombie in self.game.zombie_list:
            if zombie.eat:
                eat = True
                break
        if eat:
            if not self.zombieMusicPlay:
                self.zombieMusic.play(-1)
                self.zombieMusicPlay = True
        else:
            if self.zombieMusicPlay:
                self.zombieMusic.stop()
                self.zombieMusicPlay = False

    def ChooseCardTimeDetermine(self): # 游戏信息处理(选择卡片时间)
        # 判断卡片点击
        if not self.game.reallyButton.click:
            for card in self.game.displayed_card:
                if click(card.pos, card.size, pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not card.use:
                        card.use = True
                        self.game.selectedCard.append(DisplayedSelectedCard(
                                                                                self.game.screen,
                                                                                card.name,
                                                                                len(self.game.selectedCard) + 1
                                                                            )
                                                    )
                        break
        
        if not self.game.reallyButton.click:
            for card in self.game.selectedCard:
                if click(card.pos, card.size, pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not card.click:
                    for displayedCard in self.game.displayed_card:
                        if displayedCard.name == card.name:
                            deleteCardNumber = card.number
                            displayedCard.use = False
                            self.game.selectedCard.remove(card)
                            for selectedCard in self.game.selectedCard:
                                if selectedCard.number > deleteCardNumber:
                                    selectedCard.number -= 1
                                    selectedCard.pos[0] = CARD_FIRST_X + (CARD_SIZE[0] + 7) * (selectedCard.number - 1)
                                    selectedCard.click = True
                            break
    
    def CheckZombieIsnotEatPlant(self, zombie):
        return 1 <= zombie.grid[1] <= GRID_COUNT[1] and 1 <= zombie.grid[0] <= GRID_COUNT[0] and self.map[zombie.grid[1]][zombie.grid[0] - 1] == 0

    def RunTimeDetermine(self): # 游戏信息处理(正式运行时间)
        # 游戏信息判断
        self.PlayZombieEatMusicDetermine() # 游戏僵尸啃食植物bgm播放检测

        for zombie in self.game.zombie_list: # 遍历僵尸列表
            if zombie.hp == 0:
                continue
            # 遍历豌豆列表
            for pea in self.game.pea_list:
                # 如果豌豆和僵尸发生碰撞
                if collision_Pea_add_Zombie_detection(zombie, pea):
                    # 从豌豆列表中移除豌豆
                    self.game.pea_list.remove(pea)
                    # 僵尸的生命值减少20
                    zombie.hp -= 20
                    if zombie.hp <= 40 and zombie.head:
                        zombie.path = settings['zombie']['headlessPath']
                        zombie.imageCount = settings['zombie']['headlessImageCount']
                        self.game.zombieHead_list.append(ZombieHeadLess(self.screen, (zombie.pos[0] + 30, zombie.pos[1])))
                        zombie.head = False
                    # 如果僵尸的生命值小于等于0
                    if zombie.hp <= 0:
                        zombie.hp = 0
                        zombie.imageIndex = 0
                        zombie.path = settings['zombie']['deadPath']
                        zombie.imageCount = settings['zombie']['deadImageCount']
                        for Zombie in self.game.zombie_list:
                            if zombie.posY == Zombie.posY:
                                flag = True
                                break
                        if not flag:
                            self.game.zombiePos[zombie.posY] = False
        
        for zombie in self.game.zombie_list: # 游戏信息判断
            # 遍历豌豆射手列表
            if zombie.hp <= 40:
                if zombie.eat:
                    zombie.eat = False
                continue
            
            for peashooter in self.game.peashooter_list:
                # 如果豌豆射手和僵尸发生碰撞
                if collision_Plant_and_Zombie_detection(peashooter, zombie):
                    if not zombie.eat:
                        zombie.eat = True
                    # 豌豆射手的攻击次数加1
                    peashooter.hpTime += 1
                    # 如果攻击次数达到PLNAT_HP
                    if peashooter.hpTime == PLNAT_HP:
                        # 重置攻击次数
                        peashooter.hpTime = 0
                        # 豌豆射手生命值减20
                        peashooter.hp -= 20
                        # 如果豌豆射手生命值小于等于0
                        if peashooter.hp <= 0:
                            # 从豌豆射手列表中移除豌豆射手
                            self.map[peashooter.grid[1]][peashooter.grid[0]] = 0
                            self.game.peashooter_list.remove(peashooter)
                            zombie.eat = False
                else:
                    if self.CheckZombieIsnotEatPlant(zombie):
                        if zombie.eat:
                            zombie.eat = False
                
        for zombie in self.game.zombie_list: # 游戏信息判断
            if zombie.hp <= 40:
                if zombie.eat:
                    zombie.eat = False
                continue
            
            # 遍历坚果列表
            for nut in self.game.nut_list:
                # 如果坚果和僵尸发生碰撞
                if collision_Plant_and_Zombie_detection(nut, zombie):
                    if not zombie.eat:
                        zombie.eat = True
                    # 坚果的攻击次数加1
                    nut.hpTime += 1
                    # 如果攻击次数达到NUT_HP
                    if nut.hpTime == NUT_HP:
                        # 重置攻击次数
                        nut.hpTime = 0
                        # 坚果生命值减20
                        nut.hp -= NUT_HP / 4.0
                        if nut.hp == NUT_HP / 4.0 * 3:
                            if not nut.path == settings['nut']['path2']:
                                nut.path = settings['nut']['path2']
                                nut.imageCount = settings['nut']['imageCount2']
                        elif nut.hp == NUT_HP / 4.0 * 2:
                            if not nut.path == settings['nut']['path3']:
                                nut.path = settings['nut']['path3']
                                nut.imageCount = settings['nut']['imageCount3']
                        elif nut.hp == NUT_HP / 4.0:
                            # 从坚果列表中移除坚果
                            self.map[nut.grid[1]][nut.grid[0]] = 0
                            self.game.nut_list.remove(nut)
                            zombie.eat = False
                else:
                    if self.CheckZombieIsnotEatPlant(zombie):
                        if zombie.eat:
                            zombie.eat = False
        
        for zombie in self.game.zombie_list: # 游戏信息判断
            if zombie.hp <= 40:
                if zombie.eat:
                    zombie.eat = False
                continue
            
            # 遍历向日葵列表
            for sunflower in self.game.sunflower_list:
                # 如果向日葵和僵尸发生碰撞
                if collision_Plant_and_Zombie_detection(sunflower, zombie):
                    if not zombie.eat:
                        zombie.eat = True
                    # 向日葵的攻击次数加1
                    sunflower.hpTime += 1
                    # 如果攻击次数达到PLNAT_HP
                    if sunflower.hpTime == PLNAT_HP:
                        # 重置攻击次数
                        sunflower.hpTime = 0
                        # 向日葵生命值减20
                        sunflower.hp -= 20
                        # 如果向日葵生命值小于等于0
                        if sunflower.hp <= 0:
                            # 从向日葵列表中移除向日葵
                            self.map[sunflower.grid[1]][sunflower.grid[0]] = 0
                            self.game.sunflower_list.remove(sunflower)
                            zombie.eat = False
                else:
                    if self.CheckZombieIsnotEatPlant(zombie):
                        if zombie.eat:
                            zombie.eat = False

        for potatoMine in self.game.potatoMine_list: # 地雷爆炸判断
            for zombie in self.game.zombie_list:
                # 如果地雷和僵尸发生碰撞
                if collision_Plant_and_Zombie_detection(potatoMine, zombie):
                    # 如果地雷和僵尸在同一行
                    if zombie.posY == potatoMine.grid[1]:
                        if not potatoMine.Explode:
                            potatoMine.Explode = True
                            self.potatoMineExplodeMusic.play()
                        if not zombie.path == settings['zombie']['deadPath']:
                            if zombie.hp > 40:
                                self.game.zombieHead_list.append(ZombieHeadLess(self.screen, (zombie.pos[0] + 30, zombie.pos[1])))
                            zombie.hp = 0
                            zombie.imageIndex = 0
                            zombie.path = settings['zombie']['deadPath']
                            zombie.imageCount = settings['zombie']['deadImageCount']
                            for Zombie in self.game.zombie_list:
                                if zombie.posY == Zombie.posY:
                                    flag = True
                                    break
                            if not flag:
                                self.game.zombiePos[zombie.posY] = False

        if pygame.mouse.get_pressed()[0]: # 如果鼠标左键被按下
            for sunlight in self.game.sunlight_list:  # 遍历阳光列表
                if click(sunlight.pos, sunlight.size, pygame.mouse.get_pos()):  # 如果点击阳光
                    self.sunMusic.play()  # 播放阳光音乐
                    self.gold += 25  # 加阳光
                    self.game.sunlight_list.remove(sunlight)  # 移除阳光

        for sunlight in self.game.sunlight_list: # 遍历阳光列表
            if sunlight.delete:
                self.game.sunlight_list.remove(sunlight)