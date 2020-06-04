## setUp() method
## MAKE SURE THE 'U' IS IN CAPS

'''
when you include setup() method in a testclass case, python runs the setup() method before running each method starting with test_.

Any objects created in the setup() method are then available in each test method you write
'''

import unittest

from chapter_11.survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?" 
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        # store 'english'
        self.my_survey.store_response(self.responses[0])
        # check 'english'
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that a single response is stored properly"""
        # insert responses
        for r in self.responses:
            self.my_survey.store_response(r)
        # checking responses
        for r in self.responses:
            self.assertIn(r, self.my_survey.responses)

unittest.main()
