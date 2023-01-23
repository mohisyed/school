class Apple:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        self.basket = None

    def display(self):
        print('The {} apple has weight {}'.format(self.color, self.weight))

    def add_to_basket(self, basket):
        if not self.basket:
            self.basket = basket
            basket.add_apple(self)
            print('The apple has been added to a basket {}'.format(basket.id))
        else:
            print('The apple is already in {}'.format(basket.id))


class Basket:
    def __init__(self, id):
        self.id = id
        self.apples = []

    def add_apple(self, apple):
        if apple not in self.apples:
            self.apples.append(apple)


red_apple = Apple(0.5, 'red')
green_apple = Apple(0.62, 'green')

print(red_apple.weight, red_apple.color)

b = Basket('Big Basket 1')
green_apple.add_to_basket(b)

