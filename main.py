import random

print('Exam started')

class allTheQuestions:

    q1options = ['func', 'def', 'function', 'define']
    q2options = ['break', 'loop out', 'stop', 'abandon']
    q3options = ['string.length', 'str(length)', 'len(string)', 'len.string']

class shufflingQuestions:

    def questions():
        ques1 = 'What is the keyword for functions in Python? '
        ques2 = 'What keyword terminates a loop in Python? '
        ques3 = 'How do you get the length of a string? '

        score = 0
        answer = 0
        quesAndAns = [[ques1, 'def'], [ques2, 'break'], [ques3, 'len(string)']]
        while (len(quesAndAns) > 0):
            for q in quesAndAns:
                random.shuffle(quesAndAns)
                print (quesAndAns)
                '''questionShuffled = quesAndAns
                a = raw_input (questionShuffled[0])
                quesAndAns.append(a)
                questionShuffled.pop(0)'''
        print (allArray[0][1])
    questions()
