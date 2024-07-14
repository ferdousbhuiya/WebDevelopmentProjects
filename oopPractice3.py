# # class Item:
# #     def __init__(self, item_type, price):
# #         self.item_type = item_type
# #         self.price = price


# # class Cake(Item):
# #     def __init__(self, item_type, price):
# #         super().__init__(item_type, price)

# # cake = Cake("cake",10)

# class Item:
#     def __init__(self, item_type, price):
#         self.item_type = item_type
#         self.price = price

#     def __str__(self):
#         return f"{self.item_type} costs {self.price}"

# class Cake(Item):
#     def __init__(self, flavor, price, slices):
#         super().__init__("cake", price)
#         self.flavor = flavor
#         self.slices = slices
#         self.remaining_slices = slices

#     def sell_slice(self, count):
#         if count <= 0:
#             print('Cannot sell zero or negative slices!')
#         elif count > self.remaining_slices:
#             print(f'Cannot sell more slices than we have ({self.remaining_slices})!')
#         else:
#             self.remaining_slices -= count
#             print(f'Sold {count} slice(s). {self.remaining_slices} slice(s) remaining.')

#     def __str__(self):
#         return f"{self.flavor} cake costs {self.price} and has {self.remaining_slices}/{self.slices} slices remaining."

# # Create a cake object
# cake = Cake("Chocolate", 20, 8)

# # Print the description of the cake
# print(cake)

# # Sell some slices
# cake.sell_slice(3)
# print(cake)

# cake.sell_slice(6)  # This should show an error as it exceeds the remaining slices
# print(cake)

# cake.sell_slice(2)
# print(cake)


# Python code​​​​​​‌​‌‌​‌‌​​‌‌​‌‌‌​‌​‌​‌‌​​‌ below
# Use print("messages...") to debug your solution.

# Python code​​​​​​‌​‌‌​‌‌​‌​​‌​‌‌‌‌​​‌‌​​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True

class Item:
    def __init__(self, item_type, price):
        self.item_type = item_type
        self._price = price

    @property
    def price(self):
        return self._price

class Cake(Item):
    def __init__(self, flavor, price, slices):
        super().__init__("cake", price)
        self.flavor = flavor
        self.slices = slices
        self.slices_remaining = slices
        

    def sell(self, count): 
        if(count <= 0):
            return "Cannot sell zero or negative slices!"
        elif(self.slices_remaining - count < 0):
            return f"Cannot sell more slices than we have ({self.slices_remaining})!"
        else:
            self.slices_remaining -= count
            return f"This cake has {self.slices_remaining} slices remaining."

    def __eq__(self, other):
        return self.slices_remaining *(self._price / self.slices)==other.slices_remaining*(other.price / other.slices)

    def __gt__(self, other):
        return self.slices_remaining *(self._price / self.slices) > other.slices_remaining*(other.price / other.slices)

    def __lt__(self, other):
        return self.slices_remaining *(self._price / self.slices) < other.slices_remaining*(other.price / other.slices)

spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)

spice_cake.sell(3)
chocolate_cake.sell(4)