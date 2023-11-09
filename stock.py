import psycopg2

# Informations de connexion à la base de données
db_params = {
    'host': 'localhost',  # Adresse IP du serveur PostgreSQL
    'database': 'stock_management',  # Nom de la base de données
    'user': 'postgres',  # Nom d'utilisateur PostgreSQL
    'password': ''  # Mot de passe PostgreSQL
}

def get_product_list():

    """
        Récupère toutes les informations de la table 'products'.

    """
    product_list = []

    try:
        connection = psycopg2.connect(**db_params)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        for row in rows:
            product_id, amount, product_name, price = row
            product = {
                'product_id': product_id,
                'amount': amount,
                'product_name': product_name,
                'price': price
            }
            product_list.append(product)

        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à la base de données:", error)

    return product_list


def get_transaction_list():

    """
        Récupère toutes les informations de la table 'transactions'.

    """
    transaction_list = []

    try:
        connection = psycopg2.connect(**db_params)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM transactions")
        rows = cursor.fetchall()

        for row in rows:
            transaction_id,product_id, amount, product_name,transaction_type,company_name,cost,company_id  = row
            transaction = {
                'transaction_id': transaction_id,
                'product_id': product_id,
                'company_id' : company_id,
                'amount': amount,
                'product_name': product_name,
                'transaction_type':transaction_type,
                'company_name': company_name,
                'cost': cost
            }
            transaction_list.append(transaction)

        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à la base de données:", error)

    return transaction_list



def get_companies_list():

    """
        Récupère toutes les informations de la table 'companies'.

    """
    companies_list = []

    try:
        connection = psycopg2.connect(**db_params)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM companies")
        rows = cursor.fetchall()

        for row in rows:
            company_id,company_name,budget  = row
            company = {
                'company_id' : company_id,
                'company_name': company_name,
                'budget': budget
            }
            companies_list.append(company)

        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à la base de données:", error)

    return companies_list

def update_amount_product(id_product :int,n : int):

    """
    Met à jour le stock du produit 'id_product' en fonction de 'n'.
    n : entier positif ou négatif

    """
    
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET amount = amount +%s WHERE product_id = %s ",(n,id_product))
        connection.commit()
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à la base de données:", error)


def update_budget_company(id_company : int , n : float):
    
    """
    Met à jour le stock de l'entreprise 'id_company' en fonction de 'n'.

    """

     
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute("UPDATE companies SET budget = budget +%s WHERE company_id = %s ",(n,id_company))
        connection.commit()
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à la base de données:", error)


products = get_product_list()
for product in products:
    print(product)



transactions = get_transaction_list()
for transaction in transactions:
    print(transaction)


companies = get_companies_list()
for company in companies:
    print(company)


#update_amount_product(1,-1)
#update_budget_company(1,-1)

