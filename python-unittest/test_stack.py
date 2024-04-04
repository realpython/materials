import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.items, [1])

    def test_pop(self):
        self.stack.push(2)
        item = self.stack.pop()
        self.assertEqual(item, 2)

    def test_len(self):
        self.stack.push(3)
        self.stack.push(4)
        self.assertEqual(len(self.stack), 2)

    def test_iter(self):
        items = [5, 6, 7]
        for item in items:
            self.stack.push(item)
        for stack_item, test_item in zip(self.stack, items):
            self.assertEqual(stack_item, test_item)

    def test_reversed(self):
        items = [5, 6, 7]
        for item in items:
            self.stack.push(item)
        reversed_stack = reversed(self.stack)
        self.assertEqual(list(reversed_stack), [7, 6, 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
