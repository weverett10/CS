import random
question_markings = ['am','was','is','should','could','would','will','when','which']

while True:
    question = str.lower (input('what is your question:'))
    
    first_word = question.split()[0]
    if first_word in question_markings:
        answers = ['yes', 'no', 'maybe', 'ask again later']
        response = random.choice (answers)
        print(response)
    else:
        print('not a question')
        print('try again')
