print("-" * 30)
print("  ASCII VALUE EXPLORER  ")
print("-" * 30)

while True:
    user_input = input("\nEnter a character (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    if len(user_input) == 1:
        value = ord(user_input)
        print(f" > The secret number for '{user_input}' is: {value}")
    elif len(user_input) == 0:
        print(" ! You didn't type anything.")
    else:
        print(" ! Error: Please enter only ONE character at a time.")

    print("-" * 20)
