import unittest

from chapter_11.survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that a single response is stored properly"""
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question)

        responses = ['english', 'spanish', 'mandarin']
        for r in responses:
            # insert responses
            my_survey.store_response(r)

        for r in responses:
            # checking responses
            self.assertIn(r, my_survey.responses)
    
unittest.main()


