# कैलकुलेटर ऐप
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Zero से divide नहीं कर सकते"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Zero से modulo नहीं कर सकते"
    return a % b

def power(a, b):
    return a ** b
def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("❌ सिर्फ नंबर डालो")
def show_menu():
    print("\n--- Calculator App ---")
    print("1. जोड़ (+)")
    print("2. घटाव (-)")
    print("3. गुणा (*)")
    print("4. भाग (/)")
    print("5. शेष (%)")
    print("6. Power (**)")
    print("7. Exit")

while True:
    show_menu()
    choice = input("अपना choice डालो (1-7): ")

    if choice == "7":
        print("Calculator बंद हो गया 🙂")
        break

    a = get_number("पहला नंबर डालो: ")
    b = get_number("दूसरा नंबर डालो: ")

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    elif choice == "5":
        print("Result:", modulo(a, b))
    elif choice == "6":
        print("Result:", power(a, b))
    else:
        print("गलत choice")
