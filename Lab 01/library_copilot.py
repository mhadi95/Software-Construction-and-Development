def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


while True:
    try:
        year = int(input("Enter a year: "))

        if year < 0:
            raise ValueError("Year must be a positive number.")

        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

        break

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid integer year.")
