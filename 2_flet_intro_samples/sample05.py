import flet as ft


def main(page: ft.Page):
    # タイトルの設定
    page.title = "sample 5"

    # イベント用メソッドの定義
    # ファイル保存ダイアログ用のイベント
    def event_save_file_dialog(e: ft.FilePickerResultEvent):
        if e.path:
            # 指定パスの取得
            save_file_path = e.path

            # ファイルパスの反映
            # Note: 値の変更をUI上で反映するには "update" メソッドの実行が必要
            text_field_save_file_path.value = save_file_path
            text_field_save_file_path.update()

            # サンプルファイルの保存処理
            with open(save_file_path, "w", encoding="utf-8") as f:
                f.write("sample")

            # 処理完了後のアラートダイアログ表示
            dialog = ft.AlertDialog(
                content=ft.Text("ファイル保存が完了しました"),
                actions=[ft.TextButton("OK", on_click=lambda _: page.close(dialog))],
            )
            page.open(dialog)
        else:
            print("ファイル保存がキャンセルされました")

    # ファイル読込ダイアログ用のイベント
    def event_load_file_dialog(e: ft.FilePickerResultEvent):
        if e.files:
            # 指定パスからのファイル読込処理および出力テスト
            # Note: ファイルが1つのみでも "e.files" にリストとして格納される
            load_file_path = e.files[0].path
            print(load_file_path)

            # ファイルパスの反映
            # Note: 値の変更をUI上で反映するには "update" メソッドの実行が必要
            text_field_load_file_path.value = load_file_path
            text_field_load_file_path.update()

            # 保存完了のダイアログ表示
            dialog = ft.AlertDialog(
                content=ft.Text("ファイル読込が完了しました"),
                actions=[ft.TextButton("OK", on_click=lambda _: page.close(dialog)),],
            )
            page.open(dialog)
        else:
            print("ファイル読込がキャンセルされました")

    # FilePicker定義
    # Note: on_resultには上で定義したイベント用メソッドを指定
    save_file_dialog = ft.FilePicker(on_result=event_save_file_dialog)
    load_file_dialog = ft.FilePicker(on_result=event_load_file_dialog)

    # FilePickerのpageオーバレイへの追加
    # Note: この部分を忘れると、エラー出現するので注意
    page.overlay.append(save_file_dialog)
    page.overlay.append(load_file_dialog)

    # テキストおよびテキストフィールドの定義
    text_save_dialog = ft.Text(value="ファイル保存: ")
    text_load_dialog = ft.Text(value="ファイル読込: ")
    text_field_save_file_path = ft.TextField(label="保存ファイルパス", width=500, read_only=True)
    text_field_load_file_path = ft.TextField(label="読込ファイルパス", width=500, read_only=True)

    # ボタンの定義
    # Note: FilePickerでのon_clickのメソッド指定はlambda式を利用
    button_save_dialog = ft.ElevatedButton("保存の実行",
                               on_click=lambda _: save_file_dialog.save_file(
                                   "ファイル保存", allowed_extensions=["txt"]))
    button_load_dialog = ft.ElevatedButton("読込の実行",
                               on_click=lambda _: load_file_dialog.pick_files(
                                   "ファイル読込", allow_multiple=False))

    # Rowの定義とPageへの追加
    first_row = ft.Row(controls=[text_save_dialog, button_save_dialog, text_field_save_file_path])
    second_row = ft.Row(controls=[text_load_dialog, button_load_dialog, text_field_load_file_path])
    page.add(first_row)
    page.add(second_row)


# main関数
if __name__ == "__main__":
    ft.app(target=main)
