def ask_yes_no_question(question):
    while True:
        answer= input(question + " (Mac/Windows): ").lower()
        if answer == "Mac":
            return True
        elif answer == "Windows":
            return False

question = "Did you find adding remote repositories to github harder on Mac or on Windows"
response = ask_yes_no_question(question)

if response=='Mac':
    print ("Yes Mac is a little more confusing but it has some advantages such as being able to use git wihtin the same command terminal, wheras in windows you would have to use a whole other git bash terminal for git. Here is a guide for better understanding git's setup on mac: https://medium.com/@aklson_DS/how-to-properly-setup-your-github-repository-mac-version-3a8047b899e5")
else:
    print("Oh, but technically Windows had less steps for remoting repositories by just right clicking the folder and clicking 'git bash here' then continuing work.")
