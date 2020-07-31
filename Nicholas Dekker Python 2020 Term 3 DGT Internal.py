#Nicholas Dekker DGT Python Internal

# Question List
questionone = "Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?"

#Age Requirement
answer = input("Before you take this quiz first please let us know if you are between the ages of 8 and 13? Only input your answer as Yes or No: ")
if answer == "yes" or answer == "Yes":
    # Do this
    print("Welcome to the Cybersmart start Quiz!")
elif answer == "no" or answer == "No": 
    # Do that
    print("Unfortunantely you don't meet the criteria to take this quiz, please consider taking the Cybersmart Youth Quiz instead.")
    exit()
else:
     print("Invalid Input re-enter the quiz.")
     exit()


#Get Users Name 
print("Note you only gain a point if you get the question correct on the first attempt.")
name = input("What is your name? ")
print(f"Hello {name}. The Quiz begins now!")

#Questions 1-3
score = 0
print("Question 1: You find out someone has posted an embarrasing picture of you online. What should you do?\n")
answerCorrect = False
maxTrys = 3
while not answerCorrect and maxTrys > 0:
    print("(A): Tweet that they are an idiot and a loser")
    print("(B): Ask your friends to give the person a hard time")
    print("(C): Tell an adult you trust\n")
    Answer = input("Input your answer here: ")
    if Answer in ('C', 'Tell an adult you trust','c'): 
        print('Correct!')
        if maxTrys == 3: score = score + 1
        answerCorrect = True
    else:
        maxTrys -= 1
        if maxTrys == 0:
            print("Sorry That's incorrect the correct answer is, C. Tell an adult you trust")
        else:
            print("Incorrect, Try Again? [{} Chances Remaining]".format(maxTrys - 1)) 
            

print("Question 2: You want to join an online gaming site. Which of the following information is ok for you to post on the site?\n")
answerCorrect = False
maxTrys = 3
while not answerCorrect and maxTrys > 0: 
    print("(A): A nickname")
    print("(B): Your name")
    print("(C): Your email address\n")
    Answer = input("Input your answer here: ")
    if Answer in ('A', 'A nickname','a'): 
        print('Correct!')
        if maxTrys == 3: score = score + 1
        answerCorrect = True
    else:
        maxTrys -= 1
        if maxTrys == 0:
            print("Sorry That's incorrect the correct answer is, A. A nickname")
        else:
            print("Incorrect, Try Again? [{} Chances Remaining]".format(maxTrys - 1))
            


print("Question 3: Someone in your class is a real bully. Some of the people in your class say: Let's get them back, and spam them with random texts. What do you reply?\n")
answerCorrect = False
maxTrys = 3
while not answerCorrect and maxTrys > 0:
    print("(A): We shouldnt be mean to them just because theyre mean to us")
    print("(B): Yeah, totally. Theyre Evil and deserve it!")
    print("(C): Yes I think thats a great idea. Maybe they will understand what it feels like and stop bullying us!\n")
    Answer = input("Input your answer here: ")
    if Answer in ('A', 'We shouldnt be mean to them just because theyre mean to us','a'):
        print('Correct!')
        if maxTrys == 3:score = score + 1
        answerCorrect = True
    else:
        maxTrys -= 1
        if maxTrys == 0:
            print("Sorry That's incorrect the correct answer is, A. We shouldnt be mean to them just because theyre mean to us")
        else:
            print("Incorrect, Try Again? [{} Chances Remaining]".format(maxTrys - 1))
           
#Final Score            
print('You scored', score,'/3 Thankyou for playing goodbye!')
exit() 


