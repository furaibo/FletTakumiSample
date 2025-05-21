import flet as ft


def main(page: ft.Page):
    # タイトルの設定
    page.title = "sample 2"

    # ウィンドウサイズの設定
    page.window.width = 500
    page.window.height = 300

    # イベント用メソッドの定義
    # Note: チェックボックスを追加するイベントとして定義
    def add_clicked(e):
        page.add(ft.Checkbox(label=text_field_sample.value))
        text_field_sample.value = ""

    # テキストおよびテキストフィールドの定義
    text_sample = ft.Text(
        value="Input here!", color="green")
    text_field_sample = ft.TextField(
        hint_text="入力してみましょう", width=300)
    button_add_sample = ft.ElevatedButton(
        "追加", on_click=add_clicked)

    # Rowの定義とPageへの追加
    first_row = ft.Row([
        text_sample, text_field_sample, button_add_sample])
    page.add(first_row)


# main関数
if __name__ == "__main__":
    ft.app(target=main)
