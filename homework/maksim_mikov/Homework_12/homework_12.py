class Flower:

    def __init__(self, title, colour, stalk_length, freshness, price):
        self.title = title
        self.colour = colour
        self.stalk_length = stalk_length
        self.freshness = freshness
        self.price = price


class Bouquet:

    def __init__(self):
        self.flowers = []

    def add_flower(self, flow):
        self.flowers.append(flow)

    def total_cost(self):
        return sum(fl.price for fl in self.flowers)

    def sort_by_attribute(self, attribute):
        return sorted(self.flowers, key=lambda fl: getattr(fl, attribute))

    def time_life_bouquet(self):
        return sum(fl.freshness for fl in self.flowers) / len(self.flowers)

    def find_by_timelife(self, min_timelife):
        return [fl for fl in self.flowers if fl.freshness >= min_timelife]

    def find_by_price(self, max_price):
        return [fl for fl in self.flowers if fl.price <= max_price]


class PotFlower(Flower):

    def __init__(self, title, colour, stalk_length, freshness, price, type_pot):
        super().__init__(title, colour, stalk_length, freshness, price)
        self.type_pot = type_pot


rose = Flower("Rose", "red", 80, 5, 120)
lily = Flower("Lily", "white", 90, 10, 180)
peony = Flower("Peony", "white", 70, 12, 80)
iris = Flower("Iris", "violet", 50, 7, 100)
tulip = Flower("Tulip", "red", 40, 7, 60)

firstBouquet = Bouquet()
firstBouquet.add_flower(rose)
firstBouquet.add_flower(lily)
firstBouquet.add_flower(peony)
firstBouquet.add_flower(iris)
firstBouquet.add_flower(tulip)

print(f"Total cost of Bouquet {firstBouquet.total_cost()}")
print(f"Time life of Bouquet {firstBouquet.time_life_bouquet()}")

sorted_by_freshness = firstBouquet.sort_by_attribute("freshness")
for flo in sorted_by_freshness:
    print(f"{flo.title} with freshness {flo.freshness}")

sorted_by_price = firstBouquet.sort_by_attribute("price")
for flo in sorted_by_price:
    print(f"{flo.title} with price {flo.price}")

flower_with_long_life = firstBouquet.find_by_timelife(7)
for flower in flower_with_long_life:
    print(f"{flower.title} has a life span of {flower.freshness} days")

flower_with_min_price = firstBouquet.find_by_price(100)
for flower in flower_with_min_price:
    print(f"{flower.title} has a price {flower.price} ")
