#Task ?

##Dont forget to comments on the codes

sales_list = list()

while len(sales_list) < 10:
    sales_values = float(input("Enter a sales value: "))
    sales_list.append(sales_values)

    if sales_values < 5000:
        continue
    elif 5000 < sales_values < 10001:
        print("Total: ", sum(sales_list))
        print("Average: ", sum(sales_list/float(len(sales_list)))
    elif sales_values> 10000:
        print("A possible date entry error has occurred. ")
        break
