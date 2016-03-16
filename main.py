import random

print('Exam started')

class allTheQuestions:
    answers = ['def', 'break', 'len(string)']
    q1options = ['func', 'def', 'function', 'define'];
    q2options = ['break', 'loop out', 'stop', 'abandon'];
    q3options = ['string.length', 'str(length)', 'len(string)', 'len.string'];


class shufflingQuestions:
    def shuffling():
        '''sq = shufflingQuestions.shuffling()
        questionList = [q1, q2, q3]
        random.shuffle(questionList)
        questionShuffled = questionList
        questionList.pop(0)
        return questionShuffled'''

    def questions():
        ques1 = raw_input('What is the keyword for functions in Python? ');
        ques2 = raw_input('What keyword terminates a loop in Python? ');
        ques3 = raw_input('How do you get the length of a string? ');
        score = 0

        questionList = [ques1, ques2, ques3]
        while (len(questionList) > 0):
            for q in questionList:
                random.shuffle(questionList)
                questionShuffled = questionList
                print(questionShuffled[0])
                questionShuffled.pop(0)
    questions()
'''global q1answer, q2answer, q3answer
if q1answer == answers[0]:
    score += score + 1
if q2answer == answers[1]:
    score += score + 1
if q3answer == answers[2]:
    score += score + 1
'''
