# import Product 
# import Companie
class Transactions:
    def __init__(self, transaction_id, product_id, amount, product_name, transaction_type, company_name) :
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.amount =amount
        self.product_name = product_name
        self.transaction_type = transaction_type
        self.company_name = company_name
            
    # def verify(transaction):
    #     if Companie.