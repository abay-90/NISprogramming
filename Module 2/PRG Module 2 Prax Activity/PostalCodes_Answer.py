postal_codes = {1444: "Oslo",
                2201: "Hedmark",
                3001: "Buskerud",
                3060: "Vestfold",
                3999: "Telemark",
                4400: "Vest-Agder",
                5003: "Hordaland",
                8001: "Nordland",
                9006: "Troms",
                9501: "Finmark",
                1459: "Bergen"}

i = int(input("Enter a postal code: "))

if i in postal_codes.keys():
    print(postal_codes[i])
else:
    print("The postal code does not exist.")
