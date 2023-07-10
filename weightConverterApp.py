user_weight = input("What is your weight? ")
mass_type = input("(K)g or (L)bs? ")
if mass_type == "K" or mass_type == "k":
    new_weight = (int(user_weight) * 2.2)
    print(int(new_weight))
elif mass_type == "L" or mass_type == "l":
    new_weight = (int(user_weight) // 2.2)
    print(int(new_weight))
else:
    print("Invalid mass type.")