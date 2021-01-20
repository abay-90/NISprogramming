sales_list = list()

while len(sales_list) < 10:
    sales_value = float(input("Enter a sales value: "))
    sales_list.append(sales_value)

    if sales_value < 5000:
        continue
    elif 5000 < sales_value < 10001:
        print("Total:  ", sum(sales_list))
        print("Average:  ", sum(sales_list)/float(len(sales_list)))
    elif sales_value > 10000:
        print("A possible date entry error has occurred.")
        break





