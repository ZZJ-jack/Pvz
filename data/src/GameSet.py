import tkinter as tk  # 导入tkinter模块
from tkinter import messagebox  # 引入弹窗库
from tkinter.font import Font # 导入字体库
from data.src.const import *  # 导入常量文件
from data.src.settings import *  # 导入设置文件
import json # 导入json库
import os # 导入os库

class GameSet: # 游戏设置类
    def NotClose(self): 
        pass # 禁止关闭窗口

    def CloseSet(self):
        self.SetWindow.destroy()

    def __init__(self, game):
        self.game = game # 保存游戏实例

        self.loginWindow = tk.Tk() # 创建一个窗口
        self.loginWindow.title("Pvz游戏后台设置-登录") # 设置窗口标题
        self.loginWindow.geometry(f"{GAME_SET_WINDOW_SIZE[0]}x{GAME_SET_WINDOW_SIZE[1]}") # 设置窗口大小
        self.loginWindow.resizable(False, False) # 设置窗口大小不可变
        self.loginWindow.protocol("WM_DELETE_WINDOW", self.NotClose) # 设置窗口关闭事件
        self.loginWindow.iconbitmap(ICON_PATH) # 设置窗口图标

        self.SetWindow = tk.Tk() # 创建一个窗口
        self.SetWindow.title("Pvz游戏后台设置") # 设置窗口标题
        self.SetWindow.geometry(f"{GAME_SET_WINDOW_SIZE[0]}x{GAME_SET_WINDOW_SIZE[1]}")
        self.SetWindow.resizable(False, False) # 设置窗口大小不可变
        self.SetWindow.protocol("WM_DELETE_WINDOW", self.NotClose) # 设置窗口关闭事件
        self.SetWindow.iconbitmap(ICON_PATH) # 设置窗口图标

        self.SetWindow.withdraw() # 隐藏窗口
    
    def StartLogin(self):
        self.UserLogin() # 登录界面
    
    def UserLogin(self):
        tk.Label(self.loginWindow, text = "欢迎来到Pvz游戏后台设置系统", font = Font(size = 23, family = "宋体")).place(x = 90, y = 50)
        self.inputUser = tk.Entry(self.loginWindow, width = 30)
        self.inputPassword = tk.Entry(self.loginWindow, width = 30, show = "*")
        self.UserLable = tk.Label(self.loginWindow, text = "用户名：")
        self.PasswordLable = tk.Label(self.loginWindow, text = "密码：")
        self.loginButton = tk.Button(self.loginWindow, text = "登录", font = Font(size = 10), command = self.login, width = 10, height = 2)
        self.GuestLoginButton = tk.Button(self.loginWindow, text = "游客登录", font = Font(size = 10), command = self.InputGuestUsrPwd, width = 10, height = 2)

        self.inputUser.place(x = 210, y = 200)
        self.inputPassword.place(x = 210, y = 250)
        self.UserLable.place(x = 150, y = 200)
        self.PasswordLable.place(x = 150, y = 250)
        self.loginButton.place(x = 200, y = 300)
        self.GuestLoginButton.place(x = 330, y = 298)

    def login(self):
        login = False # 登录状态
        username = self.inputUser.get()
        password = self.inputPassword.get()
        with open(USER_PATH, "r") as pwd:
            self.user_pwd = json.load(pwd)
            for index in (1, self.user_pwd["number"]):
                if self.user_pwd[f"{index}"]["name"] == username and self.user_pwd[f"{index}"]["password"] == password:
                    self.User = username
                    self.Pwd = password
                    self.loginWindow.destroy()
                    login = True
                    break
        if username == "":
            messagebox.showerror("错误", "请输入用户名")
        if password == "":
            messagebox.showerror("错误", "请输入密码")
        if username == "" and password == "":
            messagebox.showerror("错误", "请输入用户名和密码")

        if username == "guest" and password == "guest":
            self.User = username
            self.Pwd = password
            self.loginWindow.destroy()
            login = True
            self.GuestSet()
        elif login:
            self.UserSet()
        elif not login:
            messagebox.showerror("错误", "用户名或密码错误")
    
    def UserSet(self):
        self.SetWindow.deiconify()

        self.SetGoldInput = tk.Entry(self.SetWindow, width = 30)
        self.SetGoldLable = tk.Label(self.SetWindow, text = "金币：")
        self.SetGoldButton = tk.Button(self.SetWindow, text = "设置", command = self.SetGold, width = 5, height = 1)
        self.UserLable = tk.Label(self.SetWindow, text = f"用户：{self.User}")
        self.GoOutButton = tk.Button(self.SetWindow, text = "退出", command = self.CloseSet, width = 7, height = 1)
        self.SetWindowTopButton = tk.Button(self.SetWindow, text = "窗口置顶", command = self.game.SetWindowAtTheTop, width = 7, height = 1)
        self.CancelWindowTopButton = tk.Button(self.SetWindow, text = "取消置顶", command = self.game.CancelWindowAtTheTop, width = 7, height = 1)

        self.SetGoldLable.place(x = 50, y = 20)
        self.SetGoldInput.place(x = 110, y = 20)
        self.SetGoldButton.place(x = 330, y = 17)
        self.UserLable.place(x = 500, y = 10)
        self.GoOutButton.place(x = 500, y = 30)
        self.SetWindowTopButton.place(x = 400, y = 17)
        self.CancelWindowTopButton.place(x = 400, y = 47)

    def GuestSet(self):
        self.SetWindow.deiconify()

        self.UserLable = tk.Label(self.SetWindow, text = f"用户：{self.User}")
        self.GoOutButton = tk.Button(self.SetWindow, text = "退出", command = self.CloseSet, width = 7, height = 1)
        self.SetWindowTopButton = tk.Button(self.SetWindow, text = "窗口置顶", command = self.game.SetWindowAtTheTop, width = 7, height = 1)
        self.CancelWindowTopButton = tk.Button(self.SetWindow, text = "取消置顶", command = self.game.CancelWindowAtTheTop, width = 7, height = 1)

        self.UserLable.place(x = 500, y = 10)
        self.GoOutButton.place(x = 500, y = 30)
        self.SetWindowTopButton.place(x = 50, y = 17)
        self.CancelWindowTopButton.place(x = 50, y = 47)
    
    def InputGuestUsrPwd(self):
        self.inputUser.delete(0, tk.END)
        self.inputPassword.delete(0, tk.END)
        self.inputUser.insert(0, "guest")
        self.inputPassword.insert(0, "guest")

    def SetGold(self):
        gold = self.SetGoldInput.get()
        if self.game.running:
            if gold == "":
                messagebox.showerror("错误", "请输入金币")
            else:
                if gold.isdigit():
                    gold = int(gold)
                    if gold <= 9999:
                        if gold >= 0:
                            self.game.game.gold = gold
                            messagebox.showinfo("成功", "设置成功")
                        else:
                            messagebox.showerror("错误", "请输入正整数")
                    else:
                        messagebox.showerror("错误", "请输入4位数")
                else:
                    messagebox.showerror("错误", "请输入数字")
            self.SetGoldInput.delete(0, tk.END)
        else:
            messagebox.showerror("错误", "请先开始游戏")

    def Warning(self, title, message):
        # 创建自定义警告窗口而不是使用messagebox.showwarning
        warning_window = tk.Toplevel(self.loginWindow if self.loginWindow.winfo_exists() else self.SetWindow)
        warning_window.title(title)
        warning_window.geometry("300x120")
        warning_window.resizable(False, False)
        warning_window.transient(self.loginWindow if self.loginWindow.winfo_exists() else self.SetWindow)
        warning_window.grab_set()
        
        # 设置窗口内容
        tk.Label(warning_window, text=message, font=("宋体", 12), wraplength=280).pack(pady=20)
        tk.Button(warning_window, text="确定", command=warning_window.destroy, width=10).pack(pady=10)
        
        # 将窗口居中显示
        warning_window.update_idletasks()
        x = (warning_window.winfo_screenwidth() - warning_window.winfo_width()) // 2
        y = (warning_window.winfo_screenheight() - warning_window.winfo_height()) // 2
        warning_window.geometry(f"+{x}+{y}")
        
        # 等待窗口关闭
        warning_window.wait_window()
    
    def Info(self, title, message):
        # 创建自定义信息窗口而不是使用messagebox.showinfo
        info_window = tk.Toplevel(self.loginWindow if self.loginWindow.winfo_exists() else self.SetWindow)
        info_window.title(title)
        info_window.geometry("300x120")
        info_window.resizable(False, False)
        info_window.transient(self.loginWindow if self.loginWindow.winfo_exists() else self.SetWindow)
        info_window.grab_set()
        
        # 设置窗口内容
        tk.Label(info_window, text=message, font=("宋体", 12), wraplength=280).pack(pady=20)
        tk.Button(info_window, text="确定", command=info_window.destroy, width=10).pack(pady=10)
        
        # 将窗口居中显示
        info_window.update_idletasks()
        x = (info_window.winfo_screenwidth() - info_window.winfo_width()) // 2
        y = (info_window.winfo_screenheight() - info_window.winfo_height()) // 2
        info_window.geometry(f"+{x}+{y}")
        
        # 等待窗口关闭
        info_window.wait_window()

    def Error(self, title, message):
        # 创建自定义错误窗口而不是使用messagebox.showerror
        error_window = tk.Toplevel(self.loginWindow if self.loginWindow.winfo_exists() else self.SetWindow)
        error_window.title(title)
        error_window.geometry("300x120")
        error_window.resizable(False, False)
        error_window.transient(self.loginWindow if self.loginWindow.winfo_exists() else self.SetWindow)
        error_window.grab_set()
        
        # 设置窗口内容
        tk.Label(error_window, text=message, font=("宋体", 12), wraplength=280).pack(pady=20)
        tk.Button(error_window, text="确定", command=error_window.destroy, width=10).pack(pady=10)
        
        # 将窗口居中显示
        error_window.update_idletasks()
        x = (error_window.winfo_screenwidth() - error_window.winfo_width()) // 2
        y = (error_window.winfo_screenheight() - error_window.winfo_height()) // 2
        error_window.geometry(f"+{x}+{y}")
        
        # 等待窗口关闭
        error_window.wait_window()