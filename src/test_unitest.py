import unittest
from Todolist import ToDoList

class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.todo = ToDoList()
        self.todo.tasks = []

    def test_add_task(self):
        msg = self.todo.add_task("Learn Python")
        self.assertIn("added", msg)
        self.assertIn("Learn Python", self.todo.tasks)

    def test_remove_task(self):
        self.todo.tasks = ["Learn Power BI"]
        msg = self.todo.remove_task(1)
        self.assertIn("removed", msg)
        self.assertEqual(len(self.todo.tasks), 0)

    def test_mark_task_completed(self):
        self.todo.tasks = ["Explore AWS Glue"]
        msg = self.todo.mark_task_completed(1)
        self.assertIn("[Completed]", self.todo.tasks[0])

if __name__ == "__main__":
    unittest.main()
