#Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, 
#handling any type of arithmetic errors or user input exceptions.

#Task 1: Start
#Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
#Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

#try:
#    original_servings = int(input("How many servings does the original recipe call for?: "))
#    updated_servings = int(input("How many servings would you like to make?: "))
#    print(f"Original serving amount: {original_servings} being adjusted for {updated_servings} servings...")
#except ValueError:
#    print("Only input numbers.")


#Task 2: Quantity Calculation
#Calculate the adjustment factor by dividing the desired servings by the original servings.
#Use a try block to catch any arithmetic errors that may occur during the calculation.

#def serving_size_update():
#    try:
#        original_servings = int(input("How many servings does the original recipe call for?: "))
#        updated_servings = int(input("How many servings would you like to make?: "))
#        return updated_servings // original_servings
#    except ValueError:
#        print("Please only input digits.")
#    except ZeroDivisionError:
#        print("Cannot divide by 0. Please try again.")

#Task 3: Serving Success
#If the calculation is successful, display the adjusted recipe quantities to the user.
#Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

def serving_size_update():
    try:
        original_servings = int(input("How many servings does the original recipe call for?: "))
        updated_servings = int(input("How many servings would you like to make?: "))
        adjusted_servings = updated_servings / original_servings
        print((f"Adjusted recipe quantity: {adjusted_servings}"))
    except ValueError:
        print("Please only input digits.")
    except ZeroDivisionError:
        print("Cannot divide by 0. Please try again.")
    finally:
        print("Now go make Gordon Ramsey proud and enjoy your cooking experience!")
serving_size_update()