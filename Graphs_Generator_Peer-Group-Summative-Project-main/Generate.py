import random
import time

timestart = time.time() 
vertix = int()
array = int()
C1 = list()
temp = list()
checked = list()
nCg = int()
n2 = int()
x = int()
tim = True
Graph_Matrix = list([[],[],[],[],[],[],[],[],[],[]]) # Here we put 10 arrays/matricies as a representation for the 10 verticies
c_graphs = list()

# Section one Starts from here
###############################################################################################

######################################
# This next function is used to generate the graphs of 10 matricies, and check how many components/connected graphs
# is there in our main graphs and print their strings if exist.
#####################################

def generate():
    global tim
    while tim: 
        global Graph_Matrix

        #Now we have the list of matrices which is empty, we need to fill each with 10 
        # different random numbers between 1 and zero (0), because we can 't have a number more than that 
        # as long as we are generating a simple undirected graph with no loops or multible edges.

        array_numb = int(0)
        vert_numb = int(0)
        for i in range(100):
            if vert_numb == array_numb: # Here we must make the diagonal is equal to zeros, and this condition do that, because it is a simple graph and cann't have loops
                Graph_Matrix[array_numb].append(0) #Add Zero
            else:
                Graph_Matrix[array_numb].append(random.randint(0, 1)) # This condition is for adding a random ones and zeros other than the diagonal
            vert_numb += 1
            if vert_numb == 10 : # Once we finish each array, we add 1 to the array var so that we go to the next array
                vert_numb = int(0)
                array_numb += 1
            if array_numb == 10 and vert_numb == 10: #Once we finish generating just break the loop
                break

        n1 = int(-1)
        n2 = int()

        ##### Part 01 of fixing the errors that might be found in the generated matrix #####
        #### Here we Shall check if the the matrix is making sense in the part of being undirected and here is how:
        
        #..... if two verticies are connected to each others (for example vertix 01 and vertix 02), 
        # in that case we must have a value of one in both the the second matrix value in the first array and 
        # The First matrix value in the second array in order to say that those two verticies are connected with no direction
        
        # That condition hasn't been followed in the last/first part of the code because it was mostly randomly generated  

        for array in range (10):
            n2 = 0 
            n1 += 1
            for vertix in range(10):
                if Graph_Matrix[n1][n2] == 0 and Graph_Matrix[n2][n1] == 1: #if the explained condition is not followed.....
                    Graph_Matrix[n1][n2] = 1 # add value one 1 to the matrix that is equal to zero 0
                    n2 += 1
                elif Graph_Matrix[n1][n2] == 1 and Graph_Matrix[n2][n1] == 0: #if the explained condition is not followed in the flipped way.....
                    Graph_Matrix[n2][n1] = 1 # add value one 1 to the matrix that is equal to zero 0
                    n2 += 1
                else:
                    n2 += 1
                    pass

            
        #Now we finished generating part, we can go on with the printing part
        #Here we print the code in the shape of matrix
        print (f"The Adjecency martix of our randomly generated graph is as the following")    
        for i in Graph_Matrix: 
            print (i)    

################################################################################################
#Section one is done
###############################################################################################


        
# Section Two Starts from here
###############################################################################################

# This next code function main jop is to check if the code has disconnected graph or not
# , Then append those grpahs to a list to go back to it later

# How it works ??.......
#           The other_components() function works on guiding the other functions and deliver the non checked arrays
#           to them if it is not checked yetm in order to check the array, read it and append the correct string to the list.
# 
#           The first_component function is responciple in checking each array and generating the right string 
#           of each component out of it in the shape of numbers like (graph: 0, 3  or graph: 1, 2, 4)

