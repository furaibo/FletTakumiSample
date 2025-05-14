import flet as ft


def main(page: ft.Page):
    # タイトルの設定
    page.title = "sample 1"

    # ウィンドウサイズの設定
    page.window.width = 300
    page.window.height = 200
    page.window.min_width = 200
    page.window.min_height = 100

    # テキストの追加
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()


# main関数
if __name__ == "__main__":
    ft.app(target=main)
