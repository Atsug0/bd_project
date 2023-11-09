from tkinter import *

class Products:
    def __init__(self, product_id, amount, product_name, price):
        self.product_id = product_id
        self.amount = amount
        self.product_name = product_name
        self.price = price

# ordinateur = Products(1, 100, "ordinateur portable", 800)
class Transactions:
    def __init__(self, transaction_id, product_id, amount, product_name, transaction_type, company_name) :
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.amount =amount
        self.product_name = product_name
        self.transaction_type = transaction_type
        self.company_name = company_name

class Companies :
    def __init__(self, company_id, company_name, budget):
        self.company_id =company_id
        self.company_name = company_name
        self.budget = budget

# Création de listes d'objets
products_list = [Products(i, i*10, f"Product{i}", i*100) for i in range(1, 11)]
transactions_list = [Transactions(i, i, i*5, f"Transaction{i}", "Sale", f"Company{i}") for i in range(1, 11)]
companies_list = [Companies(i, f"Company{i}", i*1000) for i in range(1, 11)]

#def create_table(data_list, columns):
#    root = tk.Tk()
#    root.title(f"Tableau de {columns}")
#
#    tree = ttk.Treeview(root)
#    tree["columns"] = columns

#    tree.heading("#0", text="", anchor="w")
#    tree.column("#0", anchor="w", width=0)

#    for col in tree["columns"]:
#        tree.heading(col, text=col)
#        tree.column(col, anchor="center")

#    for item in data_list:
#        values = [getattr(item, col.lower()) for col in columns]
#        tree.insert("", "end", values=values)

#    tree.pack()

#    root.mainloop()

# Affichage des tableaux
#create_table(products_list, ["Product_ID", "Amount", "Product_Name", "Price"])
#create_table(transactions_list, ["Transaction_ID", "Product_ID", "Amount", "Product_Name", "Transaction_Type", "Company_Name"])
#create_table(companies_list, ["Company_ID", "Company_Name", "Budget"])