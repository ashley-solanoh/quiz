import random

class Question():
     def __init__(self,pId,pQuestion,pAnswer):
        '''
        Constructor
        '''
        self.id = pId
        self.question = pQuestion
        self.answer = pAnswer

class Answer():
     def __init__(self,pQID,pCAnswer,pChoice):
        '''
        Constructor
        '''
        self.questionId = pQID
        self.cAnswer = pCAnswer
        self.choice = pChoice


def saveAccount( pAccName, pName, pYearG,pAge,pPassW ):

    fileName = (pAccName + ".txt")

    accountFile = open(fileName, "w")
    accountFile.write ("Account Name = " + pAccName + "\n")
    accountFile.write ("Name = " + pName + "\n")
    accountFile.write ("Year Group  = " + pYearG + "\n")
    accountFile.write ("Age = " + pAge + "\n")
    accountFile.write ("Password = " + pPassW + "\n")
    accountFile.close()

def getTopics():
 
    vTopics = ["history", "science", "maths"]

    return vTopics    

def getDifficulties():
 
    vDifficulties = ["easy", "medium", "hard"]

    return vDifficulties    


def getQuestions(topic):

    vQuestions = []
    

    questionsFile = open("questions.csv", "r") 
    for line in questionsFile: 
        fields = line.split(';')

        vTopic = fields[0]
        vQuestionID = fields[1]
        vQuestion = fields[2]
        vAnswer = fields[3]
        vAnswer = vAnswer.rstrip()
 
        if topic == vTopic:
            newQuestion = Question(vQuestionID, vQuestion, vAnswer)
            vQuestions.append(newQuestion)

    return vQuestions

def getChoices(pQuestion, pDifficulty): 
 
    moreChoice = True
    vChoicesList = []
    vShownChoices = []

    choicesFile = open("choices.csv", "r")
    for line in choicesFile:
        fields = line.split(';')
        vQuestionID = fields[0]
        vChoice  = fields[1]

##        if (vQuestionID == Question.id && vChoice == Question.answer) 
##          vChoicesList.append



        if (vQuestionID == pQuestion.id):
            vChoicesList.append(vChoice)
       
    for x in range (0,len(vChoices)):
        if vChoicesList[x] == pQuestion.answer :
            vShownChoices.append(vChoice)
            vChoices.remove[x]     

    vChoicesList.shuffle    
 
    if (pDifficulty == "easy"):
        moreShownChoiceNum = 1
        
        for x in range (0,moreShownChoiceNum)
            vShownChoices.append(vChoicesList[x])

    elif (pDifficulty == "medium"):
        moreShownChoiceNum = 2
        for x in range(0,moreShownChoiceNum):
            vShownChoices.append(vChoicesList[x])

    elif (pDifficulty == "hard"):   
        moreShownChoiceNum = 3
        for x in range(0,moreShownChoiceNum):
            vShownChoices.append(vChoicesList[x])

    
    vShownChoices.shuffle
   
    return vShownChoices    

confirm = True
name = input("What is your name?  ")
age = input("what is your age?  ")
yearG = input ("what is your year group?  ")

accName = name[0:3] + (age)
passW = input("what will your password be?  ")

passC = input("please confirm your password  ")

if passC != passW:
  
  while confirm : 
    if confirm:
    
      passC = input("please type your password in again  ")
	
    else:
      confirm = Ture 

#save all variables on external file
quizData = (accName + "Stats.txt")


saveAccount( accName, name, yearG, age, passW )

quizFile = open(quizData, "w")
quizFile.write (accName + "’s quizzes " + "\n")  
quizFile.write ("\n")


quizFile.write ("    History:" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.write ("\n")


quizFile.write ("    Science:" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.write ("\n")


quizFile.write ("    Maths:" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.write ("\n")
quizFile.close()

topics = getTopics()

print ("Pick a topic")

for i in range (0,len(topics)):
    print ("  - " + topics[i])

userTopic = input("> ")

print("")

print("Pick a Difficulty")

difficulties = getDifficulties()

for i in range (0,len(difficulties)):
    print ("  - " + difficulties[i])

userDifficulty = input("> ")

questions = getQuestions(userTopic)
print("")

answers = []

for i in range (0,len(questions)):

    aQuestion = questions[i]
    choices = getChoices(Question, userDifficulty)

    print(aQuestion.question)
    
    for x in range (0,len(choices)):

        print (" " + str(x + 1) + ") "+ choices[x])
 
    userAnswer = input("> ")

    userAnswer = userAnswer.rstrip()
    print("***" + userAnswer + "****")
    
    answer = Answer(aQuestion.id, aQuestion.answer, userAnswer)

    answers.append(answer)

    print("")

score = 0

for x in range (0, len(answers)):

    print ("-----------------------")
    rightAnswer = answers[x].cAnswer
    userAnswer = answers[x].choice

    print ("---" + rightAnswer + "---")
    print ("+++" + userAnswer + "+++")

    if rightAnswer == userAnswer:
        score = score + 1

    print ("-----------------------")

if score == 5:
    
    grade = "A"

elif score >= 3:

    grade = "B"

elif score >= 1:

    grade = "C"

elif score == 0:

    grade = "F"

percentage = score * 20

print ("Your score was " + str(score)  + "/5")
print ("Your Grade was " + grade )
print ("Your percentage was " + str(percentage) + "%") 

