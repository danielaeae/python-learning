def ask_age(prompt="How old are you? "):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter your age.")
            continue
        try:
            age = int(s)
        except ValueError:
            try:
                age = int(float(s))  # accept "30.0" as 30
            except ValueError:
                print("Please enter a whole number (e.g. 30).")
                continue
        if age < 0:
            print("Age can't be negative.")
            continue
        return age

def main():
    age = ask_age()
    if age < 13:
        print("You're a child.")
    elif age < 20:
        print("You're a teenager.")
    elif age < 65:
        print("You're an adult.")
    else:
        print("You're a senior.")

if __name__ == "__main__":
    main()