input_string = "Dear RECIPIENT, Please find attached a cheque to the amount of AMOUNT.  Kind regards, SENDER"
input_string = input_string.replace("RECIPIENT", "John")
input_string = input_string.replace("AMOUNT", "3000.00 NOK")
input_string = input_string.replace("SENDER", "Management")
print(input_string)
