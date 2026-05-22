import sqlite3
from config import path_db
from db import queries


def init_db():
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.create_tasks_table)


def add_task(task):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.insert_task, (task,))


def get_tasks(filter_type="all"):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.select_tasks)
        tasks = cursor.fetchall()

    if filter_type == "done":
        return [t for t in tasks if t[2] == 1]
    elif filter_type == "not_done":
        return [t for t in tasks if t[2] == 0]

    return tasks


def delete_task(task_id):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.delete_task, (task_id,))


def update_task(task_id, completed):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.update_task, (completed, task_id))