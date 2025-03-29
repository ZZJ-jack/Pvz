from data.src.PVZ import *  # 导入游戏类
from data.src.GameSet import *  # 导入游戏设置窗口类
import threading # 导入多线程

class Main:
    def __init__(self):
        self.game = Pvz()
        self.RunGame = threading.Thread(target = self.CreateGameInstance) # 创建多线程:游戏运行窗口
        self.RunGameSetWindow = threading.Thread(target = self.CreateGameSet) # 创建多线程:游戏设置窗口
    
    def run(self):        
        self.RunGame.start() # 启动游戏
        self.RunGameSetWindow.start() # 启动游戏设置窗口

    def CreateGameInstance(self): # 创建游戏实例
        # 开始游戏
        self.game.start(self.game)
        # 选择卡牌
        self.game.chooseCard()
        # 运行游戏
        self.game.run()
        # 保存游戏
        self.game.save()

    def CreateGameSet(self): # 创建游戏设置窗口
        self.GameSetWindow = GameSet(self.game)
        self.GameSetWindow.loginWindow.mainloop()
        self.GameSetWindow.SetWindow.mainloop() # 运行窗口

if __name__ == '__main__': # 主函数
    main = Main()
    main.run()