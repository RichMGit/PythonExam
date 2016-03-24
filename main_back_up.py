import random

print('Exam started')

class shufflingQuestions:
    def questions():
        overall_score = 0
        dummy_score = 0
        python_score = 0
        java_score = 0
        answer = 0

        category_dummy = [['What is the first letter of the alphabet? ', 'a'],
                          ['What is the second letter of the alphabet? ', 'b'],
                          ['What is the third letter of the alphabet? ', 'c']]

        category_python = [['What is the keyword for functions in Python? ' , 'def'],
                         ['What keyword terminates a loop in Python? ', 'break'],
                         ['How do you get the length of a string? ', 'len(string)']]

        category_java = [['What are Public, Private and Protected examples of in Java? ', 'access modifiers'],
                         ['What keyword is used to inherit a class? ' , 'extends'],
                         ['Which of these object stores association between keys and values? ', 'maps']]

        random.shuffle(category_dummy)
        random.shuffle(category_python)
        random.shuffle(category_java)

        question_set = []

        question_set.append(category_dummy[0])
        question_set.append(category_dummy[1])
        question_set.append(category_python[0])
        question_set.append(category_python[1])
        question_set.append(category_java[0])
        question_set.append(category_java[1])

        for q_a in question_set:
            userInput = raw_input(q_a[0])
            q_a.append(userInput)
            if q_a[1] == q_a[2]:
                overall_score += 1
                # if question[3] == 'dummy':
                #     dummy_score += 1
                # elif question[3] == 'python':
                #     python_score += 1
                # else:
                #     java_score += 1
        print("You scored " + str(overall_score))
        print("Dummy score: " + str(dummy_score))
        print("Python score: " + str(python_score))
        print("Java score:  " + str(java_score))
        newscore = round((overall_score / float(len(question_set))*100),1)
        print (str(newscore)+ "%")
    questions()
