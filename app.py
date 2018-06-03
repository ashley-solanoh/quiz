import random

class Question(object):

     def __init__(self,pId,pQuestion,pCorrectChoice):
        '''
        Constructor
        '''
        self.id = pId
        self.question = pQuestion
        self.correctChoice = pCorrectChoice

     def __str__(self):
         return self.id + self.question + self.correctChoice

class Answer(object):

     def __init__(self,pQID,pChoiceID,pChoice):
        '''
        Constructor
        '''
        self.questionId = pQID
        self.choiceID = pChoiceID
        self.choice = pChoice

     def __str__(self):
         return self.questionId + self.choiceID + self.choice

class Choice(object):

     def __init__(self,pQID,pChoiceID,pChoice):
        '''
        Constructor
        '''
        self.questionId = pQID
        self.choiceID = pChoiceID
    
     def __str__(self):
         return self.questionId + self.choiceID


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
        vCorrectChoice = fields[3]
        vCorrectChoice = vCorrectChoice.rstrip()
 
        if topic == vTopic:
            newQuestion = Question(vQuestionID, vQuestion, vCorrectChoice)
            vQuestions.append(newQuestion)

    return vQuestions

def getChoices(pQuestion, pDifficulty): 
 
    vChoicesList = []
    vShownChoices = []

    choicesFile = open("choices.csv", "r")
    for line in choicesFile:
        fields = line.split(';')
        vQuestionID = fields[0]
        vChoiceID  = fields[1]
        vChoice  = fields[2]
        
        newChoice = Choice(vQuestionID, vChoiceID, vChoice)
        
        if (newChoice.questionId == pQuestion.id):
           vChoicesList.append(newChoice)
           print ("This is the correct answer " + str(vChoicesList))
      
    for x in range (0,len(vChoicesList)-1):
        print ("This is the ID of the choice in the : " + vChoicesList[x].choiceID)
        print (pQuestion.correctChoice + "This is the correct choice")
        if vChoicesList[x].choiceID == pQuestion.correctChoice:
#           print (vChoicesList[x].choiceID + ":)")
            print("")
            vShownChoices.append(vChoice)
            del vChoicesList[x]     

    random.shuffle(vChoicesList)    
 
    if (pDifficulty == "easy"):
        moreShownChoiceNum = 1
        print ("Nmber of choices left to pick: " + str(moreShownChoiceNum))
        print("")
 
    elif (pDifficulty == "medium"):
        moreShownChoiceNum = 2
        print ("Nmber of choices left to pick: " + moreShownChoiceNum)
        print("")

    elif (pDifficulty == "hard"):   
        moreShownChoiceNum = 3
        print ("Nmber of choices left to pick: " + moreShownChoiceNum)
        print("")

    for x in range(0,moreShownChoiceNum):
        print ("These are the choices which will be shown, before a choice was added" +  str(vShownChoices))
        print("")
        vShownChoices.append(vChoicesList[x])
        print ("These are the choices which will be shown, after a choice was added:" +  str(vShownChoices))
        print("")

    
    random.shuffle(vShownChoices)
   
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
    choices = getChoices(aQuestion, userDifficulty)

    print(aQuestion.question)
    
    for x in range (0,len(choices)):

        currentChoiceShown = str(choices[x])
        print (" " + str(x + 1) + ") "+ currentChoiceShown[x])
 
    userAnswer = input("> ")

    userAnswer = userAnswer.rstrip()
    print("***" + userAnswer + "****")
    
    answer = Answer(aQuestion.id, aQuestion.correctChoice, userAnswer)

    answers.append(answer)

    print("")

score = 0

for x in range (0, len(answers)):

    print ("-----------------------")
    rightAnswer = answers[x].choiceID
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

