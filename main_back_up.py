import random

print('Exam started')

class shufflingQuestions:
    def questions():
        scores = {'overall_score' : 0, 'python' : 0, 'java' : 0, 'dummy' : 0}
        category = {
            'dummy': [
                ['What is the first letter of the alphabet? ', 'a', 'dummy', ['a', 'x', 'y', 'z']],
                ['What is the second letter of the alphabet? ', 'b', 'dummy', ['b', 's', 'm', 'v']],
                ['What is the third letter of the alphabet? ', 'c', 'dummy', ['c', 'r', 'w', 'p']]
            ],
            'python': [
                ['What is the keyword for functions in Python? ' , 'def', 'python', ['a', 'x', 'y', 'z']],
                ['What keyword terminates a loop in Python? ', 'break', 'python', ['a', 'x', 'y', 'z']],
                ['How do you get the length of a string? ', 'len(string)', 'python', ['a', 'x', 'y', 'z']]
            ],
            'java': [
                ['What are Public, Private and Protected examples of in Java? ', 'access modifiers', 'java', ['a', 'x', 'y', 'z']],
                ['What keyword is used to inherit a class? ' , 'extends', 'java', ['a', 'x', 'y', 'z']],
                ['Which of these object stores association between keys and values? ', 'maps', 'java', ['a', 'x', 'y', 'z']]
            ],
            'arsenal': [
                ['Who is the current Arsenal manager? ', 'Wenger', 'arsenal', ['wenger', 'mourinho', 'ferguson']],
                ['Who is the current Arsenal captain? ', 'Ozil', 'arsenal', ['wenger', 'mourinho', 'ferguson']]
            ],
            'man utd': [
                ['Who is the current Man Utd manager? ', 'Van Gaal', 'man utd', ['Van Gaal', 'mourinho', 'ferguson']],
                ['Who is the current Man Utd captain? ', 'Rooney', 'man utd',['wenger', 'mourinho', 'ferguson']]
            ]
        }

        question_set = category['dummy'] + category['python'] + category['java']
        random.shuffle(question_set)
        score, dummy, java, python = 0, 0, 0, 0
        for q in question_set[:-5]:
            random.shuffle(q[3])
            print(q[3])
            answer = input(q[0])
            if answer == q[1]:
                score += 1
                for k, v in scores.items():
                    if k == 'python':
                        print (v)

                # if q[2] == ['java']:
                #     java += 1
                # elif q[2] == 'dummy':
                #     dummy += 1
                # elif q[2] == 'python':
                #     python += 1
        print('Score: ', str(score))
        print('Java score: ', str(java))
        print('Python score: ', str(python))
        print('Dummy score: ', str(dummy))



    #     for q_a in question_set:
    #         print(possible_choices[0])
    #         userInput = input(q_a[0])
    #         possible_choices.pop(0)
    #         q_a.append(userInput)
    #         if q_a[1] == q_a[3]:
    #             overall_score += 1
    #             if q_a[2] == 'dummy':
    #                 dummy_score += 1
    #             elif q_a[2] == 'python':
    #                 python_score += 1
    #             else:
    #                 java_score += 1
    #     print("You scored " + str(overall_score))
    #     print("Dummy score: " + str(dummy_score))
    #     print("Python score: " + str(python_score))
    #     print("Java score:  " + str(java_score))
    #     newscore = round((overall_score / float(len(question_set))*100),1)
    #     print (str(newscore)+ "%")
    questions()
