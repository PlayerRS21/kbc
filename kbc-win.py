import os
import time

user = ["Ritesh", "user2", "user3"]
pswd = [150907, 200109, 190512]

def game():
    questions = [
        "Which command is used to list files and directories in Linux?",
        "Which command is used to print the current working directory?",
        "How do you create a new empty file named example.txt?",
        "Which command is used to display the contents of a file?",
        "How do you move file1.txt to folder1?",
        "Which command is used to delete a file?",
        "How do you create a new directory named myfolder?",
        "Which command shows running processes in Linux?",
        "How do you change file permissions?",
        "How do you copy doc.txt to backup/?"
    ]
    answers = ["ls", "pwd", "touch example.txt", "cat filename", "mv file1.txt folder1/", "rm", "mkdir myfolder", "top", "chmod", "cp doc.txt backup/"]
    rupees = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    
    # Use os.path.join for file path
    result_file_path = os.path.join(os.getcwd(), "result.txt")
    
    with open(result_file_path, "w", encoding="utf-8") as obj:
        i = 0
        balance = 0
        correct = 0
        incorrect = 0
        
        while i < len(questions):
            print("Question", i + 1)
            print(questions[i])
            inp = input("Enter Your Answer: ").strip()  # Strip whitespace to avoid input issues
            
            obj.write(questions[i] + ":\nYour Answer: " + inp + " , Correct Answer: " + answers[i] + "\n")
            
            if inp == answers[i]:
                balance = balance + int(rupees[correct])
                correct = correct + 1
            else:
                incorrect = incorrect + 1
            
            i = i + 1
        
        print("Your Overall Result is:", str(int(correct) * 10) + "%,", correct, "Correct and", incorrect, "Incorrect")
        obj.write("Total Correct Answers: " + str(correct) + "\nTotal Incorrect: " + str(incorrect))
        obj.write("\nTotal Prize Earned: ₹" + str(balance))
        print("The Prize You WON!!!", balance)

def login():
    inp_user = input("Enter Your UserName: ")
    inp_pswd = input("Enter Your Password: ")
    
    if inp_user in user:
        index = user.index(inp_user)
        if int(inp_pswd) == pswd[index]:
            print("Login Successful!!!\nRedirecting to Test...")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            game()
        else:
            print("Credentials Mismatch!!\nRedirecting to Login Screen...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            login()
    else:
        print("No user found\nRedirecting to Login Screen...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        login()

login()