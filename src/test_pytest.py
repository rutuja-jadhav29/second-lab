from Todolist import ToDoList

def test_add_task():
    todo = ToDoList()
    todo.tasks = []
    msg = todo.add_task("Learn AWS")
    assert "added" in msg
    assert "Learn AWS" in todo.tasks

def test_remove_task():
    todo = ToDoList()
    todo.tasks = ["Learn SQL"]
    msg = todo.remove_task(1)
    assert "removed" in msg
    assert len(todo.tasks) == 0

def test_mark_task_completed():
    todo = ToDoList()
    todo.tasks = ["Practice Databricks"]
    msg = todo.mark_task_completed(1)
    assert "[Completed]" in todo.tasks[0]
