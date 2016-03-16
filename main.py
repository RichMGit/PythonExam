import random

score = 0
print('Exam started')

def questions():
    global score
    q1options = ['func', 'def', 'function', 'define'];
    q1answer = q1options[1];
    print(q1options)
    q1 = raw_input('What is the keyword for functions in Python? ');
    if (q1 == q1answer):
        score = score + 1
def q2():
    global score
    q2options = ['break', 'loop out', 'stop', 'abandon'];
    q2answer = q2options[0];
    print(q2options)
    q2 = raw_input('What keyword terminates a loop in Python? ');
    if (q2 == q2answer):
        score = score + 1
def q3():
    global score
    q3options = ['string.length', 'str(length)', 'len(string)', 'len.string'];
    q3answer = q3options[2];
    print(q3options)
    q3 = raw_input('How do you get the length of a string? ');
    if (q3 == q3answer):
        score = score + 1

questionList = [q1(), q2(), q3()]
h = [1, 2, 3, 4 , 5]
random.shuffle(questionList)
random.shuffle(h)
print h
