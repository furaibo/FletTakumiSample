import flet as ft


def main(page: ft.Page):
    # タイトルの設定
    page.title = "sample 2"

    # ウィンドウサイズの設定
    page.window.width = 1200
    page.window.height = 900
    page.window.min_width = 800
    page.window.min_height = 600

    # テキストの追加
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()


# main関数
if __name__ == "__main__":
    ft.app(target=main)
