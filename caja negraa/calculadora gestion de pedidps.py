class OnlineSalesSystem:
    def __init__(self):
        self.users = {}
        self.products = {}
        self.orders = []

    def register_user(self, username, email, password):
        if not username or not email or not password:
            raise ValueError("Invalid input")
        self.users[username] = {'email': email, 'password': password}

    def add_product(self, product_id, stock):
        if not product_id:
            raise ValueError("Product ID cannot be empty")
        self.products[product_id] = {'stock': stock}

    def create_order(self, username, product_id, quantity):
        if username not in self.users:
            raise ValueError("User not registered")
        if product_id not in self.products:
            raise ValueError("Product not available")
        if self.products[product_id]['stock'] < quantity:
            raise ValueError("Insufficient stock")
        order = {'username': username, 'product_id': product_id, 'quantity': quantity, 'status': 'created'}
        self.orders.append(order)
        return order

    def process_payment(self, order_id, payment_successful):
        if order_id >= len(self.orders) or order_id < 0:
            raise ValueError("Invalid order ID")
        if not payment_successful:
            self.orders[order_id]['status'] = 'payment failed'
            return
        self.orders[order_id]['status'] = 'paid'
        self.products[self.orders[order_id]['product_id']]['stock'] -= self.orders[order_id]['quantity']

    def ship_order(self, order_id):
        if self.orders[order_id]['status'] != 'paid':
            raise ValueError("Order not paid")
        self.orders[order_id]['status'] = 'shipped'

    def deliver_order(self, order_id):
        if self.orders[order_id]['status'] != 'shipped':
            raise ValueError("Order not shipped")
        self.orders[order_id]['status'] = 'delivered'

    def cancel_order(self, order_id):
        self.orders[order_id]['status'] = 'cancelled'

# Ejemplo de pruebas
system = OnlineSalesSystem()
system.register_user("user1", "user1@example.com", "password123")
system.add_product("product1", 10)

order = system.create_order("user1", "product1", 2)
print(order)  # {'username': 'user1', 'product_id': 'product1', 'quantity': 2, 'status': 'created'}

system.process_payment(0, True)
print(system.orders[0])  # {'username': 'user1', 'product_id': 'product1', 'quantity': 2, 'status': 'paid'}

system.ship_order(0)
print(system.orders[0])  # {'username': 'user1', 'product_id': 'product1', 'quantity': 2, 'status': 'shipped'}

system.deliver_order(0)
print(system.orders[0])  # {'username': 'user1', 'product_id': 'product1', 'quantity': 2, 'status': 'delivered'}
