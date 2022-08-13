from Generate import generate, Graph_Matrix, c_graphs

# THis programme checks if the generated graphs has an euler path

x = int()
circ_num = int()
test_graph = list()
circuits = list()
euler_c = bool()

def euler():
    global x, test_graph, circuits, circ_num, euler_c
    for array in Graph_Matrix:
        for i in array:
            x += i
        if x % 2: # if all has even degree, then it has an euler circuit
            x = int()
            euler_c = True
            pass
        else: # if any of the arrays/verticies has an odd degree, so there is no euler's circuit here
            euler_c = False
            print("The Main graph doesn't have an euler circuit as one or more of the verticies has an odd degree...")
            break

    if euler_c == True: # if there is an euler circuit........................
        for graph in c_graphs: 
            # print it after making sure it is a circuit.....(first and last vertix are the same)
            for vertix in graph:
                if vertix not in test_graph:
                    test_graph.append(vertix)
                test_graph.append(test_graph[0])
                circuits.append(test_graph)

        print(f" We have {circ_num} Euler's circuits in the main graph, and they are as the following: ")
        y = int()
        for circ in circuits:
            y += 1
            print(f"The circuit number {y} is : {circ}")
