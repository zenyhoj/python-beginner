calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):

    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


# def validate_execute():  # encapsulating the validation logic by putting all in the function
#     if user_input.isdigit():  # validates the user_input if it is a number
#         user_input_number = int(user_input)  # converts the user_input into a number
#         if user_input_number > 0:
#             calculated_days = days_to_units(user_input_number)
#             print(calculated_days)
#         elif user_input_number == 0:
#             print("You enter 0, please provide a valid positive number")
#
#     else:
#         print("your input is not a valid number, please provide a valid number")

# using a try/except block to catch errors
def validate_execute():  # encapsulating the validation logic by putting all in the function
    try:
        user_input_number = int(user_input)  # converts the user_input into a number
        if user_input_number > 0:
            calculated_days = days_to_units(user_input_number)
            print(calculated_days)
        elif user_input_number == 0:
            print("You enter 0, please provide a valid positive number")
        else:
            print("You enter a negative number, Please enter a non-negative number")

    except ValueError:
        print("your input is not a valid number, please provide a valid number")


user_input = ""  # initialized the user_input to suppress the error
while user_input != "exit":  # continue asking for input until the user types exit word
    user_input = input("Please provide a number of days to convert to hours \n")
    validate_execute()
