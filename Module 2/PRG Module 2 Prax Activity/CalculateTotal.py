#Comments on the codes

total = 0    # This is global variable.
add_me = int(input("Enter an integer: "))   # The int() method returns an integer object from any number or string.

while add_me != -1:     # The while statement is used for repeated execution as long as an expression is true
    total += add_me     # Add both the parameters and return them."
    add_me = int(input("Enther an integer: "))  # Here total is local variable.

print("Total: ", total)
