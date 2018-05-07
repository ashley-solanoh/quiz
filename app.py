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
print ("all done!") 



quizData = (accName + "Stats.txt")


saveAccount( accName, name, yearG, age, passW )

quizFile = open(quizData, "w")
quizFile.write (accName + "’s quizzes " + "\n")  
quizFile.write ("\n")


quizFile.write ("    Science:" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.write ("\n")


quizFile.write ("    History:" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.write ("\n")


quizFile.write ("    Geography:" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.write ("\n")


quizFile.write ("    Common Sense:" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.write ("\n")


quizFile.write ("   Music :" + "\n")
quizFile.write ("      Easy: N/A" + "\n")
quizFile.write ("      Medium: N/A" + "\n")
quizFile.write ("      Hard: N/A" + "\n")
quizFile.close()

topics = getTopics()
