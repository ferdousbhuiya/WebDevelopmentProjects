# Python code​​​​​​‌​‌‌​‌‌​​‌‌​‌‌‌​​​​​‌‌‌​​ below
# Use print("messages...") to debug your solution.

# show_expected_result = False
# show_hints = False

class Cake:
    def __init__(self, flavor, price, slices):
        self.flavor = flavor
        self.price = price
        self.slices = slices
        self.remaining = slices

    def sell(self, count):
        if count <= 0:
            print('Cannot sell zero or negative slices!')
        elif self.remaining-count<0:
            print(f'Cannot sell more slices than we have ({self.remaining})!')
        else:
            self.remaining -= count
            print(f'Sold {count} slice(s) of {self.flavor} cake.')
            print(f'This cake has {self.remaining} slice(s) remaining.')

    def print_description(self):
        print(f'The {self.flavor} cake costs ${self.price} and is divided into {self.slices} slices.')

# Example usage
spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)

spice_cake.print_description()
spice_cake.sell(5)
spice_cake.sell(2)
spice_cake.sell(1)  # This should now correctly track the remaining slices

chocolate_cake.print_description()
chocolate_cake.sell(2)
chocolate_cake.sell(4)  # This should now correctly track the remaining slices
