import unittest

from chapter_11.employee import Employee

class Test_Employee(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('bob', 'the builder', 3000)
        self.custom_bonus = 7777
    
    def test_give_default_raise(self):
        """giving your employee a default raise"""
        self.my_employee.give_raise()
        self.assertEqual(8000, self.my_employee.salary)

    def test_give_custom_raise(self):
        """giving your employee a special raise"""
        self.my_employee.give_raise(self.custom_bonus)
        self.assertEqual(10777, self.my_employee.salary)

unittest.main()