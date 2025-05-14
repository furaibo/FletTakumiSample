import flet as ft


def main(page: ft.Page):
    # タイトルの設定
    page.title = "sample 5"

    # ウィンドウサイズの設定
    page.window.width = 400
    page.window.height = 300

    # タブ用コンテンツの定義
    # Note: ft.Dividerを使って表示位置調整を実施
    tab_contents_list = []
    for i in range(3):
        tab_contents = ft.Column(
            controls=[
                ft.Row(controls=[ft.Divider(height=10)]),
                ft.Row(controls=[ft.Text(f"タブサンプル{i+1}", size=16, color=ft.Colors.RED)]),
                ft.Row(controls=[ft.Divider(height=3)]),
                ft.Row(controls=[ft.Text(f"タブ{i+1} - コンテンツ1")]),
                ft.Row(controls=[ft.Divider(height=3)]),
                ft.Row(controls=[ft.Text(f"タブ{i+1} - コンテンツ2")])
            ])
        tab_contents_list.append(tab_contents)

    # タブの定義
    tab1 = ft.Tab(text="タブ1", icon=ft.Icons.HOME, content=tab_contents_list[0])
    tab2 = ft.Tab(text="タブ2", icon=ft.Icons.INFO, content=tab_contents_list[1])
    tab3 = ft.Tab(text="タブ3", icon=ft.Icons.STAR, content=tab_contents_list[2])

    # pageへのタブ追加
    page_tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[tab1, tab2, tab3],
        expand=1
    )
    page.add(page_tabs)


# main関数
if __name__ == "__main__":
    ft.app(target=main)
