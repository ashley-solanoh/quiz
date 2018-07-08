test = 0

print (" 1) select a quiz ")
print (" 2) view results  ")
print (" 3) exit program  ")

choice = int(input("choose a numbered option "))

while (test == 0):
    if (choice == 1):
        print("Welcome to the quiz menu!\n");
        test =1
    elif (choice == 2):
        print("Look at these overall results!\n")
        test =1
    elif (choice == 3):
        print("Exiting program")
        break
    else:
        print("Pick a valid option")
