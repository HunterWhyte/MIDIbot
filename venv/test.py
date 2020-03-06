def cost(n_lemons, cost_per_lemon):
    return (n_lemons * cost_per_lemon)


def revenue(donations, n_lemonades, price_per_lemonade):
    return ((n_lemonades * price_per_lemonade) + donations)


def profit(donations, n_lemonades, price_per_lemonade, n_lemons, cost_per_lemon):
    return (revenue(donations, n_lemonades, price_per_lemonade) - cost(n_lemons, cost_per_lemon))


n_lemons = int(input("How many lemons were used ?: "))
cost_per_lemon = float(input("What was the cost per lemon ( in dollars )?: "))
n_lemonades = int(input("How many lemonades were sold ?: "))
price_per_lemonade = float(input("What was the selling price of one lemonade ( in dollars )?: "))
donations = float(input("How much money did you receive in donations ( in dollars )?: "))

profit = profit(donations, n_lemonades, price_per_lemonade, n_lemons, cost_per_lemon)

print("Revenue: $" + str(revenue(donations, n_lemonades, price_per_lemonade)))
print("Cost: $" + str(cost(n_lemons, cost_per_lemon)))
print("Profit: $" + str(profit))
