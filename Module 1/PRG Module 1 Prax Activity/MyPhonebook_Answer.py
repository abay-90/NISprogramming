phonebook = {"Big Corp": "555 1234",
             "PRG Inc": "555 2353",
             "Codeco": "555 1221",
             "FishNet": "555 2663",
             "Oil co": "555 7523"}

company_name = input("Enter a company name: ")
company_number = input("Enter a the company's number: ")
phonebook[company_name] = company_number

search = input("Enter a company name: ")

if search in phonebook.keys():
    print(phonebook[search])
else:
    print("The company is not in the phonebook.")

print(phonebook)
print(phonebook.keys())
