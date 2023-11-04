import unittest
import db_controller as controller
import os
import csv


class TestDBController(unittest.TestCase):
    def setUp(self):
        """
        - Invoked before the execution of each test method
        - Setup resources / state needed for tests
        - Works just like beforeEach in Jest
        """
        self.db_name = "test_db.csv"
        controller.DB_NAME = self.db_name

        self.test_todo_dict = {"id": 0, "msg": "test todo message", "complete": False}

        # Create a new CSV file
        with open(self.db_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(controller.HEADERS)
            writer.writerow(list(self.test_todo_dict.values()))

    def tearDown(self):
        """
        - Invoked immediately after each test method
        - Clean up any resources / state created by setUp
        - Works just like afterEach in Jest
        """
        # If the db exists (.txt file), remove it
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_create_db_if_not_exists(self):
        # ARRANGE -- Define testing environments & values
        # If the DB already exists, remove it (so that can test function)
        os.remove(self.db_name)
        self.assertFalse(os.path.exists(self.db_name))

        # ACT -- Run the code that is being tested
        controller.create_db_if_not_exists()

        # ASSERT -- Evaluate result and compare to expected value
        self.assertTrue(os.path.exists(self.db_name))

    def test_get_todos(self):
        # ARRANGE -- Define testing environments & values
        # ACT -- Run the code that is being tested
        todos = controller.get_todos()

        # ASSERT -- Evaluate result and compare to expected value
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0], self.test_todo_dict)

    def test_get_todo_by_id(self):
        # ARRANGE -- Define testing environments & values
        id = 0

        # ACT -- Run the code that is being tested
        todo = controller.get_todo_by_id(id)

        # ASSERT -- Evaluate result and compare to expected value
        self.assertEqual(todo, self.test_todo_dict)
        self.assertIsNone(controller.get_todo_by_id(1))

    def test_add_todo(self):
        # ARRANGE -- Define testing environments & values
        todo_msg = "New Todo"

        # ACT -- Run the code that is being tested
        added = controller.add_todo(todo_msg)
        todos = controller.get_todos()

        # ASSERT -- Evaluate result and compare to expected value
        self.assertTrue(added)
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[1], {"id": 1, "msg": todo_msg, "complete": False})

    def test_update_todo(self):
        # ARRANGE -- Define testing environments & values
        id = 0
        updated_msg = "Updated Todo"
        updated_complete = True

        # ACT -- Run the code that is being tested
        updated = controller.update_todo(id, updated_msg, updated_complete)
        updated_todo = controller.get_todo_by_id(id)

        # ASSERT -- Evaluate result and compare to expected value
        self.assertEqual(
            updated_todo, {"id": id, "msg": updated_msg, "complete": updated_complete}
        )
        # self.assertTrue(updated)
        # self.assertFalse(controller.update_todo(2, "Nonexistent Todo"))

    def test_toggle_complete(self):
        # ARRANGE -- Define testing environments & values
        id = 0
        todo = controller.get_todo_by_id(id)

        # ACT + ASSERT -- Run the code that is being tested, Evaluate result and compare to expected value
        toggled = controller.toggle_complete(id)
        self.assertTrue(toggled)

        toggled2 = controller.toggle_complete(id)
        self.assertFalse(toggled2)

        toggled3 = controller.toggle_complete(id)
        self.assertTrue(toggled3)

    def test_delete_todo(self):
        # ARRANGE -- Define testing environments & values
        count_before_delete = controller._get_todos_count()

        # ACT -- Run the code that is being tested
        deleted = controller.delete_todo(0)
        todos = controller.get_todos()

        # ASSERT -- Evaluate result and compare to expected value
        self.assertTrue(deleted)
        self.assertEqual(len(todos), 0)


if __name__ == "__main__":
    unittest.main()
