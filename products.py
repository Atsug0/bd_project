class Product:
    def __init__(self, product_id, amount, product_name, price):
        self.product_id = product_id
        self.amount = amount
        self.product_name = product_name
        self.price = price


    def product_id_exist(list, product_id ):
        for produit in list :
            if produit.product_id == product_id:
                return True
        return False
    
    def product_name_exist(list, product_name ):
        for produit in list :
            if produit.product_name == product_name:
                return True
        return False
    
    def stock_produit_epuise(product):
        if product.amount == 0:
            return True
        return False


ordinateur = Product(1, 100, "ordinateur portable", 800)

l = [ordinateur]
print(Product.product_id_exist(l, 1))
print(Product.stock_produit_epuise(ordinateur))

