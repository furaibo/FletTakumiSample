import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        t.value =\
            f"Textboxes values are: "\
            f"'{tb1.value}', '{tb2.value}', '{tb3.value}', "\
            f"'{tb4.value}', '{tb5.value}'."
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="Disabled",
                       disabled=True, value="First name")
    tb3 = ft.TextField(label="Read-only",
                       read_only=True, value="Last name")
    tb4 = ft.TextField(label="With placeholder",
                       hint_text="Please enter text here")
    tb5 = ft.TextField(label="With an icon",
                       icon=ft.Icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)


ft.app(main)
