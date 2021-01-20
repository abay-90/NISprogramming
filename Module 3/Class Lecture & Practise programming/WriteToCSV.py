my_file = open("CSVfile.csv", "w")

# First row / heading
my_file.write("Name,Description,Amount\n")

# Other row
my_file.write("John Doe, First customer, 1000.00\n")
my_file.write("Jane Doe, Second customer, 2500.00\n")

my_file.close()
