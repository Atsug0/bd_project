# import Product 
# import Companie
class Transactions:
    def __init__(self, transaction_id,product_id, amount, product_name, company_name, cost,company_id ) :
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.amount =amount
        self.product_name = product_name
        self.company_name = company_name
        self.cost = cost
        self.company_id = company_id
            
    # def verify(transaction):
    #     if Companie.