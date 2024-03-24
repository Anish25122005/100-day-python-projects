'''
this is a quiz game containing 10 questions the score increases based on the number of questions answered correctly

'''
score=0
Q1=input("What is the capital of INDIA?:")
if (Q1.lower()=="delhi"):
    score+=1
else:
    print("wrong answer")
Q2=int(input("How Many States does INDIA have?:"))
if (Q2==29):
    score+=1
else:
    print("wrong answer")
Q3=input("Does INDIA have a desert (Y/N):")
if (Q3.lower()=='y'):
    score+=1
else:
    print("wrong answer")
Q4=int(input("In which year did india get its independence:"))
if (Q4==1947):
    score+=1
else:
    print("wrong answer")
Q5=int(input("How Many years has it been since INDIA got independence:"))
if (Q5==76):
    score+=1
else:
    print("wrong answer")
print("you scored",score,"out of 5")
if(score<=2):
    print("can do better.")
    print("THANK YOU FOR PLAYING.")
elif(score>2 and score<=4):
    print("you are very knowledgeable.")
    print("THANK YOU FOR PLAYING.")
else:
    print("outstanding.")
    print("THANK YOU FOR PLAYING.")

