from data.src._BasicImports import *  # 导入所有需要的模块和常量
from data.src._GameObjectImports import *  # 导入所有需要的类和函数

class Game:
    def __init__(self, game): 
        """
        初始化游戏对象

        :param game: 游戏主对象，包含游戏的基本信息和状态
        """
        # 初始化地图，使用二维列表表示，0 表示该位置没有植物
        self.map = [
            [],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
        # 初始化玩家拥有的金币数量
        self.gold = 200
        
        # 初始化游戏相关对象
        self.game = game
        self.screen = self.game.screen

        # 初始化游戏道具和状态变量
        self.shovel = Shovel(self.screen)  # 初始化铲子对象
        self.shovelFrame = ShovelFrame(self.screen)  # 初始化铲子框对象
        self.zombieTime = 0  # 僵尸生成计时器
        self.sunlightTime = 0  # 阳光生成计时器
        self.zombieMusicPlay = False  # 标记僵尸啃食音乐是否正在播放

        # 加载阳光音乐并设置音量
        self.sunMusic = pygame.mixer.Sound(settings["game"]["bgm"]["sunlight"])
        self.sunMusic.set_volume(settings["game"]["bgm"]["sunVolume"])  # 设置阳光音乐音量

        # 加载种植音乐并设置音量
        self.plantMusic = pygame.mixer.Sound(settings["game"]["bgm"]["plant"])
        self.plantMusic.set_volume(settings["game"]["bgm"]["plantVolume"])  # 设置种植音乐音量

        # 加载僵尸啃食音乐并设置音量
        self.zombieMusic = pygame.mixer.Sound(settings["game"]["bgm"]["zombieEat"])
        self.zombieMusic.set_volume(settings["game"]["bgm"]["zombieEatVolume"])  # 设置僵尸啃食音乐音量

        # 加载土豆地雷爆炸音乐并设置音量
        self.potatoMineExplodeMusic = pygame.mixer.Sound(settings["game"]["bgm"]["potatoMineExplode"])
        self.potatoMineExplodeMusic.set_volume(settings["game"]["bgm"]["potatoMineExplodeVolume"])  # 设置土豆地雷爆炸音乐音量

        # 初始化网格坐标列表
        GRID_X.append(0)
        GRID_Y.append(0)
        # 计算并添加 x 轴上每个网格的坐标
        for i in range(1, GRID_COUNT[0] + 1):
            GRID_X.append(GRID_LEFT_X + (i - 1) * GRID_SIZE[0])
        # 计算并添加 y 轴上每个网格的坐标
        for i in range(1, GRID_COUNT[1] + 1):
            GRID_Y.append(GRID_TOP_Y + (i - 1) * GRID_SIZE[1])
        
    def CheckInGarden(self, pos): 
        """
        检查给定坐标是否在花园种植区域内

        :param pos: 待检查的坐标，格式为 (x, y)
        :return: 如果坐标在花园内返回 True，否则返回 False
        """
        # 通过比较坐标与花园边界的关系判断是否在花园内
        return pos[0] > GRID_LEFT_X and pos[0] < GRID_RIGHT_X and pos[1] > GRID_TOP_Y and pos[1] < GRID_DOWN_Y

    def CheckPlant_Grid(self, plant_type): 
        """
        检查是否有足够金币种植指定类型的植物

        :param plant_type: 要种植的植物类型
        :return: 如果金币足够返回 True，否则返回 False
        """
        # 检查金币是否足够种植指定类型的植物
        if self.gold >= settings[plant_type]["gold"]:
            self.game.gridPlant.plantType = plant_type
            self.game.gridPlant.preIndexTimeNumber = settings["game"]["plantPreIndexTimeNumber"][plant_type]
            self.game.Plant.preIndexTimeNumber = settings["game"]["plantPreIndexTimeNumber"][plant_type]
            return True
        else:
            return False

    def CheckAddPlant(self, xy, plant_type): 
        """
        检查是否可以在指定位置种植指定类型的植物

        :param xy: 要种植植物的屏幕坐标
        :param plant_type: 要种植的植物类型
        :return: 包含种植结果和种植位置的字典
        """
        # 初始化种植标志为 True
        plant = True
        # 检查坐标是否在花园内
        if not self.CheckInGarden(xy):
            plant = False
            return {"plant": plant,
                    "pos": False
                   }
        # 获取坐标对应的网格位置
        grid = self.getGrid(xy)
        # 检查网格位置是否为空
        if self.map[grid[1]][grid[0]] == 0:
            # 若为空则记录种植的植物类型
            self.map[grid[1]][grid[0]] = plant_type
            # 扣除种植所需的金币
            self.gold -= settings[settings["plant_name"][plant_type]]["gold"]
            plant = True
            # 播放种植音乐
            self.plantMusic.play()
        else:
            plant = False
        return {"plant": plant,
                "pos": [GRID_X[grid[0]], GRID_Y[grid[1]]]
               }

    def getGrid(self, xy): 
        """
        将屏幕坐标转换为网格坐标，并确保坐标在有效范围内

        :param xy: 屏幕坐标，格式为 (x, y)
        :return: 对应的网格坐标，格式为 [col, row]
        """
        pos = list(xy)
        grid = [0, 0]
        # 计算相对于网格起始位置的偏移量
        pos[0] -= GRID_LEFT_X
        pos[0] /= GRID_SIZE[0]
        pos[1] -= GRID_TOP_Y
        pos[1] /= GRID_SIZE[1]
        # 向上取整得到网格坐标
        grid[0] = math.ceil(pos[0])
        grid[1] = math.ceil(pos[1])
        # 确保网格坐标在有效范围内
        grid[0] = max(1, min(grid[0], GRID_COUNT[0]))
        grid[1] = max(1, min(grid[1], GRID_COUNT[1]))
        return grid
    
    def run(self):
        """
        游戏主循环，负责游戏的运行和更新
        """
        self.draw()  # 绘制游戏界面
        if self.game.really:  # 判断游戏是否正式开始
            self.RunTimeDetermine()  # 处理游戏正式运行时的信息
            self.update()  # 更新游戏状态
        else:
            self.ChooseCardTimeDetermine()  # 处理选择卡片阶段的信息

    def draw(self): 
        """
        绘制游戏界面，包括铲子和铲子框
        """
        self.shovelFrame.run()  # 运行铲子框的绘制逻辑
        self.shovel.run()  # 运行铲子的绘制逻辑

    def update(self): 
        """
        更新游戏状态，包括僵尸和阳光的生成，以及鼠标操作处理
        """
        # 更新僵尸生成计时器
        self.zombieTime = (self.zombieTime + 1) % ZOMBIE_TIME
        # 更新阳光生成计时器
        self.sunlightTime = (self.sunlightTime + 1) % SUNLIGHT_TIME
        # 判断是否到了生成僵尸的时间
        if self.zombieTime == 0: 
            self.game.zombie_list.append(Zombie(self.game))
        # 判断是否到了生成阳光的时间
        if self.sunlightTime == 0: 
            self.game.sunlight_list.append(Sunlight(self.screen, (random.randint(GRID_LEFT_X, GRID_RIGHT_X), 0)))
        
        # 处理鼠标左键按下事件且铲子上次操作已完成的情况
        if pygame.mouse.get_pressed()[0] and not self.shovel.click: 
            if not self.shovel.use:
                # 判断是否点击了铲子
                if click(self.shovel.pos, self.shovel.size, pygame.mouse.get_pos()):
                    self.shovel.use = True
                    self.shovel.click = True
            else:
                # 判断铲子是否放回铲子框
                if collision_detection(self.shovel, self.shovelFrame):
                    self.shovel.use = False
                    self.shovel.click = True

        # 处理鼠标左键按下且铲子正在使用的情况
        if pygame.mouse.get_pressed()[0] and self.shovel.use:
            if self.CheckInGarden(pygame.mouse.get_pos()):
                grid = getGrid(pygame.mouse.get_pos())
                # 检查网格位置是否有植物
                if self.map[grid[1]][grid[0]] != 0:
                    # 移除豌豆射手
                    for peashooter in self.game.peashooter_list:
                        if peashooter.grid == grid:
                            self.map[peashooter.grid[1]][peashooter.grid[0]] = 0
                            self.game.peashooter_list.remove(peashooter)
                            break
                    # 移除向日葵
                    for sunflower in self.game.sunflower_list:
                        if sunflower.grid == grid:
                            self.map[sunflower.grid[1]][sunflower.grid[0]] = 0
                            self.game.sunflower_list.remove(sunflower)
                            break
                    # 移除坚果
                    for nut in self.game.nut_list:
                        if nut.grid == grid:
                            self.map[nut.grid[1]][nut.grid[0]] = 0
                            self.game.nut_list.remove(nut)
                            break
                    # 移除大嘴花
                    for chomper in self.game.chomper_list:
                        if chomper.grid == grid:
                            self.map[chomper.grid[1]][chomper.grid[0]] = 0
                            self.game.chomper_list.remove(chomper)
                            break
    
    def PlayZombieEatMusicDetermine(self): 
        """
        判断是否有僵尸在吃植物，并控制僵尸啃食音乐的播放
        """
        eat = False
        # 遍历僵尸列表，检查是否有僵尸在吃植物
        for zombie in self.game.zombie_list:
            if zombie.eat:
                eat = True
                break
        if eat:
            if not self.zombieMusicPlay:
                # 播放僵尸啃食音乐，循环播放
                self.zombieMusic.play(-1)
                self.zombieMusicPlay = True
        else:
            if self.zombieMusicPlay:
                # 停止播放僵尸啃食音乐
                self.zombieMusic.stop()
                self.zombieMusicPlay = False

    def ChooseCardTimeDetermine(self): 
        """
        处理选择卡片阶段的游戏信息，包括卡片点击和选择操作
        """
        # 判断是否点击了游戏开始按钮
        if not self.game.reallyButton.click:
            # 遍历显示的卡片列表
            for card in self.game.displayed_card:
                if click(card.pos, card.size, pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not card.use:
                        card.use = True
                        # 将选中的卡片添加到已选卡片列表
                        self.game.selectedCard.append(DisplayedSelectedCard(
                                                                                self.game.screen,
                                                                                card.name,
                                                                                len(self.game.selectedCard) + 1
                                                                            )
                                                    )
                        break
        
        # 判断是否点击了游戏开始按钮
        if not self.game.reallyButton.click:
            # 遍历已选卡片列表
            for card in self.game.selectedCard:
                if click(card.pos, card.size, pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not card.click:
                    for displayedCard in self.game.displayed_card:
                        if displayedCard.name == card.name:
                            deleteCardNumber = card.number
                            displayedCard.use = False
                            # 从已选卡片列表中移除卡片
                            self.game.selectedCard.remove(card)
                            # 调整剩余已选卡片的编号和位置
                            for selectedCard in self.game.selectedCard:
                                if selectedCard.number > deleteCardNumber:
                                    selectedCard.number -= 1
                                    selectedCard.pos[0] = CARD_FIRST_X + (CARD_SIZE[0] + 7) * (selectedCard.number - 1)
                                    selectedCard.click = True
                            break
    
    def CheckZombieIsnotEatPlant(self, zombie):
        """
        检查僵尸是否没有在吃植物

        :param zombie: 僵尸对象
        :return: 如果僵尸没有在吃植物返回 True，否则返回 False
        """
        return 1 <= zombie.grid[1] <= GRID_COUNT[1] and 1 <= zombie.grid[0] <= GRID_COUNT[0] and self.map[zombie.grid[1]][zombie.grid[0] - 1] == 0

    def RunTimeDetermine(self): 
        """
        处理游戏正式运行阶段的游戏信息，包括碰撞检测、植物和僵尸状态更新等
        """
        # 检测是否需要播放僵尸啃食音乐
        self.PlayZombieEatMusicDetermine() 

        # 处理豌豆与僵尸的碰撞
        for zombie in self.game.zombie_list: 
            if zombie.hp == 0:
                continue
            for pea in self.game.pea_list:
                if collision_Pea_add_Zombie_detection(zombie, pea):
                    # 移除被击中的豌豆
                    self.game.pea_list.remove(pea)
                    # 减少僵尸的生命值
                    zombie.hp -= 20
                    if zombie.hp <= 40 and zombie.head:
                        zombie.path = settings["zombie"]["headlessPath"]
                        zombie.imageCount = settings["zombie"]["headlessImageCount"]
                        # 添加僵尸头对象
                        self.game.zombieHead_list.append(ZombieHead(self.screen, (zombie.pos[0] + 30, zombie.pos[1])))
                        zombie.head = False
                    if zombie.hp <= 0:
                        zombie.hp = 0
                        zombie.imageIndex = 0
                        zombie.path = settings["zombie"]["deadPath"]
                        zombie.imageCount = settings["zombie"]["deadImageCount"]
                        flag = False
                        for Zombie in self.game.zombie_list:
                            if zombie.posY == Zombie.posY:
                                flag = True
                                break
                        if not flag:
                            self.game.zombiePos[zombie.posY] = False
        
        # 处理豌豆射手与僵尸的碰撞

        for zombie in self.game.zombie_list:
            if zombie.hp <= 40:
                if zombie.eat:
                    zombie.eat = False
                continue
            
            for peashooter in self.game.peashooter_list:

                # 修改后的调用
                if collision_Plant_and_Zombie_detection(peashooter, zombie, "peashooter"):
                    if not zombie.eat:
                        zombie.eat = True
                    # 增加豌豆射手的攻击次数
                    peashooter.hpTime += 1
                    if peashooter.hpTime == PLNAT_HP:
                        peashooter.hpTime = 0
                        # 减少豌豆射手的生命值
                        peashooter.hp -= 20
                        if peashooter.hp <= 0:
                            # 移除被吃掉的豌豆射手
                            self.map[peashooter.grid[1]][peashooter.grid[0]] = 0
                            self.game.peashooter_list.remove(peashooter)
                            zombie.eat = False
                else:
                    if self.CheckZombieIsnotEatPlant(zombie):
                        if zombie.eat:
                            zombie.eat = False

        
        # 处理坚果与僵尸的碰撞

        for zombie in self.game.zombie_list:
            if zombie.hp <= 40:
                if zombie.eat:
                    zombie.eat = False
                continue
            
            for nut in self.game.nut_list:

                # 修改后的调用
                if collision_Plant_and_Zombie_detection(nut, zombie, "nut"):
                    if not zombie.eat:
                        zombie.eat = True
                    # 增加坚果的攻击次数
                    nut.hpTime += 1
                    if nut.hpTime == NUT_HP:
                        nut.hpTime = 0
                        # 减少坚果的生命值
                        nut.hp -= NUT_HP / 4.0
                        if nut.hp == NUT_HP / 4.0 * 3:
                            if not nut.path == settings["nut"]["path2"]:
                                nut.path = settings["nut"]["path2"]
                                nut.imageCount = settings["nut"]["imageCount2"]
                        elif nut.hp == NUT_HP / 4.0 * 2:
                            if not nut.path == settings["nut"]["path3"]:
                                nut.path = settings["nut"]["path3"]
                                nut.imageCount = settings["nut"]["imageCount3"]
                        elif nut.hp == NUT_HP / 4.0:
                            # 移除被吃掉的坚果
                            self.map[nut.grid[1]][nut.grid[0]] = 0
                            self.game.nut_list.remove(nut)
                            zombie.eat = False
                else:
                    if self.CheckZombieIsnotEatPlant(zombie):
                        if zombie.eat:
                            zombie.eat = False
        
        # 处理向日葵与僵尸的碰撞

        for zombie in self.game.zombie_list:
            if zombie.hp <= 40:
                if zombie.eat:
                    zombie.eat = False
                continue
            
            for sunflower in self.game.sunflower_list:

                # 修改后的调用
                if collision_Plant_and_Zombie_detection(sunflower, zombie, "sunflower"):
                    if not zombie.eat:
                        zombie.eat = True
                    # 增加向日葵的攻击次数
                    sunflower.hpTime += 1
                    if sunflower.hpTime == PLNAT_HP:
                        sunflower.hpTime = 0
                        # 减少向日葵的生命值
                        sunflower.hp -= 20
                        if sunflower.hp <= 0:
                            # 移除被吃掉的向日葵
                            self.map[sunflower.grid[1]][sunflower.grid[0]] = 0
                            self.game.sunflower_list.remove(sunflower)
                            zombie.eat = False
                else:
                    if self.CheckZombieIsnotEatPlant(zombie):
                        if zombie.eat:
                            zombie.eat = False

        # 处理食人花与僵尸的碰撞(大嘴花吃僵尸)
        for chomper in self.game.chomper_list:
            if chomper.state == "Idle":  # 如果食人花未处于进食状态
                for zombie in self.game.zombie_list:
                    if collision_Plant_and_Zombie_detection(chomper, zombie, "chomper"):
                        chomper.ToEat(zombie) # 让食人花进入进食状态
                        break  # 跳出循环，避免重复处理
        
        # 处理食人花与僵尸的碰撞(僵尸咬食人花)
        for zombie in self.game.zombie_list:
            if zombie.hp <= 40:
                if zombie.eat:
                    zombie.eat = False
                continue
            for chomper in self.game.chomper_list:
                if chomper.state == "Eating":  # 如果食人花处于进食状态
                    if collision_Plant_and_Zombie_detection(zombie, chomper, "chomper"):
                        if not zombie.eat:
                            zombie.eat = True
                        # 增加食人花的攻击次数
                        chomper.hpTime += 1
                        if chomper.hpTime == PLNAT_HP:
                            chomper.hpTime = 0
                            # 减少食人花的生命值
                            chomper.hp -= 20
                            if chomper.hp <= 0:
                                # 移除被吃掉的食人花
                                self.map[chomper.grid[1]][chomper.grid[0]] = 0
                                self.game.chomper_list.remove(chomper)

        # 处理土豆地雷与僵尸的碰撞
        for potatoMine in self.game.potatoMine_list: 
            for zombie in self.game.zombie_list:
                if collision_Plant_and_Zombie_detection(potatoMine, zombie, "potato_mine"):
                    if zombie.posY == potatoMine.grid[1]:
                        if not potatoMine.Explode:
                            potatoMine.Explode = True
                            # 播放土豆地雷爆炸音乐
                            self.potatoMineExplodeMusic.play()
                            # 移除土豆地雷
                            self.map[potatoMine.grid[1]][potatoMine.grid[0]] = 0
                        if not zombie.path == settings["zombie"]["deadPath"]:
                            if zombie.hp > 40:
                                # 添加僵尸头对象
                                self.game.zombieHead_list.append(ZombieHead(self.screen, (zombie.pos[0] + 30, zombie.pos[1])))
                            zombie.hp = 0
                            zombie.imageIndex = 0
                            zombie.path = settings["zombie"]["deadPath"]
                            zombie.imageCount = settings["zombie"]["deadImageCount"]
                            flag = False
                            for Zombie in self.game.zombie_list:
                                if zombie.posY == Zombie.posY:
                                    flag = True
                                    break
                            if not flag:
                                self.game.zombiePos[zombie.posY] = False

        # 处理鼠标点击阳光事件
        if pygame.mouse.get_pressed()[0]: 
            for sunlight in self.game.sunlight_list:  
                if click(sunlight.pos, sunlight.size, pygame.mouse.get_pos()):  
                    # 播放阳光音乐
                    self.sunMusic.play()  
                    # 增加金币数量
                    self.gold += 25  
                    # 移除被点击的阳光
                    self.game.sunlight_list.remove(sunlight)  

        # 移除标记为删除的阳光
        for sunlight in self.game.sunlight_list: 
            if sunlight.delete:
                self.game.sunlight_list.remove(sunlight)