katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            message += f' {i + 1}. {katz_deli[i]}'
        print(message)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. ' +\
        f'You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]
# katz_deli = []

# def line():
#     if not katz_deli:
#         print("The line is currently empty.")
#     else:
#         line_positions = [f"{index+1}. {name}" for index, name in enumerate(katz_deli)]
#         current_line = ", ".join(line_positions)
#         print(f"The line is currently: {current_line}")

# def take_a_number(line, name):
#     line.append(name)
#     position = len(line)
#     print(f"Welcome, {name}. You are number {position} in line.")

# def now_serving(line):
#     if not line:
#         print("There is nobody waiting to be served!")
#     else:
#         serving = line.pop(0)
#         print(f"Now serving {serving}.")


# take_a_number(katz_deli, "Alice") "
# take_a_number(katz_deli, "Bob")    

# line()  # Output: 

# now_serving(katz_deli)  
# now_serving(katz_deli

# line() 
