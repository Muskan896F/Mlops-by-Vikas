class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()


    
    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("enter your password here -> ")
        self.username = email
        self.password = pwd
        print("You have successfully signed up")
        print("\n")
        self.menu()


    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here ->")
            pwd = input("enter your password here -> ")
            if self.username==uname and self.password==pwd:
                print("You have successfully signed in")
                self.loggedin = True
            else:
                print("please input correct credentials")

        print("\n")
        self.menu()



    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your post here -> ")
            print(f"Your post is: {txt}")
        else:
            print("You need to sign in first to write a post")  
        print("\n")
        self.menu()


    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            friend = input("Whom to send the msg? ->") 
            print(f"Your message is: {txt} and it has been sent to {friend}")
        else:
            print("You need to sign in first to send a message")
        print("\n") 
        self.menu()  




obj = chatbook()
