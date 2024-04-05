class User:
    def __init__(self, user_id, name, date_of_birth, role, active, ready_to_order=True):
        self.user_id = user_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.role = role  # 0 for admin, 1 for shopper
        self.active = active  # 0 for not active, 1 for active
        self.ready_to_order = ready_to_order # 0 for not ready, 1 for ready
        self.basket = {} #dictionary for the basket

    def add_to_basket(self, product_id, quantity):
        self.basket[int(product_id)] = int(quantity)

    # this is for printing after loading
    def display_user_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Role: {'Admin' if self.role == 0 else 'Shopper'}")
        print(f"Active: {'Yes' if self.active == 1 else 'No'}")
        print(f"Ready to Order: {'Yes' if self.ready_to_order else 'No'}")
        print("Basket:")
        for product_id, quantity in self.basket.items():
            print(f"  Product ID: {product_id}, Quantity: {quantity}")
        print("-----------------------------------------------------")

        # this is for loading purposes
    @classmethod
    def from_text(cls, text):
        data = text.strip().split(';')

        user_id, name, date_of_birth, role, active, ready_to_order, *basket_data = data
        role = int(role)
        active = int(active)
        ready_to_order = int(ready_to_order) == 1  # Convert "ready_to_order" to True (1) or False (0)

        user = cls(int(user_id), name, date_of_birth, role, active, ready_to_order)

        if basket_data:  # Check if basket data is available
            for item in basket_data:
                parts = item.split(':')
                if len(parts) == 2:
                    product_id, quantity = parts
                    user.basket[int(product_id)] = int(quantity)

        return user
