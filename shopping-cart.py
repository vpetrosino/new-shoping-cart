class cart:
   
    def __init__(self, name):
        self.name = name
        self.list = []


    def showCart(self):
        print(self.name + ' ' + 'Has this in their cart: ')
        # looping through the items in cart
        for item in self.list:
            print(item)
        print('\n \n')


    def addItem(self, item):
        self.list.append(item)


    def delItem(self, item):
        self.list.remove(item)


    def clearCart(self):
        self.list.clear()



user_name = input('Who is shopping today? ')



cart = cart(user_name)

while True:
    instructions = """The User has 5 commands:
    Show Cart
    Add Item
    Del Item
    Clear Cart
    Quit
    \n
    \n
    """

    print(instructions)
  
    user_choice = input('What would ' + user + ' like to do today? ')

   
    if user_choice.lower() == 'show cart':
        cart.showCart()

    elif user_choice.lower() == 'add item':
        item = input('What would you like to add to the cart? ')
        if item.lower() == "quit":
            cart.showCart()
            break
        cart.addItem(str(item))

    elif user_choice.lower() == 'del item':
        item = input('What would you like to delete from the cart? ')
        if item.lower() == "quit":
            cart.showCart()
            break
        cart.delItem(item)

    elif user_choice.lower() == "clear cart":
        cart.clearCart()

    elif user_choice.lower() == "quit":
        cart.showCart()
        break

    else:
        print('Please use a defined command.')
