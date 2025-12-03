# Product Class

class Product:
  def __init__(self, name: str, price: float, stock: int):
    self.name = name
    self.price = price
    self.stock = int(stock)

    #Attempt to purchase `quantity` units.
    #If enough stock, reduce stock and return total price.
    #If not enough stock, raise ValueError.

  def purchase (self, quantity: int) -> float:
    quantity = int(quantity)
    if quantity <= 0:
      raise ValueError("Quantity must be positive")
    if quantity > self.stock:
      raise ValueError(f"Insufficient stock for {self.name}, Requested quantity {quantity}, but available quantity is {self.stock}.")
    self.stock -= quantity
    return self.price * quantity

  def restock(self,quantity: int): #Adds quantity units to the stock
    quantity = int(quantity)
    if quantity <= 0:
      raise ValueError("Restock Quantity must be positive")
    self.stock += quantity

  def display_info(self):
    #Returns a redable product summary (string).
    return f"Product(name={self.name}, price={self.price:.2f}, stock={self.stock})"

  def __repr__(self):
    return f"Product({self.name!r}, {self.price}, {self.stock})"

# Customer Class

class Customer:
  def __init__(self, name: str, customer_id: str):
    self.name = name
    self.customer_id = customer_id
    self.cart = {} #Cart: Dictionary mapping product instance -> quantity

  def add_to_cart(self, product: Product, quantity: int):
    quantity = int(quantity)
    if quantity <= 0:
      raise ValueError("Quantity must be positive")
    current = self.cart.get(product, 0)
    self.cart[product] = current + quantity
    print(f"Added {quantity} * {product.name} to {self.name}'s cart")

  def remove_from_cart(self, product: Product, quantity: int = None):

        #Remove `quantity` of product from the cart.
        #If quantity is None, remove the product entirely.            

    if product not in self.cart:
      raise ValueError(f"{product.name} is not in {self.name}'s cart")

    if quantity is None or quantity <= 0:
      del self.cart[product]
      print(f"Removed all {product.name} from {self.name}'s cart")

    quantity = int(quantity)
    if quantity <= 0:
      raise ValueError("Quantity must be positive")

    if quantity >= self.cart[product]:
      del self.cart[product]
      print(f"Removed all {product.name} from {self.name}'s cart")
    else:
      self.cart[product] -= quantity
      print(f"Removed {quantity} * {product.name} from {self.name}'s cart")

  def checkout(self):

    """
        Attempt to purchase all items in the cart.
        - First check availability for all items.
        - If any item lacks stock, abort and report which item failed.
        - If all available, charge total, reduce stocks, clear cart, and return total.
        """

    if not self.cart:
      print("Your Cart is empty.")
      return 0.0
    
    # Check Availability 
    for product, qty in self.cart.items():
      if qty > product.stock:
        print(f"Checkout failed: {product.name} has only {product.stock} units, but {qty} requested.")
        return -1
    
    # All Available Perform purchase
    total = 0.0
    for product, qty in self.cart.items():
      total += product.purchase(qty) #reduces product.stock
    self.cart.clear()
    print(f"Checkout successful. Total: {total:.2f}")
    return total

  def display_cart(self):
    if not self.cart:
      return "Cart is empty"
    lines = []

    for product, qty in self.cart.items():
      lines.append(f"{product.name} * {qty} @ {product.price:.2f} each = {product.price * qty:.2f}")
    return "\n".join(lines)
  
  def display_info(self):
    return f"Customer(name={self.name}, customer_id={self.customer_id})"

  def __repr__(self):
    return f"Customer({self.name!r}, {self.customer_id!r})"



# -------------------------
# Demo / Test the system
# -------------------------
if __name__ == "__main__":
    # Create some products
    p1 = Product("T-shirt", 399.0, 10)
    p2 = Product("Mug", 199.0, 5)
    p3 = Product("Notebook", 99.0, 2)

    # Create a customer
    alice = Customer("Alice", "C001")

    # Show products
    print(p1.display_info())
    print(p2.display_info())
    print(p3.display_info())
    print()

    # Add to cart
    alice.add_to_cart(p1, 2)      # 2 T-shirts
    alice.add_to_cart(p2, 1)      # 1 Mug
    alice.add_to_cart(p3, 2)      # 2 Notebooks (exact stock)
    print("\nCart contents:")
    print(alice.display_cart())
    print()

    # Try checkout (should succeed)
    alice.checkout()
    print()

    # Stocks after purchase
    print("Stocks after checkout:")
    print(p1.display_info())
    print(p2.display_info())
    print(p3.display_info())
    print()

    # Add something exceeding stock
    alice.add_to_cart(p2, 10)  # only 4 left after prior purchase
    print("\nAttempt checkout with insufficient stock:")
    alice.checkout()  # will fail and return -1
    print()

    # Restock and checkout again
    p2.restock(10)
    print("After restock:", p2.display_info())
    alice.add_to_cart(p2, 10)
    alice.checkout()
    print()
