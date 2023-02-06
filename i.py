import flet as ft
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

    txt_name = ft.TextField(label="你的启动器路径")

    page.add(txt_name, ft.ElevatedButton("启动游戏", on_click=btn_click))

ft.app(target=main)