class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self, item_name, qty, unit_price=0.0):
        item = (item_name, qty, unit_price)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            qty = item[1]
            unit_price = item[2]
            total += qty * unit_price
        return total

    def show_cart(self):
        print("\nCart Contents:")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.2f}")
        print(f"Subtotal: Ksh {self.calculate_total():.2f}")


# Subclass that applies a discount
class DiscountedCart(ShoppingCart):
    def _init_(self, discount_rate):
        super()._init_()
        self.discount_rate = discount_rate

    def calculate_total(self):
        total = super().calculate_total()
        discount = total * self.discount_rate
        return total - discount


# Subclass that applies tax
class TaxedCart(ShoppingCart):
    def _init_(self, tax_rate):
        super()._init_()
        self.tax_rate = tax_rate

    def calculate_total(self):
        total = super().calculate_total()
        tax = total * self.tax_rate
        return total + tax


# Polymorphic function
def checkout(cart: ShoppingCart):
    cart.show_cart()
    print(f"Final Total: Ksh {cart.calculate_total():.2f}\n")


# ==== MAIN TESTING BLOCK ====
cart = ShoppingCart()
cart.add_item(item_name="Kiwi", qty=100, unit_price=5.00)
cart.add_item(item_name="Papaya", qty=200, unit_price=3.50)
cart.add_item(item_name="Mango", qty=78, unit_price=6.00)

print(">>> ORDINARY CART <<<")
checkout(cart)

print(">>> DISCOUNTED CART (15%) <<<")
disc_cart = DiscountedCart(discount_rate=0.15)
disc_cart.add_item("Kiwi", 100, 5.00)
disc_cart.add_item("Papaya", 200, 3.50)
disc_cart.add_item("Mango", 78, 6.00)
checkout(disc_cart)

print(">>> TAXED CART (12%) <<<")
taxed_cart = TaxedCart(tax_rate=0.12)
taxed_cart.add_item("Kiwi", 100, 5.00)
taxed_cart.add_item("Papaya", 200, 3.50)
taxed_cart.add_item("Mango", 78, 6.00)
checkout(taxed_cart)