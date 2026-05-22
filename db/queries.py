create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0
);
"""
insert_task = '''
INSERT INTO tasks (task)
VALUES (?)
'''

select_tasks = '''
SELECT id, task, completed
FROM tasks
'''

select_tasks_completed = '''
SELECT id, task, completed
FROM tasks
WHERE completed = 1
'''

select_tasks_uncompleted = '''
SELECT id, task, completed
FROM tasks
WHERE completed = 0
'''


update_task = '''
UPDATE tasks
SET completed = ?
WHERE id = ?
'''

delete_task = '''
DELETE FROM tasks
WHERE id = ?
'''