import random, itertools # Import needed Modules

#All Variables we will need in one place
# global list_of_sets, user_input_set01, user_input_set02, choices_list, n1, n2, list_length
list_of_sets = [{1, 2, 3, 4, 5},
    {3, 4, 5}, {10, 22, 11}, {11, 22, 33, 44}, {10, 20, 30, 40}, {-1, 0, 1, 2, 3}]
n1 = random.randint(0, len(list_of_sets)-1)
n2 = random.randint(0, len(list_of_sets)-1)
user_input_set01 = set({})
user_input_set02 = set({})
choices_list = ["1. input a set", "2. use our examples/trial sets"]
list_length = int()
cart_product = list()
cart_lists = list([])




def choice(): # This Function is only for giving the user the coice to input lists/sets or use ready ones
    
    #define variables
    global list_of_sets, user_input_set01, user_input_set02, choices_list, n1, n2, list_length

    #Make the user choose the way the program will go
    print("Please indicate weather you want to input a set or you want to try one from our trial sets: ")
    for choice in choices_list:
        print(choice)
    user_choice = int(input("Answer (1 OR 2): "))

    ###User chose to to input his own lists/sets###
    if user_choice == 1: #The user will input a list 
    
    #input the first list/set (A)
        # number of elements as input
        list_length = int(input("Enter number of elements in your first set : "))
        # converting to list to append
        user_input_set01 = list(user_input_set01)
        # iterating till the range
        for i in range(0, list_length):
            element = int(input("Enter the elemnet here: "))
            user_input_set01.append(element) # adding the element
        #making it a set again
        user_input_set01 = set(user_input_set01)
        # self.input01 = user_input_set01

    #input the Second list/set (B)
        list_length = int(input("Enter number of elements in your second set : "))
        # converting to list to append
        user_input_set02 = list(user_input_set02)
        # iterating till the range
        for i in range(0, list_length):
            element = int(input("Enter the elemnet here: "))
            user_input_set02.append(element) # adding the element
        user_input_set02 = set(user_input_set02)
        # self.input02 = user_set02
    
    ###User chose to use the program lists/sets###
    elif user_choice == 2: #From the programme random list
        user_input_set01 = list_of_sets[n1] #Choose a random set to make operation on from the trial list
        user_input_set02 = list_of_sets[n2] #Choose a random set to make operation on from the trial list 
    
    ###If he/she chose a wrong number from the choices ###
    else:
        print("you chose the wrong answer")
        choice()


def Q2():

    #Define Variables
    global list_of_sets, user_input_set01, user_input_set02, choices_list, n1, n2, list_length, cart_product, cart_lists

    #print the input sets/lists
    print (f"\nSet A = {user_input_set01}, \n Set B = {user_input_set02} \n ")

    # (a) The answer of  [B is subset of A]
    if user_input_set02.issubset(user_input_set01) :
        print ("True, B is a subset of A \n")
    else:
        print ("False, B is not a subset of A \n")
    
    # (b) The answer of  [A - B]
    diff = user_input_set01.difference(user_input_set02)
    print(f"The value of A-B = {diff} \n")
    
    # (c) The answer of [A x B]

    user_input_set01 = list(user_input_set01)
    user_input_set02 = list(user_input_set02)
    
    
    cart_lists.append(user_input_set01)
    cart_lists.append(user_input_set02) 

    import itertools
    for pair in itertools.product(*cart_lists):
        cart_product.append(pair)

    cart_product = set(cart_product) 
    print(f"The value of AxB = {cart_product}")
    cart_product = list(cart_product)

choice()
Q2()