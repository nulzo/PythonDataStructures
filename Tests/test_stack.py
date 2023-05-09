import unittest
from DataStructures.stack_structure import Stack

class TestStackMethods(unittest.TestCase):
    def test_instantiation_default(self):
        stack = Stack()
        self.assertEqual(stack.size, 100)
        self.assertEqual(type(stack.stack), list)
        self.assertEqual(stack._size, 0)
        self.assertEqual(stack._warnings, "Verbose")

    def test_instantiation_Custom(self):
        stack = Stack(1, 2, 3, warnings="Essential", size=10)
        self.assertEqual(stack.size, 10)
        self.assertEqual(type(stack.stack), list)
        self.assertEqual(stack._size, 3)
        self.assertEqual(stack._warnings, "Essential")

    def test_Stack_Push_Pop_Size_Int(self):
        stack = Stack(warnings="Verbose", size=10)
        stack.push(5)
        stack.push(10)
        self.assertEqual(stack._size, 2)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack._size, 1)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack._size, 0)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack._size, 0)
        self.assertEqual(stack.push(100), None)
        self.assertEqual(stack._size, 1)

    def test_Stack_Push_Pop_Size_Float(self):
        stack = Stack(warnings="Verbose", size=10)
        stack.push(5.3)
        stack.push(10.1)
        self.assertEqual(stack._size, 2)
        self.assertEqual(stack.pop(), 10.1)
        self.assertEqual(stack._size, 1)
        self.assertEqual(stack.pop(), 5.3)
        self.assertEqual(stack._size, 0)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack._size, 0)
        self.assertEqual(stack.push(10.6), None)
        self.assertEqual(stack._size, 1)

    def test_Stack_Peek(self):
        stack = Stack(5, 10, 15, warnings="Verbose", size=10)
        self.assertEqual(stack._size, 3)
        self.assertEqual(stack.peek(), 15)
        self.assertEqual(stack._size, 3)

if __name__ == "__main__":
    unittest.main()
