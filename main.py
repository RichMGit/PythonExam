score = 0

print('Exam started')

def q1():
    q1options = ['func', 'def', 'function', 'define'];
    q1answer = q1options[1];
    print(q1options)
    q1 = raw_input('What is the keyword for functions in Python? ');
    if (q1 == q1answer):
        global score
        score = score + 1
def q2():
    q2options = ['break', 'loop out', 'stop', 'abandon'];
    q2answer = q2options[0];
    print(q2options)
    q2 = raw_input('What keyword terminates a loop in Python? ');
    if (q2 == q2answer):
        global score
        score = score + 1
def q3():
    q3options = ['string.length', 'str(length)', 'len(string)', 'len.string'];
    q3answer = q3options[2];
    print(q3options)
    q3 = raw_input('How do you get the length of a string? ');
    if (q3 == q3answer):
        score = score + 1
q1()
q2()
q3()

print score
