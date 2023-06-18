class Customer:
    name = ''
    lastname = ''
    age = 0
    def addCart(self):
        print('Added product to',self.name,self.lastname,"'s cart")
customer1 = Customer()
customer1.name = 'Soravis'
customer1.lastname = 'Amnuaysarn'
customer1.age = 21
customer1.addCart()

customer2 = Customer()
customer2.name = 'Jatturong'
customer2.lastname = 'Amnuaysarn'
customer2.age = 89
customer2.addCart()

customer3 = Customer()
customer3.name = 'Panya'
customer3.lastname = 'Amnuaysarn'
customer3.age = 98
customer3.addCart()

customer1 = Customer()
customer1.name = 'Sunee'
customer1.lastname = 'Amnuaysarn'
customer1.age = 74
customer1.addCart()