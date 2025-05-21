import flet as ft


def main(page: ft.Page):
    # タイトルの設定
    page.title = "sample 6"

    # appbar設定
    page.appbar = ft.AppBar(title=ft.Text("Viewテスト用サンプル"))

    # ウィンドウサイズの設定
    page.window.width = 600
    page.window.height = 400

    # View制御関連メソッドの定義
    def route_change(route: str):
        # 遷移先のrouteごとに処理を分岐
        # Note:　デフォルトで追加される最初のViewは残すこと
        if page.route == "/":
            # 最初のデフォルト生成Viewだけ残るように処理
            first_view = page.views[0]
            page.views.clear()
            page.views.append(first_view)
        elif page.route == "/form/1":
            page.views.append(view_form1)
        elif page.route == "/form/2":
            page.views.append(view_form2)
        elif page.route == "/finish":
            page.views.append(view_finish)
            # 値のセット
            text_field_check_1_1.value = text_field_1_1.value
            text_field_check_1_2.value = text_field_1_2.value
            text_field_check_2_1.value = text_field_2_1.value
            text_field_check_2_2.value = text_field_2_2.value

        page.update()

    def view_pop(view):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    #
    # トップページの内容
    #

    # ルート変更時・戻る際のロジックを設定
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.appbar = ft.AppBar(title=ft.Text("Viewテスト用サンプル"))
    button_top = ft.OutlinedButton(
        "入力へ進む", on_click=lambda _: page.go("/form/1"))
    page.add(button_top)

    #
    # Viewの内容
    #

    # View 1
    text_field_1_1 = ft.TextField(
        label="サンプル入力(1-1)", width=300)
    text_field_1_2 = ft.TextField(
        label="サンプル入力(1-2)", width=300)
    button_submit_1 = ft.OutlinedButton(
        "次へ", on_click=lambda _: page.go("/form/2"))

    # View 2
    text_field_2_1 = ft.TextField(
        label="サンプル入力(2-1)", width=300)
    text_field_2_2 = ft.TextField(
        label="サンプル入力(2-2)", width=300)
    button_submit_2 = ft.OutlinedButton(
        "次へ", on_click=lambda _: page.go("/finish"))

    # View Finish
    text_field_check_1_1 = ft.TextField(
        label="サンプル入力(2-1)", width=300, read_only=True)
    text_field_check_1_2 = ft.TextField(
        label="サンプル入力(2-2)", width=300, read_only=True)
    text_field_check_2_1 = ft.TextField(
        label="サンプル入力(2-1)", width=300, read_only=True)
    text_field_check_2_2 = ft.TextField(
        label="サンプル入力(2-2)", width=300, read_only=True)
    button_submit_finish = ft.OutlinedButton(
        "確認完了して最初に戻る", on_click=lambda _: page.go("/"))

    # Viewの定義
    view_form1 = ft.View(
        appbar=ft.AppBar(title=ft.Text("View 1")),
        controls=[
            ft.Row(controls=[ft.Text("サンプル1-1: "), text_field_1_1]),
            ft.Row(controls=[ft.Text("サンプル1-2: "), text_field_1_2]),
            ft.Row(controls=[button_submit_1]),
        ]
    )
    view_form2 = ft.View(
        appbar=ft.AppBar(title=ft.Text("View 2")),
        controls=[
            ft.Row(controls=[ft.Text("サンプル2-1: "), text_field_2_1]),
            ft.Row(controls=[ft.Text("サンプル2-2: "), text_field_2_2]),
            ft.Row(controls=[button_submit_2]),
        ]
    )
    view_finish = ft.View(
        appbar=ft.AppBar(title=ft.Text("View Finish")),
        controls=[
            ft.Row(controls=[
                ft.Text("サンプル1-1入力内容: "), text_field_check_1_1]),
            ft.Row(controls=[
                ft.Text("サンプル1-2入力内容: "), text_field_check_1_2]),
            ft.Row(controls=[
                ft.Text("サンプル2-1入力内容: "), text_field_check_2_1]),
            ft.Row(controls=[
                ft.Text("サンプル2-2入力内容: "), text_field_check_2_2]),
            ft.Row(controls=[button_submit_finish]),
        ]
    )


# main関数
if __name__ == "__main__":
    ft.app(target=main)
