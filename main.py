from data.src.PVZ import *  # 导入游戏类
from data.src.GameSet import *  # 导入游戏设置窗口类
import threading # 导入多线程

class Main: # 主函数
    def __init__(self):
        self.game = Pvz() # 创建游戏实例
        self.GameSetWindow = GameSet(self.game) # 创建游戏设置窗口
        self.RunGameSetWindow = threading.Thread(target = self.CreateGameSet) # 创建多线程:游戏设置窗口
        self.RunGame = threading.Thread(target = self.CreateGameInstance) # 创建多线程:游戏运行窗口
    
    def run(self):        
        self.RunGameSetWindow.start() # 启动游戏设置窗口
        self.RunGame.start() # 启动游戏
        self.GameSetWindow.StartLogin() # 启动登录窗口
        self.GameSetWindow.loginWindow.mainloop() # 运行登录窗口
        self.GameSetWindow.SetWindow.mainloop() # 运行窗口

    def CreateGameInstance(self): # 创建游戏实例
        self.game.start(self.game, self.GameSetWindow) # 开始游戏
        self.game.chooseCard() # 选择卡牌
        self.game.run() # 运行游戏
        self.game.save() # 保存游戏

    def CreateGameSet(self): # 创建游戏设置窗口
        pass

if __name__ == '__main__': # 如果是主程序
    main = Main() # 创建主函数
    main.run() # 运行主函数