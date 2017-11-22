class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls('{} - franchise'.format(store.name))

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return ('{}, total stock price: {}'.format(store.name, store.stock_price()))


if __name__ == '__main__':
    store = Store("Test")
    store2 = Store("Amazon")
    store2.add_item("Keyboard", 160)

    x = Store.franchise(store)  # returns a Store with name "Test - franchise"
    print(x.name)
    assert (x.name == "Test - franchise")

    x = Store.franchise(store2)  # returns a Store with name "Amazon - franchise"
    print(x.name)
    assert (x.name == "Amazon - franchise")

    x = Store.store_details(store)  # returns "Test, total stock price: 0"
    print(x)
    assert (x == "Test, total stock price: 0")

    x = Store.store_details(store2)  # returns "Amazon, total stock price: 160"
    print(x)
    assert (x == "Amazon, total stock price: 160")