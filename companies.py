class Companie :
    def __init__(self, companie_id, companie_name, budget):
        self.companie_id =companie_id
        self.companie_name = companie_name
        self.budget = budget
        

    def companie_exist(companies, companie_id):
        for companie in companie:
            if companie.companie_id == companie_id:
                return True
        return False


    def is_budget_enough(companie, prix):
        return companie.budget > prix