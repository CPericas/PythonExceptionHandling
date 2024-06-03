while True:
    try:
        user_age = input("Enter your age: ")
        age = int(user_age)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
    except ValueError as ve:
        if "invalid literal" in str(ve):
            print("That is not a number. Please use digits.")
        else:
            print(ve)
    else:
        print(f"Thank you, your age is recorded as: {age}")
        break
