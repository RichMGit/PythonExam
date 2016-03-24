
import random
from HTMLParser import HTMLParser

print('Exam started')

class shufflingQuestions:
    def main():
        parser = HTMLparser()
    def questions():
        score = 0
        answer = 0
        quesAndAns = [
            ['What is the keyword for functions in Python? ' , 'def'],
            ['What keyword terminates a loop in Python? ', 'break'],
            ['How do you get the length of a string? ', 'len(string)']]
        random.shuffle(quesAndAns)
        for qa in quesAndAns:
            userInput = raw_input(qa[0])
            qa.append(userInput)
            if qa[1] == qa[2]:
                score += 1
        #print("Total: " + parse(score) + "/3")
        print(score)
        print((score//3))
    questions()
