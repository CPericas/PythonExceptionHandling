#Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast 
#application that gracefully handles unexpected user input and provides user-friendly error messages.

#Task 1: Start
#Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.
#Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be 
#converted to a number.

#while True:
#    try:
#        f_temp = int(input("Please enter the temperature in Fahrenheit: "))
#    except ValueError:
#        print("Please only enter a number.")
#    print(f_temp)
#    break


#Task 2: Temperature Conversion
#Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
#Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.
#def temp_conversion():
#    while True:
#        try:
#            f_temp = int(input("Please enter the temperature in Fahrenheit: "))
#            celcius_conversion = (f_temp - 32) * 5 / 9
#            return celcius_conversion
#        except ValueError:
#            print("Please only input numerical numbers.")
#        except ZeroDivisionError:
#            print("Cannot divide by 0.")
#        except OverflowError:
#            print("Your numbers are crazy. Please try again.")
#celcius = temp_conversion()
#print(f"The converted temperature is {celcius:.2f}C")


#Task 3: User Experience
#Implement an else block that prints the converted temperature in a user-friendly format.
#Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed 
#regardless of whether an exception was caught or not.

def temp_conversion():
    while True:
        try:
            f_temp = int(input("Please enter the temperature in Fahrenheit: "))
            celcius_conversion = (f_temp - 32) * 5 / 9            
        except ValueError:
            print("Please only input numerical numbers.")
        except ZeroDivisionError:
            print("Cannot divide by 0.")
        except OverflowError:
            print("Your numbers are crazy. Please try again.")
        else:
            print(f"The converted temperature is {celcius_conversion:.2f}C")
        finally:
            print("Thank you for using the Weather Forecast app!")
            break
temp_conversion()



