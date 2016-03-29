import random

print('Exam started')

class shufflingQuestions:
    def questions():
        overall_score = 0
        dummy_score = 0
        python_score = 0
        java_score = 0
        answer = 0

        multi_choice_dummy = ['a', 'x', 'y', 'z']
        multi_choice_dummy_2 = ['b', 's', 'm', 'v']
        multi_choice_dummy_3 = ['c', 'r', 'w', 'p']
        multi_choice_python = ['func', 'def', 'funcy', 'function()']
        multi_choice_java = ['inherits', 'extends', 'attaches', 'other']

        category_dummy = [['What is the first letter of the alphabet? ', 'a', 'dummy'],
                          ['What is the second letter of the alphabet? ', 'b', 'dummy'],
                          ['What is the third letter of the alphabet? ', 'c', 'dummy']]

        category_python = [['What is the keyword for functions in Python? ' , 'def', 'python'],
                         ['What keyword terminates a loop in Python? ', 'break', 'python'],
                         ['How do you get the length of a string? ', 'len(string)', 'python']]

        category_java = [['What are Public, Private and Protected examples of in Java? ', 'access modifiers', 'java'],
                         ['What keyword is used to inherit a class? ' , 'extends', 'java'],
                         ['Which of these object stores association between keys and values? ', 'maps', 'java']]

        random.shuffle(multi_choice_dummy)
        random.shuffle(multi_choice_python)
        random.shuffle(multi_choice_java)

        random.shuffle(category_dummy)
        random.shuffle(category_python)
        random.shuffle(category_java)

        possible_choices = []
        question_set = []

        possible_choices.append(multi_choice_dummy)
        possible_choices.append(multi_choice_dummy_2)
        possible_choices.append(multi_choice_dummy_3)
        possible_choices.append(multi_choice_python)
        possible_choices.append(multi_choice_java)

        question_set.append(category_dummy[0])
        question_set.append(category_dummy[1])
        question_set.append(category_python[0])
        question_set.append(category_python[1])
        question_set.append(category_java[0])
        question_set.append(category_java[1])



        for q_a in question_set:
            print(possible_choices[0])
            userInput = raw_input(q_a[0])
            possible_choices.pop(0)
            q_a.append(userInput)
            if q_a[1] == q_a[3]:
                overall_score += 1
                if q_a[2] == 'dummy':
                    dummy_score += 1
                elif q_a[2] == 'python':
                    python_score += 1
                else:
                    java_score += 1
        print("You scored " + str(overall_score))
        print("Dummy score: " + str(dummy_score))
        print("Python score: " + str(python_score))
        print("Java score:  " + str(java_score))
        newscore = round((overall_score / float(len(question_set))*100),1)
        print (str(newscore)+ "%")
    questions()
