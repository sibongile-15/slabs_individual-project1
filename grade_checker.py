def main():
    try:
        practical = float(input("Enter Practical Assessment mark (0-100): "))
        theory = float(input("Enter Theory Examination mark (0-100): "))
        if not (0 <= practical <= 100) or not (0 <= theory <= 100):
            print("Error: Marks must be between 0 and 100")
            return
        final_mark = (practical * 0.4) + (theory * 0.6)
        print(f"Weighted Final Mark: {final_mark:.2f}%")
        if final_mark >= 50:
            print("Student status: PASS")
        else:
            print("Student status: FAIL")
    except ValueError:
        print("Error: Please enter valid numbers only")
if __name__ == "__main__":
    main()
