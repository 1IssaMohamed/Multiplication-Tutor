import time
import random
import pyfiglet
from termcolor import colored
figlet= pyfiglet.Figlet(font='Graffiti')
print(colored(figlet.renderText("Welcome to your own personal Math Tutor!"),"red",on_color="on_black"))
totalStart=time.time()
#User specifies the nbumber of questiosn that they will be asked and the limits of the questions 
numOfQs=int(input("How many questions woud you like to practice?\n"))
QLimit=int(input("What is the limit of the questions?"))
#run the questions
#allow the user to know how much time they used per question
correct=0
answerSheet={}
for x in range(numOfQs):
    quickTimeS=time.time()
    n1=random.randint(0,QLimit)
    n2=random.randint(0,QLimit)
    attempt=int(input(f"{n1} x {n2}"))
    answer=n1*n2
    if attempt==answer:
        correct+=1
    answerSheet[f"{n1}X{n2}"]=n1*n2
    quickTimeE=time.time()
    print(f"it took you {quickTimeE-quickTimeS} to answer the q")
#once done output 
#1. thanks for playing
#2. Their socre
#3. Their %
#4. How much time it took to solve in total
#5. Questions and answers
totalEnd=time.time()
figlet2=pyfiglet.Figlet(font="Mini")
print(colored(figlet2.renderText("Thank you for playing!"),"red",on_color="on_black"))
print(f"You final score is: {correct}/{numOfQs}\nThis is equivalent to {(correct/numOfQs)*100}%\nIt  took you {totalEnd-totalStart} to complete the set of questions\nHere is the final answer sheet:")
for x,y in answerSheet.items():
    print(f"{x}:{y}")

