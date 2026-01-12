class Economy:
    def __init__(self):
        # Supply levels
        self.supply = {
            "food": 100,
            "tools": 40
        }

        # Base prices
        self.prices = {
            "food": 10,
            "tools": 25
        }

    def update_prices(self, demand):
        """
        Prices rise when demand > supply,
        fall when supply > demand.
        """
        for item in self.prices:
            if demand[item] > self.supply[item]:
                self.prices[item] += 2
            else:
                self.prices[item] -= 1

            self.prices[item] = max(self.prices[item], 1)

    def consume(self, item, amount):
        self.supply[item] -= amount
        self.supply[item] = max(self.supply[item], 0)

    def produce(self, item, amount):
        self.supply[item] += amount
