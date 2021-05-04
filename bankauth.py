# Register
# first name,last name ,password, email
# generate user account
#login
# account number and password


#Bank operations

#Initializing the system
import random
database = {}

def init():

    #isvalid_option_selected 
    print("Welcome to bank PHP")

    #while isvalid_option_selected == False:

    have_account=int(input("Do you have account with us: 1(Yes) 2(No)\n"))
        
    if(have_account == 1):
           
           #  isvalid_option_selected = True
           
       login()
    
    elif(have_account == 2):
           # isvalid_option_selected = True
        
        register()
    
    else:
        print("You have selected invalid option")
        init()



def login():

   
    print("**********  Login **********")

   # islogin_successful = False

    #while islogin_successful == False:

    account_number_from_user = int(input("What is your account number?\n"))
    password = input("What is your password?\n")

    for account_number,user_details in database.items():
        if(account_number == account_number_from_user):
            if(user_details[3] == password):
                bank_operation(user_details)
                     #islogin_successful = True
                 

    print('Invalid account or password')
    login()
    #bank_operation(user_details)


def register():

    print("***** Register *****")

    email = input("What is your email address?\n")
    first_name = input("What is your first name?\n")
    other_name= input("What is your other name?\n")
    last_name= input("What is your last name\n")
    password = input("Create your password?\n")

    account_number = generation_account_number()

    database[account_number] = [first_name, other_name, last_name, email, password]

    print("Your account has been created")
    print("*** **** ***** *****")
    print("Your account number is: %d" %account_number)
    print("Make sure you keep it safe")
    print("*** **** ***** ***** ")

    login()

def bank_operation(user):

    print("Welcome %s %s " %{ user[0], user[1] } )

    selected_option = int(input("What would you like to do? (1) Withdrawal (2) Deposit (3) Complaint (4) Logout (5) Exit\n"))

    if(selected_option == 1):

         withdrawal_operation()

    elif(selected_option == 2):

         deposit_operation()
    elif(selected_option == 3):

         complaint_operation
    elif(selected_option == 4):

         login()
    elif(selected_option == 5):

         exit()

    else:

        print("Invalid option selected")
        bank_operation(user)

def withdrawal_operation():
    print("withdrawal")

def deposit_operation():
    print("deposit")

def complaint_operation():
    print("complaint")

def logout_operation():
    print("logout")


def generation_account_number():

    #print("Generating Account Number")
    return random.randrange(1111111111,9999999999)

def logout():
    login



""" ACTUAL BANKING SYSTEM """

#print(generation_account_number())
init()
