import flet as ft
import webbrowser
import requests
import random
import os

def main(page):
    try:
        news = requests.get("http://low-webing-newsapi.mc-m.net/")
    except:
        news = '网络错误'
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
    t = ft.Text(value=str(news), color="green")
    page.controls.append(t)
ft.app(target=main,port=random.randint(8255,9000))