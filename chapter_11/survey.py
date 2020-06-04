class AnonymousSurvey():
    """Collect anonymous answers to a survey question"""

    def __init__(self, question):
        """Store a qn and prepare to store responses"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """show the qn"""
        print(self.question)
    
    def store_response(self, new_response):
        """stores 1 response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses to the qn"""
        print("Survey results: ")
        for r in self.responses:
            print('- ' + r)