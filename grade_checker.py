def main():
    try:
        mark = float(input("Enter student mark (0-100): "))
        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100")
            return
        if mark >= 50:
            print("Student status: PASS")
        else:
            print("Student status: FAIL")
    except ValueError:
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()
