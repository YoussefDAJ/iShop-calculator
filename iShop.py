basket = []
price = []
print("**** Welcome to the iShop calculator ****")
number = int(input("\nHow many items are there in your basket today?\n"))

for i in range(1, number + 1):
    element = input(f"\nPlease tell me the name of number {i}:\n")
    prix = int(input(f"\nWhat is the price of {element}\n"))
    basket.append(element)
    price.append(prix)

client = input("\nDo you want to see your basket items? \n").lower()
if client == "yes":
    print(basket)
    client = input("\nDo you want to know the price?\n").lower()
    if client == "yes":
        print(sum(price))
    else:
        print("Enter ok to quit")
else:
    print("Enter ok to quit")
