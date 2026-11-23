import os
import tempfile
import unittest
from tasks import add_task, total_minutes, complete_task, save_tasks, load_tasks


class TestTasks(unittest.TestCase):
    def test_add_task_success(self):
        tasks = []
        add_task(tasks, "Подготовить отчёт", 45)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Подготовить отчёт")
        self.assertEqual(tasks[0]["minutes"], 45)
        self.assertFalse(tasks[0]["done"])

    def test_add_task_invalid(self):
        tasks = []
        with self.assertRaises(ValueError):
            add_task(tasks, "   ", 30)
        with self.assertRaises(ValueError):
            add_task(tasks, "Задача", -10)

    def test_complete_and_total_minutes(self):
        tasks = []
        add_task(tasks, "Задача 1", 20)
        add_task(tasks, "Задача 2", 40)
        self.assertEqual(total_minutes(tasks, only_active=True), 60)

        complete_task(tasks, 0)
        self.assertEqual(total_minutes(tasks, only_active=True), 40)
        self.assertEqual(total_minutes(tasks, only_active=False), 60)

    def test_save_and_load_tasks(self):
        tasks = []
        add_task(tasks, "Тест JSON", 15)

        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test_tasks.json")
            save_tasks(tasks, filepath)
            loaded = load_tasks(filepath)
            self.assertEqual(loaded, tasks)


if __name__ == "__main__":
    unittest.main()