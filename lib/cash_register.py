#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, qty=1):
        self.last_transaction = price * qty
        # if title in self.items:
        #     pass
        # else:
        self.total+= price * qty
        for _ in range(qty):
            self.items.append(title)
        # print(self.items)
            # return self.items
    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total - (self.total * self.discount/100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        self.total -= self.last_transaction

# new_register = CashRegister()
# new_register.add_item("eggs", 1.99)
# new_register.add_item("tomato", 1.76)
# print(new_register.items)