import flet as ft
from time import sleep


def main(page: ft.Page):
    # タイトルの設定
    page.title = "sample 3"

    # ウィンドウサイズの設定
    page.window.width = 800
    page.window.height = 500

    # イベントの定義
    def event_click_counter_minus():
        value = int(text_field_counter.value)
        text_field_counter.value = str(value - 1)
        text_field_counter.update()

    def event_click_counter_plus():
        value = int(text_field_counter.value)
        text_field_counter.value = str(value + 1)
        text_field_counter.update()

    # さまざまなテキストフィールドの定義
    text_field_sample1 = ft.TextField(label="サンプルテキストフィールド(1)", width=300)
    text_field_sample2 = ft.TextField(label="サンプルテキストフィールド(2)", width=300,
                                      multiline=True, min_lines=5)

    # さまざまなボタンの定義
    button_sample1 = ft.CupertinoButton("サンプルボタン(1)")
    button_sample2 = ft.CupertinoFilledButton("サンプルボタン(2)")
    button_sample3 = ft.ElevatedButton("サンプルボタン(3)")
    button_sample4 = ft.FilledButton("サンプルボタン(4)")
    button_sample5 = ft.OutlinedButton("サンプルボタン(5)")

    # カウンターの定義
    text_field_counter = ft.TextField(label="カウンター", width=100, read_only=True, value="0")
    button_counter_minus = ft.IconButton(ft.Icons.REMOVE, on_click=lambda _: event_click_counter_minus())
    button_counter_plus = ft.IconButton(ft.Icons.ADD, on_click=lambda _: event_click_counter_plus())

    # ラジオボタンの定義
    radio_button_sample = ft.RadioGroup(ft.Row([
        ft.Radio(value="1", label="属性1"),
        ft.Radio(value="2", label="属性2"),
        ft.Radio(value="3", label="属性3"),
    ]))
    radio_button_sample.value = "1"  # 属性1がデフォルトの状態に設定

    # ドロップダウンメニューの定義
    # Note: このサンプルでは新しいバージョンの"DropdownM2"を利用
    dropdown_sample = ft.DropdownM2(
        border=ft.InputBorder.UNDERLINE,
        label="ドロップダウンメニューサンプル",
        width=400,
        options=[
            ft.dropdownm2.Option(key="Option1"),
            ft.dropdownm2.Option(key="Option2"),
            ft.dropdownm2.Option(key="Option3"),
            ft.dropdownm2.Option(key="Option4")
        ],
    )

    # プログレスバーの定義
    progress_bar_text = ft.Text("Progress bar sample")
    progress_bar_sample = ft.ProgressBar(width=400)

    # Rowの定義とPageへの追加
    rows_list = [
        ft.Row(controls=[text_field_sample1, text_field_sample2]),
        ft.Row(controls=[button_sample1, button_sample2,
                         button_sample3, button_sample4, button_sample5]),
        ft.Row(controls=[button_counter_minus, text_field_counter, button_counter_plus]),
        ft.Row(controls=[radio_button_sample]),
        ft.Row(controls=[dropdown_sample]),
        ft.Row(controls=[progress_bar_text]),
        ft.Row(controls=[progress_bar_sample]),
    ]
    for row in rows_list:
        page.add(row)

    # プログレスバー表示の更新
    # Note: 時間経過でバーを進め、100%になると最初に戻る
    count = 0
    while True:
        progress_bar_sample.value = count / 100
        progress_bar_sample.update()
        sleep(0.1)
        count += 1
        count %= 100


# main関数
if __name__ == "__main__":
    ft.app(target=main)
