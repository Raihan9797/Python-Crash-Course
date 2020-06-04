import unittest

from chapter_11.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

### Adding new test
    def test_first_last_mid_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        function_output = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(function_output, 'Wolfgang Amadeus Mozart')

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
THERE ARE REFERENCING PROBLEMS WHEN YOU TRY TO RUN IT THIS WAY:
VSCODE WORK AREA IS ONE ISSUE AND THE TEST_FILES WHICH IMPORTS CHAPTER_11 MEAN THAT IF YOU GO IN CHAPTER_11 FOLDER, THEY WILL HAVE AN ERROR BECAUSE 'CHAPTER_11' MODULE IS NOT AVAILABLE....
additionally, we can also run it in CMD by typing
> python -m unittest
However, you can't seem to do
> python
> unittest # or unittest.py or unittest.main()
'''


### A Failing Test
## we will modify get_formatted_name() to accept middle names which will break the function if we just have 'Janis' and 'Joplin'

'''
>>> unittest.main()
E    
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 5, in test_first_last_name
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
'''
# 1 E ==> 1 Error


### Responding to a Failed Test
'''
DO NOT CHANGE THE TEST! IT'S LIKE CHANGING ANSWERS WHEN YOU ANSWERED WRONGLY

we resolve this by making middle names optional

MAKE SURE YOU ADD THE NEW TEST CASE FUNCTION IN THE UNITTEST CLASS!!
'''
