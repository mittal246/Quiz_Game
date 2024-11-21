import random # improting the module
login_info='login_details.txt'  #stores the credentials of user in local storage
registration_info='registration_details.txt'  # stores the data of newly registered user
users_info = {}  # contains username and password of users
Question_set = {
    "DSA": [
        {"Ques": "Which data structure uses LIFO (Last In, First Out) principle?", "Answer": ['A.Queue', 'B.Stack', 'C.Array', 'D.Linked List', 'B.Stack']},
        {"Ques": "Which of these is not a sorting algorithm?", "Answer": ['A.Bubble Sort','B.Quick Sort','C.Binary Search','D.Merge Sort','C.Binary Search']},
        {"Ques": "Which data structure is used for Breadth-First Search (BFS) of a graph?", "Answer": ['A.Queue', 'B.Stack', 'C.Array', 'D.Linked List', 'A.Queue']},
        {"Ques":"Which traversal technique visits all nodes of a binary tree in left-root-right order?", "Answer": ['A.Inorder', 'B.Preorder', 'C.Postorder', 'D.LevelOrder', 'A.Inorder']},
        {"Ques":"Which data structure is used to implement recursion?", "Answer": ['A.Queue', 'B.Stack', 'C.Array', 'D.Linked List', 'B.Stack']}
    ],
    "DBMS": [
        {"Ques": "Which SQL keyword is used to fetch data from a database?", "Answer": ['A.SELECT', 'B.FETCH', 'C.GET', 'D.RETRIEVE', 'A.SELECT']},
        {"Ques": "Which database model organizes data into tables?", "Answer": ['A.Relational','B.Hierarchical','C.Network','D.NoSQL','A.Relational']},
        {"Ques": "Which command is used to delete a table in SQL?", "Answer": ['A.DROP', 'B.DELETE', 'C.REMOVE', 'D.TRUNCATE', 'A.DROP']},
        {"Ques": "What type of key uniquely identifies a record in a table?", "Answer": ['A.Foreign key', 'B.Primary key', 'C.Candidate key', 'D.Alternate key', 'B.Primary key']},
        {"Ques": "Which of the following is not a type of database normalization?", "Answer": ['A.1NF', 'B.2NF', 'C.4NF', 'D.6NF', 'D.6NF']},
    ],
    "PYTHON": [
        {"Ques": "Which keyword is used to define a function in Python?", "Answer": ['A.def', 'B.func', 'C.function', 'D.define', 'A.def']},
        {"Ques": "What is the output of print(2 ** 3) in Python?", "Answer": ["A.8","B.6","C.2","D.9","A.8"]},
        {"Ques": "Which data type is mutable in Python?", "Answer": ['A.String', 'B.List', 'C.Tuple', 'D.Int', 'B.List']},
        {"Ques": "Which library is used for data analysis in Python?", "Answer": ['A.numpy', 'B.pandas', 'C.matplotlib', 'D.scikit-learn', 'B.pandas']},
        {"Ques": "Which keyword is used to handle exceptions in Python?", "Answer": ['A.handle', 'B.error', 'C.except', 'D.catch', 'C.except']},
    ]
}      # dictionary which stores questions of three different subjects
def show_profile(username):
    profile={}
    with open('registration_info.txt','r') as file:
        for line in file:
            data=line.strip().split(',')
            username=data[3]
            profile[username]={
                'name':data[0],
                'enroll_num':data[1],
                'college':data[2]
            }
    # Display user profile info
    if username in profile:
        user_data = profile[username]
        print(f"Name: {user_data['name']}")
        print(f"Enrollment Number: {user_data['enroll_num']}")
        print(f"College: {user_data['college']}")
    else:
        print("User not found.")
    

def registration():
    name = input("Enter your name: ").strip()
    enroll_num = input("Enter your enrollment number: ").strip()
    college = input("Enter your college: ").strip()
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    try:
        # Load existing usernames to check for duplicates
        users_info = {}
        try:
            with open('login_details.txt', 'r') as file:
                for line in file:
                    existing_username, _ = line.strip().split(",", 1)
                    users_info[existing_username] = True
        except FileNotFoundError:
            # If file doesn't exist, assume no users exist yet
            pass

        if username in users_info:
            print("User already exists. Please try logging in.")
        else:
            # Write to registration details
            with open('registration_details.txt', 'a') as reg_file:
                reg_file.write(f"{name},{enroll_num},{college},{username},{password}\n")

            # Write to login details
            with open('login_details.txt', 'a') as log_file:
                log_file.write(f"{username},{password}\n")

            print("Registration successful!")
    except Exception as e:
        print(f"An error occurred during registration: {e}")


def login():
    username = input("enter your username:").strip()
    password = input("enter your password:").strip()
    try:
        with open('login_details.txt', 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    print("Login successful!")
                    return True  # Successfully logged in
        print("Invalid username or password. Please try again.")
        return False  # Login failed
    except FileNotFoundError:
        print("No registered users found. Please register first.")
    

def attempt_quiz(username):
    print("Choose any one subject:DSA/DBMS/PYTHON")
    sub = input("Enter your subject: ").upper().strip()
    if sub in Question_set:
        print(f"You have choosen {sub}.Here are the questions for the respected subject:-")
        score = 0
        questions = Question_set[sub][:]  # Create a copy of the questions to shuffle
        random.shuffle(questions)  # Shuffle the questions
        for ques in questions:
            print("Q:-",ques["Ques"])
            for option in ques['Answer'][:-1]:
                print(option)
            Answer = input("Enter your correct option(A/B/C/D):-").strip()
            if Answer.upper() == (str(ques["Answer"][-1])[0:1]):
                print("Answer is correct")
                score += 1
            else:
                # print(str(ques["Answer"][-1])[0:1])
                # print(str(ques["Answer"][-1]))
                print(f"Wrong! The correct answer is:\n{ques['Answer'][-1]}")
        print(f"\nYour final score: {score}/{len(questions)}")
        show_result(username,score)
    else:
        print("Choose the subject correctly!")  


def show_result(username,score):
    filename = "scores.txt"
    scores = {}

    # Read existing scores from the file
    try:
        with open(filename, "r") as file:
            for line in file:
                user, user_score = line.strip().split(",")
                scores[user] = int(user_score)
    except FileNotFoundError:
        pass  # File doesn't exist yet, will be created

    # Update or add the user's score
    scores[username] = max(scores.get(username, 0), score)

    # Write the updated scores back to the file
    with open(filename, "w") as file:
        for user, user_score in scores.items():
            file.write(f"{user},{user_score}\n")

def main():
    while True:
        print("\n--- Welcome to the Quiz Game ---")
        print("1. Register")
        print("2. Login")
        print("3. Show user profile")
        print("4. Attempt the quiz!")
        print("5. Display the result")
        print("6. Quit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            registration()
        elif choice == "2":
            username=login()
            if login():
                attempt_quiz(username)
        elif choice == "3":
            username = input("Enter your username to view profile: ").strip()
            show_profile(username)
        elif choice=='4':
            attempt_quiz(username)
        elif choice=='5':
            username = input("Enter your username to view result: ").strip()
            with open("scores.txt", "r") as file:
                for line in file:
                    user, user_score = line.strip().split(",")
                    if user == username:
                        print(f"{user}'s score: {user_score}")
        elif choice=='6':
            print("Thanks for taking the quiz!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__=='__main__':
    main()