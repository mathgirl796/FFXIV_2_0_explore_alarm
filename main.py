import cal
import tkinter as tk
import tkinter.messagebox
import webbrowser

class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = tk.StringVar()
        self.lb = tk.Label(self, textvariable=self.text)
        self.link1 = tk.Button(self, text="视频攻略01-20", 
                    command=lambda: webbrowser.open("https://www.bilibili.com/video/BV1Z5411U7MR", new=0))
        self.link2 = tk.Button(self, text="视频攻略21-80",
                    command=lambda: webbrowser.open("https://www.bilibili.com/video/BV1Q44y137Ec", new=0))
        self.lb2 = tk.Label(self, text="made by 伊修加德-杏奈")
        
        self.lb.pack()
        self.link1.pack(side='left')
        self.link2.pack(side='right')
        self.lb2.pack()
        self.refresh()
        self.attributes('-topmost', True)
        self.title("FFXIV2.0探索笔记时钟")
        self.mainloop()

    def refresh(self):
        self.text.set(cal.cal.init())
        self.after(1000, self.refresh)

UI()