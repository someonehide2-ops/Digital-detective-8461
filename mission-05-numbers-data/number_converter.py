"""Convert a positive whole decimal number to binary and hexadecimal."""

def main():
    raw_value = input("Enter a positive whole number: ").strip()

    try:
        number = int(raw_value)
        if number <= 0:
            print("Please enter a positive whole number greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number, such as 13.")
        return

    print(f"Binary: {bin(number)}")
    print(f"Hexadecimal: {hex(number)}")


if __name__ == "__main__":
    main()
