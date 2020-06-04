## don't forget to shift terminal to this folder!
from survey import AnonymousSurvey

# or this instead
from chapter_11.survey import AnonymousSurvey 

# define the question, and make a survey instance
question = "What language did you first learn to speak?" 
my_survey = AnonymousSurvey(question)

# show the question and show the responses
my_survey.show_question()

print('enter q to quit')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

# show results
my_survey.show_results()


