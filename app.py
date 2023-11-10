from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style, Treeview
from companies import Companie
from products import Product
from transactions import Transactions


# Création de listes d'objets
products_list = [Product(i, i*10, f"Product{i}", i*100) for i in range(1, 11)]
transactions_list = [Transactions(i, i, i*5, f"Transaction{i}", f"Company{i}") for i in range(1, 11)]
companies_list = [Companie(i, f"Company{i}", i*1000) for i in range(1, 11)]

#page principal
root = Tk()

#personnaliser la fenetre
root.title("ManagerStock.exe")
root.geometry("900x400")
root.resizable(False,False)
root.minsize(1000, 360)


def home_page():
    home_page = Frame(main_frame,bg='white')
    lb = Label(home_page, text='Le Stock', font=('Bold', 13),bg='white',fg='black')
    lb.pack()
    tree = Treeview(home_page,style="mystyle.Treeview")
    tree["columns"] = ("ID", "Amount", "Name", "Price")
    style = Style()
    style.theme_use("clam")

    style.configure("mystyle.Treeview", foreground="black", bordercolor="black", background="white", bg="white")

    tree.heading("#0", text="", anchor="w")
    tree.column("#0", anchor="w", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center",width=80)

    for product in products_list:
        tree.insert("", "end", values=(product.product_id, product.amount, product.product_name, product.price))
    tree.pack(pady=10)

    home_page.pack(pady=20)

def histo_page():
    histo_page = Frame(main_frame,bg='white')

    lb = Label(histo_page, text='Historique des transactions', font=('Bold', 13),bg='white',fg='black')
    lb.pack()
    tree = Treeview(histo_page,style="mystyle.Treeview")
    tree["columns"] = ("Transaction_ID", "Product_ID", "Amount", "Product_Name", "Company_Name")
    style = Style()
    style.theme_use("clam")

    style.configure("mystyle.Treeview", foreground="black", bordercolor="black", background="white", bg="white")

    tree.heading("#0", text="", anchor="w")
    tree.column("#0", anchor="w", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center",width=100)

    for transaction in transactions_list:
        tree.insert("", "end", values=(transaction.transaction_id, transaction.product_id, transaction.amount, transaction.product_name, transaction.company_name))
    tree.pack(pady=10)
    histo_page.pack(pady=20)

def validate(selected_option, counter_value):
    try:
        counter_value.get()
        if not selected_option or counter_value.get() <= 0:
        # Afficher une erreur et rafraîchir la page
            messagebox.showerror("Erreur", "Veuillez sélectionner une option ou un compteur valide.")
        else:
            # Effectuer une action avec les valeurs sélectionnées
            messagebox.showinfo("Succès", f"il y a {counter_value.get()} {selected_option}s qui ont été ajouté au stock")
    except TclError :
        messagebox.showerror("Erreur", "Veuillez sélectionner une option ou un compteur valide.")

def validate2(selected_option, selected_option2, counter_value):
    try:
        counter_value.get()
        if not selected_option or not selected_option2 or counter_value.get() <= 0:
        # Afficher une erreur et rafraîchir la page
            messagebox.showerror("Erreur", "Veuillez sélectionner une option ou un compteur valide.")
        else:
            # Effectuer une action avec les valeurs sélectionnées
            messagebox.showinfo("Succès", f"il y a {counter_value.get()} {selected_option}s qui ont été ajouté au stock")
    except TclError :
        messagebox.showerror("Erreur", "Veuillez sélectionner une option ou un compteur valide.")
    

def part_page():
    part_page = Frame(main_frame,bg='white')
    lb = Label(part_page, text='Nos partenaires', font=('Bold', 13),bg='white',fg='black')
    lb.pack()
    tree = Treeview(part_page,style="mystyle.Treeview")
    tree["columns"] = ("Company_ID", "Company_Name", "Budget")
    style = Style()
    style.theme_use("clam")

    style.configure("mystyle.Treeview", foreground="black", bordercolor="black", background="white", bg="white")

    tree.heading("#0", text="", anchor="w")
    tree.column("#0", anchor="w", width=0)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center",width=100)

    for companies in companies_list:
        tree.insert("", "end", values=(companies.companie_id, companies.companie_name, companies.budget,))
    tree.pack(pady=10)
    part_page.pack(pady=20)

def new_page():
    new_page = Frame(main_frame, bg="white")
    lb = Label(new_page, text='Gestion du stock', font=('Bold', 13),bg='white',fg='black')
    lb.pack()

    selected_option = StringVar()
    counter_value = IntVar()

    # Menu déroulant
    select_label = Label(new_page, text="Choisir le produit : (minimum 1)",font=('Bold', 13),bg='white',fg='black')
    select_label.pack(pady=20)
    options = ["Company_ID", "Company_Name", "Budget"]
    option_menu = OptionMenu(new_page, selected_option, *options)
    option_menu.configure(background="white", fg="black")
    option_menu.pack(pady=10)
    new_page.update() 

    # Compteur
    counter_label = Label(new_page, text="Choisir la quantité :",font=('Bold', 13),bg='white',fg='black')
    counter_label.pack()
    # Utilisation d'une méthode pour la validation
    validate_method = (new_page.register(validate_entry), '%P')
    counter_entry = Entry(new_page, textvariable=counter_value, width=2,validate='key', validatecommand=validate_method)
    # Utilisation d'une méthode pour la validation
    counter_entry.pack(pady=5)

    # Bouton Valider
    
    validate_button = Button(new_page, text="Valider", command=lambda: validate(selected_option.get(), counter_value),bg='white',bd=0,background="white")
    validate_button.pack(pady=10)
    
    new_page.pack(pady=20)

def validate_entry(new_value):
    # La méthode de validation pour s'assurer que le contenu est un entier
    if new_value == "":
        return True  # La saisie est vide, donc la validation est réussie
    try:
        int(new_value)
        return True
    except ValueError:
        return False
        
def transac_page():
    transac_page = Frame(main_frame, bg="white")
    lb = Label(transac_page, text='Créer une nouvelle transaction', font=('Bold', 13),bg='white',fg='black')
    lb.pack()
    selected_option = StringVar()
    selected_option2 = StringVar()
    counter_value = IntVar()

    # Menu déroulant
    select_label = Label(transac_page, text="Choisir le produit :",font=('Bold', 13),bg='white',fg='black')
    select_label.pack(pady=20)
    options = ["Company_ID", "Company_Name", "Budget"]
    option_menu = OptionMenu(transac_page, selected_option, *options)
    option_menu.configure(background="white", fg="black")
    option_menu.pack(pady=10)

    # Compteur
    counter_label = Label(transac_page, text="Choisir la quantité : (minimum 1)",font=('Bold', 13),bg='white',fg='black')
    counter_label.pack()
    # Utilisation d'une méthode pour la validation
    validate_method = (transac_page.register(validate_entry), '%P')
    counter_entry = Entry(transac_page, textvariable=counter_value, width=2,validate='key', validatecommand=validate_method)
    # Utilisation d'une méthode pour la validation
    counter_entry.pack(pady=5)

    # Bouton Valider
     # Menu déroulant
    select2_label = Label(transac_page, text="Choisir le partenaire :",font=('Bold', 13),bg='white',fg='black')
    select2_label.pack(pady=20)
    options2 = ["Company_ID", "Company_Name", "Budget"]
    option2_menu = OptionMenu(transac_page, selected_option2, *options2)
    option2_menu.configure(background="white", fg="black")
    option2_menu.pack(pady=10)
    
    validate_button = Button(transac_page, text="Valider", command=lambda: validate2(selected_option.get(), selected_option2.get(),counter_value),bg='white',bd=0,background="white")
    validate_button.pack(pady=10)
    
    transac_page.update_idletasks()
    transac_page.pack(pady=20)

def hide_indicators():
    part_indicate.config(bg='#c3c3c3')
    main_indicate.config(bg='#c3c3c3')
    new_indicate.config(bg='#c3c3c3')
    histo_indicate.config(bg='#c3c3c3')
    transac_indicate.config(bg='#c3c3c3')

def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb: Label, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_page()
    page()



#Nav bar
option_frame = Frame(root, bg='#c3c3c3')

#button MainPage
main_btn = Button(option_frame, text='Le stock', font=('Bold',15), fg='#158aff',bd=0,bg='#c3c3c3', command=lambda: indicate(main_indicate, home_page))
main_btn.place(x=15,y=50)

#button histoPage
historique_btn = Button(option_frame, text='Historique', font=('Bold',15), fg='#158aff',bd=0,background='#c3c3c3',command=lambda: indicate(histo_indicate, histo_page))
historique_btn.place(x=15,y=100)

#button partenaire
part_btn = Button(option_frame, text='Partenaires', font=('Bold',15), fg='#158aff',bd=0,background='#c3c3c3',command=lambda: indicate(part_indicate, part_page))
part_btn.place(x=15,y=150)

#button gestion
nt_btn = Button(option_frame, text='Gestion du Stock', font=('Bold',15), fg='#158aff',bd=0,background='#c3c3c3',command=lambda: indicate(new_indicate, new_page))
nt_btn.place(x=15,y=200)


#button trans
nt_btn = Button(option_frame, text='Transaction', font=('Bold',15), fg='#158aff',bd=0,background='#c3c3c3',command=lambda: indicate(transac_indicate, transac_page))
nt_btn.place(x=15,y=250)

#home indicator
main_indicate = Label(option_frame, text='', bg='#c3c3c3')
main_indicate.place(x=3, y=50, width=5, height=30)

#histo indicator
histo_indicate = Label(option_frame, text='', bg='#c3c3c3')
histo_indicate.place(x=3, y=100, width=5, height=30)

#part indicator
part_indicate = Label(option_frame, text='', bg='#c3c3c3')
part_indicate.place(x=3, y=150, width=5, height=30)

#new indicator
new_indicate = Label(option_frame, text='', bg='#c3c3c3')
new_indicate.place(x=3, y=200, width=5, height=30)

#transac indicator
transac_indicate = Label(option_frame, text='', bg='#c3c3c3')
transac_indicate.place(x=3, y=250, width=5, height=30)


option_frame.pack(side= LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=200,height=400)

#Frame principal
main_frame = Frame(root, highlightbackground='black',highlightthickness=2)
main_frame.pack(side=LEFT)
indicate(main_indicate, home_page)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=700,bg='white')
root.configure(background='white')
root.mainloop()
