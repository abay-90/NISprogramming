sales_values = list()

print("SALES MANAGER")
print("-" * 80)

while input("Do you wish to enter a sales value?  Enter y for yes or any other key for no: ") == "y":
    try:
        sales_values.append(float(input("Please enter a sales value:  ")))
    except ValueError:
        print("Please ensure that you enter a valid sales value.")

print("You have entered", len(sales_values), "sales values.")
print("How many of these values do you wish to include in the total calculation?")

while True:
    number_of_sales = -1
    try:
        number_of_sales = int(input("Number of sales: "))

        total = 0

        try:
            for i in range(0, number_of_sales):
                total += sales_values[i]

            print("Sales total:  ", total)
            break
        except IndexError:
            print("Please ensure that the number of sales entered is in the range 0 to", len(sales_values), ".")
            continue
    except ValueError:
        print("Please ensure that you enter a valid number of sales.")
        continue






