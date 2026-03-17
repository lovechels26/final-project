import random

if __name__ == '__main__':
    print('welcome to my quiz!')
#Categories: Book Musicals, Concept Musicals, Jukebox Musicals, and Rock/Pop Operas
    questions = [
        'What is the largest animal on earth?',
        'What is the fastest animal on earth?',
        'What is the most famous muscial in the Jukebox genre?',
        'Who directed this musical?',
        'What year did this musical open?',
        'Is this musical still being performed?',
        'Is the show on or off broadway?',
        'Who is the main character in this musical?'
    ]

    answers = [
        'blue whale',
        'falcon',
        'Mamma Mia!',
        'Phyllida Lloyd',
        '1999',
        'Yes',
        'Off Broadway',
        'Donna',
    ]

    r = random.randint(0, len(questions) - 1)

    response = input(questions[r] + ' ')

    response = response.lower()
    print('response: ' + response)

    if response == answers[r]:
        print('Correct!')
    else:
        print('Incorrect')

    