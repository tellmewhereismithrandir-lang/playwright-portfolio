class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = ".inventory_item"
        self.sort_dropdown = ".product_sort_container"
        self.price_items = ".inventory_item_price"
        self.add_backpack_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"

    def get_item_count(self):
        return self.page.locator(self.inventory_items).count()

    def sort_by(self, option):
        self.page.select_option(self.sort_dropdown, option)

    def get_prices(self):
        prices = self.page.locator(self.price_items).all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def add_backpack_to_cart(self):
        self.page.click(self.add_backpack_button)

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).text_content()