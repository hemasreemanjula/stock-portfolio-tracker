stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 320,
    "AMZN": 3300
}

total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock} = ${investment}")
    else:
        print("Stock not found")

print("\nTotal Investment Value = $", total_investment)

choice = input("Save to file? (yes/no): ").lower()

if choice == "yes":
    file = open("portfolio.txt", "w")
    file.write("Total Investment Value = $" + str(total_investment))
    file.close()
    print("Data saved to portfolio.txt")