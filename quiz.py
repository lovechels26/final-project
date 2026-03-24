import random

questions = [
    'What is the largest animal on earth?',
    'What is the fastest animal on earth?',
    'What is the most famous muscial in the Jukebox genre?',
    'Who directed this musical?',
    'What year did this musical open?',
    'Is this musical still being performed?',
    'Is the show on or off broadway?',
    'Who is the main character in this musical?',
    'Where does the plot of this musical take place?',
    'How many characters are in this musical?',

]

answers = [
    'blue whale',
    'falcon',
    'mamma mia!',
    'phyllida lloyd',
    '1999',
    'yes',
    'off broadway',
    'donna',
    'kalokairi',
    'twelve',
]

asked = []

def select_question_and_answer(questions: list, answers: list, asked: list) -> tuple:

    # TODO check if asked list is already same size as questions and answers list
    # TODO if so, return None

    r = random.randint(0, len(questions) - 1)
    while r in asked:
        r = random.randint(0, len(questions) - 1)
    
    asked.append(r)
    return (questions[r], answers[r])

if __name__ == '__main__':
    print('welcome to my quiz!')
    print('Categories: Book Musicals, Concept Musicals, Jukebox Musicals, and Rock/Pop Operas')

    count = 0
    i = 0
    while i < len(questions):
        q = select_question_and_answer(questions, answers, asked)

        response = input(questions[0] + ' ')

    response = response.lower() == r[1].lower()

    if response == answers[0]:
        print('Correct!')
    else:
        print('Incorrect')

    i += 1