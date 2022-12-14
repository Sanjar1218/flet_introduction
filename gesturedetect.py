import flet as ft


def main(page: ft.Page):

    def on_pan_update(e: ft.DragUpdateEvent):
        print(e.data)
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        on_vertical_drag_update=on_pan_update,
        left=100,
        top=100,
        content=ft.Container(bgcolor=ft.colors.BLUE,
                             width=50,
                             height=50,
                             border_radius=5),
    )

    page.add(ft.Stack([gd], expand=True))


ft.app(target=main)