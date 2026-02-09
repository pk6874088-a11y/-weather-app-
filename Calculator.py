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
    print("Result:"
