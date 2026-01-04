import time
emeralds = 5
bread = 0
potatoes = 130
beetroots = 75
carrots = 110
wheat = 100
print("Welcome to MC Trade Sim!")
while True:
    print(f"\nYou have {emeralds} emerald(s),")
    print(f"{bread} bread loaf(s),")
    print(f"{potatoes} potato(es),")
    print(f"{beetroots} beetroot(s),")
    print(f"{carrots} carrot(s),")
    print(f"{wheat} bundle(s) of wheat.")
    print("22 Carrots / 20 Wheat / 26 Potatoes / 15 Beetroots = 1 emerald.")
    print("1 emerald = 6 bread loaves.")
    action = input("Press p to sell potatoes, b for beetroots, c for carrots, w for wheat, e to buy bread, or q to quit: ").lower()
    if action == "p":
        if potatoes >= 26:
            potatoes -= 26
            emeralds += 1
            print("Sold 26 potatoes for 1 emerald.")
            print("Wait for 5 seconds.")
        else:
            print("Not enough potatoes to sell.")
    elif action == "b":
        if beetroots >= 15:
            beetroots -= 15
            emeralds += 1
            print("Sold 15 beetroots for 1 emerald.")
            print("Wait for 5 seconds.")
        else:
            print("Not enough beetroots to sell.")
    elif action == "c":
        if carrots >= 22:
            carrots -= 22
            emeralds += 1
            print("Sold 22 carrots for 1 emerald.")
            print("Wait for 5 seconds.")
        else:
            print("Not enough carrots to sell.")
    elif action == "w":
        if wheat >= 20:
            wheat -= 20
            emeralds += 1
            print("Sold 20 wheat for 1 emerald.")
            print("Wait for 5 seconds.")
        else:
            print("Not enough wheat to sell.")
    elif action == "e":
        if emeralds >= 1:
            emeralds -= 1
            bread += 6
            print("Bought 6 bread loaves for 1 emerald.")
            print("Wait for 5 seconds.")
        else:
            print("Not enough emeralds to buy bread.")
    elif action == "q":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice.")
    time.sleep(5)
    potatoes += 3
    beetroots += 3
    wheat += 3
    carrots += 3
