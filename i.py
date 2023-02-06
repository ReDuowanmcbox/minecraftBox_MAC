import flet as ft
import webbrowser
import random
import os

def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "请输入您的启动器路径"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            os.system(name)
    def goStory():
        webbrowser.open('http://golink.mc-m.net/story')
    txt_name = ft.TextField(label="你的启动器路径")

    page.add(txt_name, ft.ElevatedButton("启动游戏", on_click=btn_click))
    page.add(txt_name, ft.ElevatedButton("我的世界:故事模式", on_click=goStory))
ft.app(target=main,port=random.randint(8255,9000))