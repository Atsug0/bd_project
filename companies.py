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


def is_budget_enough(list ,id, prix):
    for companie in list:
        if (companie.companie_id == id):
            return companie.budget > prix
    return False

def get_companies(list):
    res = []
    for companies in list:
        if companies.companie_name not in res:
            res.append(companies.companie_name)
    return res

def get_idc(list, companie_name):
    for companie in list:
        if (companie.companie_name == companie_name):
            return companie.companie_id
    return -1

def get_bud(list, companie_name):
    for companie in list:
        if (companie.companie_name == companie_name):
            return companie.budget
    return -1
    