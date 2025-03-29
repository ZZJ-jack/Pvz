from data.src.const import *

# 定义一个字典，用于存储游戏中各种元素的属性
settings = {
                # 植物名称
                'plant_name': ['', 'sunflower', 'peashooter', 'nut', 'potato_mine'],
                # 植物卡片图片路径
                'plant_card_path': ['', 'data/image/PlantCard/Sunflower.png', 'data/image/PlantCard/Peashooter.png', 'data/image/PlantCard/Nut.png', 'data/image/PlantCard/PotatoMine.png'],
                # 游戏设置
                'game': {
                    'bgm':{
                        'startMusic': 'data/bgm/Crazy Dave.mp3',
                        'startMusicVolume': 0.4,
                        'gameMusic': 'data/bgm/Grasswalk.mp3',
                        'gameMusicVolume': 0.4,
                        'sunlight': 'data/bgm/Sun.mp3',
                        'sunVolume': 0.9,
                        'plant': 'data/bgm/Plant.mp3',
                        'plantVolume': 0.1,
                        'zombieEat': 'data/bgm/ZombieEat.mp3',
                        'zombieEatVolume': 0.1,
                        'potatoMineExplode': 'data/bgm/PotatoMineExplode.mp3',
                        'potatoMineExplodeVolume': 0.4,
                        'gameover': 'data/bgm/gameover.mp3',
                        'win': 'data/bgm/win.mp3',
                    },
                    'gridPlantPos':{
                        'sunflower': (10, 0),
                        'peashooter': (10, 0),
                        'nut': (10, 0),
                        'potato_mine': (8, 10),
                    },
                    'plantPreIndexTimeNumber':{
                        'sunflower': 0.1,
                        'peashooter': 0.1,
                        'nut': 0.1,
                        'potato_mine': 0.2,
                    }
                },
                # 阴影
                'shadow':{
                    'name': 'shadow',
                    'path': 'data/image/Other/shadow.png'
                },
                # 卡片选择框
                'ChooseCardFrame':{
                    'name': 'ChooseCardFrame',
                    'size': (470, 500),
                    'path': 'data/image/Other/ChooseCardFrame.png',
                    'pos': (90, 90),
                },
                # 定义豌豆射手
                'peashooter': {
                    'name': 'peashooter',  # 名称
                    'gold': 100,
                    'size': (60, 80),  # 大小
                    'path': 'data/image/Plant/Peashooter/Idle%d.png',  # 图片路径
                    'imageCount': 10,  # 图片数量
                    'shoot_path': 'data/image/Plant/Peashooter/Shoot%d.png',  # 射击图片路径
                    'shoot_imageCount': 8,  # 射击图片数量
                },
                # 定义向日葵
                'sunflower': {
                    'name': 'sunflower',
                    'gold': 50,
                    'size': (60, 80),
                    'path': 'data/image/Plant/Sunflower/Idle%d.png',
                    'imageCount': 12,
                    'shoot_path': 'data/image/Plant/Sunflower/Shoot%d.png',
                    'shoot_imageCount': 15,
                },
                # 定义坚果
                'nut': {
                    'name': 'nut',
                    'path': 'data/image/Plant/Nut/Nut-1 (%d).png',
                    'imageCount': 15,
                    'path1': 'data/image/Plant/Nut/Nut-1 (%d).png',
                    'imageCount1': 15,
                    'path2': 'data/image/Plant/Nut/Nut-2 (%d).png',
                    'imageCount2': 11,
                    'path3': 'data/image/Plant/Nut/Nut-3 (%d).png',
                    'imageCount3': 15,
                    'gold': 50,
                    'size': (60, 70)
                },
                # 定义土豆地雷
                'potato_mine': {
                    'name': 'potato_mine',
                    'gold': 25,
                    'size': (60, 60),
                    'growTime': 600,
                    'explodeTime': 20,
                    'initPath': 'data/image/Plant/PotatoMine/PotatoMineInit.png',
                    'initImageCount': 1,
                    'path': 'data/image/Plant/PotatoMine/PotatoMine (%d).png',
                    'imageCount': 8,
                    'explodePath': 'data/image/Plant/PotatoMine/PotatoMineExplode.png',
                    'explodeImageCount': 1,
                    'explodeSound': 'data/bgm/Explode.mp3',
                },
                # 定义僵尸
                'zombie': {
                    'name': 'zombie',
                    'hp': 100,
                    'size': (110, 110),
                    'path': 'data/image/Zombie/Zombie/Idle (%d).png',
                    'imageCount': 18,
                    'eatPath': 'data/image/Zombie/Zombie/Eat (%d).png',
                    'eatImageCount': 21,
                    'headlessPath': 'data/image/Zombie/Zombie/Headless (%d).png',
                    'headlessImageCount': 18,
                    'deadPath': 'data/image/Zombie/Zombie/die (%d).png',
                    'deadImageCount': 10,
                },
                # 定义僵尸头部
                'zombie_headless': {
                    'path': 'data/image/Zombie/Zombie-turn-around/(%d).png',
                    'imageCount': 12,
                    'size': (110, 110),
                },
                # 定义阳光
                'sunlight': {
                    'name': 'sun',
                    'path': 'data/image/Other/Sunlight/(%d).png',
                    'size': (60, 60),
                    'imageCount': 30,
                },
                # 定义卡片框
                'cardframe': {
                    'name': 'cardframe',
                    'path': 'data/image/Other/CardFrame.png',
                    'size': (540, 90),
                    'pos': (20, 0),
                },
                # 定义背景
                'background': {
                    'name': 'background',
                    'path': 'data/image/Other/background.png',
                    'pos': (0, -130),
                    'size': (1300, 800),
                },
                # 定义开始背景
                'startBackground': {
                    'name': 'startBackground',
                    'path': 'data/image/Other/Start-Background.png',
                    'size': (1200, 700),
                    'pos': (0, -50),
                },
                # 定义豌豆
                'pea': {
                    'name': 'pea',
                    'path': 'data/image/Other/Pea.png',
                    'size': (20, 20),
                },
                # 定义铲子
                'shovel': {
                    'name': 'shovel',
                    'path': 'data/image/Other/Shovel.png',
                    'size': (60, 70),
                },
                # 定义铲子框
                'shovelFrame': {
                    'name': 'shovelFrame',
                    'path': 'data/image/Other/ShovelFrame.png',
                    'pos': (560, 0),
                    'size': (70, 70),
                },
                # 定义游戏结束
                'gameover': {
                    'name': 'gameover',
                    'path': 'data/image/GameOver.png',
                    'size': (1200, 800),
                },
                # 定义开始按钮
                'startButton': {
                    'name': 'startButton',
                    'path': 'data/image/Other/Adventure_1.png',
                    'onPath': 'data/image/Other/Adventure_0.png',
                    'size': (350, 180),
                    'pos': (670, 50),
                },
                # 定义开始按钮
                'reallyButton': {
                    'name': 'startButton',
                    'path': 'data/image/Other/ReallyButton.png',
                    'size': (155, 35),
                    'pos': (247, 540),
                },
           }  