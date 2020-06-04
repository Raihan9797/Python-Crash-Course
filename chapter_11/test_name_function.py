import unittest

from chapter_11.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

### ABOUT UNITTEST ###
'''
the dot (.) on the first line of the output tells us that a single test passed

also shows us that it took less than 0.001 seconds to run
'''

##### NOTE ABOUT RUNNING THE CODE #####
'''
run the program once in VSCode. It will actually send you out of Python terminal and into CMD ie Powershell. So to run the code again, we have to type in
> python

which will open the python terminal again
then run the code again
'''

'''
additionally, we can also run it in CMD by typing
> python -m unittest
However, you can't seem to do
> python
> unittest # or unittest.py or unittest.main()
'''


### A Failing Test
## we will modify get_formatted_name() to accept middle names which will break the function if we just have 'Janis' and 'Joplin'

