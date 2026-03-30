def kaprekar(number: str) -> None:
    numbers = list(number)
    result = ""
    steps = 0
    while result != "6174":
        numbers.sort(reverse=True)
        bigger = "".join(numbers)

        numbers.sort()
        smaller = "".join(numbers)

        result = str(int(bigger) - int(smaller)).zfill(4)
        steps += 1
        print(f"{bigger} - {smaller} = {result}")

        numbers = list(result)

    print(f"To achieve Kaprekar's Constant from number: {number}. You need to do: {steps} steps")

user_input = input("Enter a number: ")
if user_input.isdigit():
    if len(user_input) == 4:
        if len(set(user_input)) > 1:
            if user_input[0] != "0":
                kaprekar(user_input)
            else:
                print("A number cannot start with zero")
        else:
            print("Number must have at least two different digits")
    else:
        print("Number must be 4 digits long")
else:
    print("Input must be a number")
    
