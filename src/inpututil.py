from art import aprint

def safe_input(prompt, conversion_func=None):
    readable_error = {
        'int': 'numbers',
        'float': 'numbers',
        'str': 'text'
    }

    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            print("Thank you for using Drop Chance Calculator!")
            aprint("sad and confused")
            exit()
            
        elif conversion_func:
            try:
                converted = conversion_func(user_input)
                if isinstance(converted, int) or isinstance(converted, float):
                    if user_input.replace('.','',1).isdigit():
                        if converted <= 0:
                            raise ValueError(f"Invalid input! - Please enter positive {readable_error[conversion_func.__name__]}.")
                        return converted
                    else:
                        print(f"Invalid input! - Please enter positive {readable_error[conversion_func.__name__]}.")
            except ValueError as exception:
                print(f"Invalid input! - Please enter positive {readable_error[conversion_func.__name__]}.")
        else:
            return user_input
