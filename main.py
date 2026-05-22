import flet as ft

from db.main_db import (
    init_db,
    add_task,
    get_tasks,
    delete_task,
    update_task
)


def main(page: ft.Page):
    page.title = "Список покупок"

    init_db()

    task_input = ft.TextField(label="Новый товар", width=300)
    tasks_column = ft.Column()

    filter_type = "all"

    def load_tasks():
        tasks_column.controls.clear()

        tasks = get_tasks(filter_type)

        for task in tasks:
            task_id = task[0]
            task_name = task[1]
            completed = task[2]

            checkbox = ft.Checkbox(
                label=task_name,
                value=bool(completed),
                on_change=lambda e, tid=task_id: change_status(e, tid)
            )

            delete_btn = ft.TextButton(
    "Удалить",
    on_click=lambda e, tid=task_id: remove_task(tid)
)

            tasks_column.controls.append(
                ft.Row([checkbox, delete_btn])
            )

        page.update()

    def add_new_task(e):
        if task_input.value:
            add_task(task_input.value)
            task_input.value = ""
            load_tasks()

    def remove_task(task_id):
        delete_task(task_id)
        load_tasks()

    def change_status(e, task_id):
        update_task(task_id, int(e.control.value))
        load_tasks()

    def set_filter(e):
        nonlocal filter_type
        filter_type = e.control.data
        load_tasks()

    add_button = ft.ElevatedButton(
        "ADD",
        on_click=add_new_task
    )

    filter_row = ft.Row([
        ft.ElevatedButton("Все", data="all", on_click=set_filter),
        ft.ElevatedButton("Купленные", data="done", on_click=set_filter),
        ft.ElevatedButton("Не купленные", data="not_done", on_click=set_filter),
    ])

    page.add(
        ft.Text("Список покупок", size=30),

        ft.Row([task_input, add_button]),

        filter_row,

        tasks_column
    )

    load_tasks()


ft.app(target=main)