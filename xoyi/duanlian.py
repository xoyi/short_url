# -*- coding: UTF-8 -*-

import requests
import json
import win32clipboard
from Tkinter import *

def input():
    urls = user.get()
    return urls

def make():
    url = 'http://dwz.cn/create.php'
    data = {
        'url': input(),
        'access_type': 'web'
    }
    comment = requests.post(url=url,data=data).content
    con = json.loads(comment)
    status = con["status"]
    if status == 0:
        var1.set(con["tinyurl"])
    else:
        var1.set(con["err_msg"])

def send_to_clibboard():
    b = var1.get()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_TEXT,str(b))
    win32clipboard.CloseClipboard()

def center_window(w=300, h=200):
    ws = box.winfo_screenwidth()
    hs = box.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    box.geometry('%dx%d+%d+%d' % (w, h, x, y))
if __name__ == '__main__':
    box = Tk()
    center_window(500, 300)
    box.geometry('570x80')
    box.title('短链接生成器')
    lable = Label(box,text='输入地址:').place(x=3)
    user = Entry(box,borderwidth=1,width=60)
    # var = StringVar(box)
    # labl = Label(box,textvariable=var).grid()
    user.place(x=60,y=0)

    lable1 = Label(box,text='生成链接:').place(x=3,y=50)
    var1 = StringVar(box,'点击"复制"按钮会将此命令码复制到系统剪切板中去')
    lab = Entry(box, textvariable=var1,width=60,stat=DISABLED).place(x=60,y=50)
    buton = Button(box,text='开始',width=10,command=make).place(x=487)
    buton2 = Button(box,text='复制',width=10,command=send_to_clibboard).place(x=487,y=50)
    box.mainloop()








