#Task put all the postal code on Norway.

#Dont forget to comments on the codes

postal_codes = {1444: "Oslo",
                2201: "Hedmark",
                3001: "Buskerud",
                3060: "Vestfold",
                3999: "Telemark",
                4400: "Vest-Agder",
                5003: "Hordland",
                8001: "Nordland",
                9006: "Torms",
                9501: "Finmark"}

user_input = int(input("Enter a postal code:"))

if user_input in postal_codes.keys():
    print(postal_codes[user_input])
else:
    print("The postal code does not exist.")