#           The first_component() function contains two parts, the first one works in checking the first 
#           arrays in a specific connected graph, and the second one works in checking and processing the 
#           temporary graphs (Please read about our algorithms to understand this)




        def other_components(): # works in guiding the next function work, and make sure to stop the app once all the verticies are checked
            global array, vertix, C1, checked, temp, x

            
            for num in range(10): #In range of the number of values in each array which is 10......
                try:
                    if C1[-1] != "sep" : # We add the string "sep"  == "separator" in the start of the process of appending
                                            # ..... the connected vertices to the list as a way to differ between the connected graphs and the disconnected graphs. 
                        C1.append("sep")# we add it if it is not (in the end of the list)/(The closing of a connected graph)
                except BaseException:
                    C1.append("sep") # When the list is empty it gives an index error, that means that this is the start of the programme and we should add it
                
                # ------ The next small code works in checking if the cuurent
                #array (x value) has been checked or not (in the checked list) -------
                if x in checked and x < 9: #If checked  and still there are more to see the checking situation....
                    x+=1 # Go to the next one and skip the current one
                elif x not in checked and x < 9: # if not checked.........
                    array = x 
                    C1.append(array) #We put it as the first vertix in the path
                    checked.append(x) # Put it as a checked array
                    first_component(array) # Send it to the first_component() function.................
                    x += 1 # Go to the next one if the first_component() function is done with it.........
                elif x == 9 and x not in checked: # If it is the last array....
                    array = x 
                    C1.append(array)
                    first_component(array)
                    break # break the loop after you finish
                elif x == 9 and x in checked: # If it is the last array....
                    break # break the loop after 
            


        def first_component(line):
            global array, vertix, C1, checked, temp, n2, tim

            loop = True

            while loop == True:

                # This part of the code works in generating the strings of each component, and make sure it is not repeated or making loops
                # and if it finds a new vertix it add it to the temp list to repeat the process for the verticies in the temp elements.

                vertix = 0
                for i in Graph_Matrix[line]:
                    
                    if i == 0: 
                        vertix += 1
                        pass
                    elif i == 1 and vertix < 9 and vertix not in checked and vertix != C1[-2]:
                        if Graph_Matrix[vertix][C1[-1]] == 1:
                            C1.append(vertix)
                        temp.append(vertix)
                        vertix += 1
                    elif i == 1 and vertix < 9 and (vertix in checked or vertix == C1[-2]):
                        # C1.append(vertix)
                        vertix += 1
                    elif i == 1 and vertix == 9 and vertix not in checked and vertix != C1[-2]:
                        C1.append(vertix)
                        temp.append(vertix)
                        # checked.append(line)
                    elif i == 1 and vertix == 9 and (vertix in checked or vertix == C1[-2]) :
                            # checked.append(temp[0])
                            # del temp[0]
                            pass
                    elif i == 0 and vertix == 9 and vertix in checked:
                        # checked.append(line)
                        pass
            
                if temp == []: # if there is no other elements in the temp list, just break the loop
                    loop = False
                else:
                    pass
                

                # This is where the verticies in the temp elements will be proceeced.......

                for i1 in range(len(temp)):
                    vertix = 0
                    for num in Graph_Matrix[temp[0]]:
                        if num == 0 and vertix < 9: 
                            vertix += 1
                            pass
                        elif num == 1 and vertix < 9 and vertix != C1[-2] and vertix not in checked:
                            if vertix not in checked:
                                if vertix not in temp:
                                    temp.append(vertix)
                            if vertix != C1[-1] and temp[0] == C1[-1]:
                                C1.append(vertix)
                            elif vertix != C1[-1] and temp[0] != C1[-1] and temp[0] != C1[-2]:
                                C1.append(temp[0])
                                C1.append(vertix)
                            vertix += 1
                        elif num == 1 and vertix < 9 and (vertix in checked or vertix == C1[-2]) :
                            # C1.append(vertix)
                            vertix += 1
                            # if vertix not in checked:
                            #     checked.append(vertix)
                            # del temp[i1]
                        elif num == 1 and vertix == 9 and (vertix in checked or vertix == C1[-2]) :
                            checked.append(temp[0])
                            del temp[0]
                            n2 = True
                        elif (num == 1  and vertix == 9) and (vertix != C1[-2] and vertix not in checked):
                            if vertix not in C1:
                                temp.append(vertix)
                            if vertix != C1[-1] and temp[0] == C1[-1] :
                                C1.append(vertix)
                            elif vertix != C1[-1] and temp[0] != C1[-1] and temp[0] != C1[-2]:
                                C1.append(temp[0])
                                C1.append(vertix)
                                
                            checked.append(temp[0])
                            del temp[0]
                            n2 = True
                        elif (num == 0 ) and (vertix == 9):
                            checked.append(temp[0])
                            del temp[0]
                            n2 = True
                        if temp == []: # if there is no other elements in the temp list, just break the loop
                            loop = False 
                            other_components() # Then go to the other compnents function to finish the guidence
                        else:
                            if 1 in checked and 2 in checked and 3 in checked and 4 in checked and 5 in checked and 6 in checked and 7 in checked and 8 in checked and 9 in checked and 0 in checked:
                                loop = False
                                other_components()
                                break
                            pass
        other_components()
# ---------------------------------------------------------------------

# Section Three Starts from here
###############################################################################################

        global c_graphs
        c_graphs = list()
        n1 = int()
        n2 = int()
        n3 = int()
        l = True
        component_num = int()
        temp_list = list()
        del C1[0]

## This section has been made to reorganize the generated strigs of teh components because we found that
# sometimes it generates with wrong order, so here we will check if every vertix is in the right place.....

        for g in C1: # to check every compnent in the compononents list
            l = True
            count = int()
            if g != 'sep':
                temp_list.append(g)
            else:
                while l == True :
                    for i in temp_list:
                        n2 = int()
                        
                        # Here we will check if each vertix is in the right place depending on its place from the other vertices before and after it

                        if Graph_Matrix[i][temp_list[n2+1]] == 1 and Graph_Matrix[temp_list[n2+1]][i] == 1:
                            count +=1
                            if count == len(temp_list)-1:
                                l = False
                                break
                            else:
                                n2+=1
                                pass
                        elif Graph_Matrix[i][temp_list[n2+1]] != 1 or Graph_Matrix[temp_list[n2+1]][i] != 1:
                            n2 = int()
                            temp_list.remove(i)
                            for t in range(len(temp_list)+1):
                                if time.time()- timestart > 3:
                                    break
                                temp_list.insert(t, i)
                                if Graph_Matrix[i][temp_list[n2+1]] == 1 and Graph_Matrix[temp_list[n2+1]][i] == 1:
                                    n2+=1
                                    break
                                elif Graph_Matrix[i][temp_list[n2+1]] != 1 or Graph_Matrix[temp_list[n2+1]][i] != 1:
                                    n2+=1
                                    pass
                        if n2 >= len(temp_list)-1:
                            l = False
                            break
                component_num += 1
                # print(f"The component number {component_num} is : {temp_list}")

                # ONce we are done, we will print the last product of our components......
                
                c_graphs.append(temp_list)
                temp_list = list()
                print(f"We have {component_num} components/connected graphs in our main graph and they are as the following: ")
                g_num = int()
                for k in c_graphs:
                    g_num += 1
                    if len(c_graphs) <= 1:
                        print(f"The component number {g_num} is : {k} (This is the a complete path in the graph)")
                        tim = False
                    # elif len(c_graphs) == 1:
                    #     tim = False
                if time.time()- timestart > 3:
                    print("Something wrong happend with the graph, please rerun the programme")


    ########################################


# generate()


