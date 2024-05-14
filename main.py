from unittest import TestCase
from parameterized import parameterized


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return
        example = self.stack.pop()
        return example

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def stack_reserch(stroka: str) -> str:
    s = Stack()
    for i in stroka:
        if i in '([{':
            s.push(i)
        elif i in ')]}':
            a = s.pop()
            if a == '(' and i == ')':
                continue
            elif a == '[' and i == ']':
                continue
            elif a == '{' and i == '}':
                continue
            else:
                s.push(a)
                break
    if s.is_empty():
        return 'Последовательность сбалансирована'
    else:
        return 'Последовательность не сбалансирована'


class TestSomething(TestCase):

    @parameterized.expand([('(((([{}]))))', 'Последовательность сбалансирована'),
                           ('[([])((([[[]]])))]{()}', 'Последовательность сбалансирована'),
                           ('{{[()]}}', 'Последовательность сбалансирована'),
                           ('}{}', 'Последовательность сбалансирована'),
                           ('{{[(])]}}', 'Последовательность не сбалансирована'),
                           ('[[{())}]', 'Последовательность не сбалансирована')])
    def test_get_stack_ok_1(self, stroka, expected):
        self.assertEqual(stack_reserch(stroka), expected)

