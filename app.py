class Question():
     def __init__(self,pId,pQuestion):
        '''
        Constructor
        '''
        self.id = pId
        self.question = pQuestion



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
 
        if topic == vTopic:
            newQuestion = Question(vQuestionID, vQuestion)
            vQuestions.append(newQuestion)

    return vQuestions    


def getChoices(pQuestionID, pDifficulty):
 
    moreChoice = True
    vChoices = []

    choicesFile = open("choices.csv", "r")
    for line in choicesFile:
        fields = line.split(';')
        vQuestionID = fields[0]
        vChoice = fields[1]

        if (vQuestionID == pQuestionID):
            
            vChoices.append(vChoice)
        
        if (pDifficulty == "easy"):
            return vChoices[0,2]    
        if (pDifficulty == "medium"):
            return vChoices[0,3]    
        return vChoices    



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

difficulties = getDifficulties()

print ("Pick a Difficulty")

for i in range (0,len(difficulties)):
    print ("  - " + difficulties[i])

userDifficulty = input("> ")

questions = getQuestions(userTopic)
print("")


for i in range (0,len(questions)):

    aQuestion = questions[i]
    choices = getChoices(aQuestion.id, userDifficulty)

    print(aQuestion.question)
    
    for x in range (0,len(choices)):

        print (" " + str(x + 1) + ") "+ choices[x])
 
    userAnswer = input("> ")

    print("")
