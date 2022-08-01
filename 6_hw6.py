prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
          "Blueberries": 1.0, "Raspberries": 1.0, "Apple": 1.75,
          "Pineapple": 3.5}


class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum(prices[i] for i in self.ingredients)
        self.price = self.cost * 2.5

    def get_cost(self):
        # total_beverage_cost = 0
        # for i in self.ingredients:
        #     total_beverage_cost = total_beverage_cost + prices[i]
        # return round(total_beverage_cost, 2)
        return f"${self.cost:.2f}"

    def get_price(self):
        return f"${self.price:.2f}"

    def get_name(self):
        self.ingredients.sort()
        beverage_name_list = []
        for i in range(len(self.ingredients)):
            if self.ingredients[i].endswith('berries'):
                beverage_name_list.append(self.ingredients[i].replace('berries', 'berry'))
            else:
                beverage_name_list.append(self.ingredients[i])
        beverage_name_string = " ".join(beverage_name_list)
        if len(self.ingredients)>1:
            return f"{beverage_name_string} Fusion"
        else:
            return f"{beverage_name_string} Smoothie"


beverage_1 = Beverage(["Banana"])
#beverage_1.get_name()

beverage_2 = Beverage(["Strawberries", "Banana", "Raspberries", "Mango"])
print(f"Name: {beverage_2.get_name()}")
print(f"Cost: {beverage_2.get_cost()}")
print(f"Price: {beverage_2.get_price()}")
print(f"Name: {beverage_1.get_name()}")
print(f"Cost: {beverage_1.get_cost()}")
print(f"Price: {beverage_1.get_price()}")
