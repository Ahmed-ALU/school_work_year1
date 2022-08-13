

x_list = list()
y_list = list()
result_list = list()

x_len = int(input("Please enter the number of elements in the list [X]: "))
for i in range(x_len):
    inp = int(input("Please input the list element here: "))
    x_list.append(inp)

y_len = int(input("Please enter the number of elements in the list [y]: "))
for i in range(y_len):
    inp = int(input("Please input the list element here: "))
    y_list.append(inp)

print("X = ", x_list)
print("Y = ", y_list)

Value = bool()


for numy in y_list: # There is exists Y that ....
    
    for numx in x_list: # for all of X ...
        if numx%numy == 0: #The condition
            Value = True #continue looping
        else:
            Value = False # IF there is only one value.... 
            #....of x that is false, the condition is false
            #.... for that specific element of Y
            break # break and go to the next y if exist
    
    if Value == True:
        result_list.append(True)  
    elif Value == False:
        result_list.append(False)


if True in result_list:
    print("The condition Y|X is True")
else: 
    print("The condition is False")