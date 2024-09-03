""" A quiz program. """

total_score = 0

class Quiz_Refactor: # created a Quiz Refactor class
    def __init__(self, topic, art_and_space_questions):
        self.topic = topic # this will give the answer of the topic to equal the answer given
        self.art_and_space_questions = art_and_space_questions # this will give the answer of the art and space questions to equal the answer given

def main():  #  creating a main method
    topic = input('Would you like art, or space questions?')
    if topic == 'art': # creating a if/else statement for the two topics, if the answer is art, then it will ask these questions
        art_and_space_questions = [ #creating a list inside the if statement with questions for Art
            ('Who painted the Mona Lisa?', 'Leonardo Da Vinci'),
            ('What precious stone is used to make the artist\'s pigment ultramarine?', 'Lapiz lazuli'),
            ('Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?', 'Chicago'),
        ]

    elif topic == 'space': # creating a if/else statement for the two topics, if the answer is space, then it will ask these questions
        art_and_space_questions = [ #creating a list inside the if statement with questions for Space
            ('Which planet is closest to the sun?', 'Mercury'),
            ('Which planet spins in the opposite direction to all the others in the solar system?', 'Venus'),
            ('How many moons does Mars have?', '2')
        ]
    else:
        print('That is not a valid topic. Restart the program to try again.') # this will print out if 'art' or 'space' isn't chosen and will return
        return

    def __str__(self, total_score):  # adding question method to the Quiz_Refactor class
        for question, answer in self.art_and_space_questions:
            if answer == answer:
                print('Correct!')
                self.total_score += 1
            else:
                print(f'Sorry the answer is {answer}')


    def total_score(self): # adding a total_
        print('End of quiz!')
        print (f'Your total score on {topic} questions is {total_score} out of 3.')
        if total_score == 3:
            print ('You got all the answers correct!')


main() # have to call main methods after calling


#
# total_score = 0
#
# topic = input('Would you like art, or space questions? ')
#
# if topic == 'art':
#
#     print('Who painted the Mona Lisa?')
#     answer = input('Enter your answer: ')
#     if answer == 'Leonardo Da Vinci':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the answer is Leonardo Da Vinci.')
#
#     print('What precious stone is used to make the artist\'s pigment ultramarine?')
#     answer = input('Enter your answer: ')
#     if answer == 'Lapiz lazuli':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Lapiz lazuli.')
#
#     print('Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?')
#     answer = input('Enter your answer: ')
#     if answer == 'Chicago':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Chicago.')
#
#     print('End of quiz!')
#     print(f'Your total score on {topic} questions is {total_score} out of 3.')
#
#     if total_score == 3:
#         print('You got all the answers correct!')
#
#
# elif topic == 'space':
#
#     print('Which planet is closest to the sun?')
#     answer = input('Enter your answer: ')
#     if answer == 'Mercury':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Mercury.')
#
#     print('Which planet spins in the opposite direction to all the others in the solar system?')
#     answer = input('Enter your answer: ')
#     if answer == 'Venus':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Venus.')
#
#     print('How many moons does Mars have?')
#     answer = input('Enter your answer: ')
#     if answer == '2':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is 2.')
#
#     print('End of quiz!')
#     print(f'Your total score on {topic} questions is {total_score} out of 3.')
#
#     if total_score == 3:
#         print('You got all the answers correct!')
#
# else:
#     print('That is not a valid topic. Restart the program to try again.')
#
