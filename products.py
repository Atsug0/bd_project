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

def stock_produit_epuise(list, product_name):
    for product in list:
        if (product.product_name == product_name):
            return not product.amount == 0
    return False

def get_lst(list):
    res = []
    for product in list:
        if product.product_name not in res:
            res.append(product.product_name)
    return res

def get_id(list, product_name):
    for product in list:
        if (product.product_name == product_name):
            return product.product_id
    return -1

def get_price(list, product_name):
    for product in list:
        if (product.product_name == product_name):
            return product.price
    return -1

def get_amoutp(list, product_name):
    for product in list:
        if (product.product_name == product_name):
            return product.amount
    return -1


