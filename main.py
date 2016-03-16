score = 0

print('Exam started')
q1options = ['func', 'def', 'function', 'define'];
q1answer = q1options[1];
q2options = ['break', 'loop out', 'stop', 'abandon'];
q2answer = q2options[0];
q3options = ['string.length', 'str(length)', 'len(string)', 'len.string'];
q3answer = q3options[2];

print(q1options)
q1 = raw_input('What is the keyword for functions in Python? ');

if (q1 == q1answer):
    score += 1

print(q2options)
q2 = raw_input('What keyword terminates a loop in Python? ');

if (q2 == q2answer):
    score += 1

print(q3options)
q3 = raw_input('How do you get the length of a string? ');

if (q3 == q3answer):
    score += 1






print score
