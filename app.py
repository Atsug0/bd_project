from tkinter import *

#page principal
root = Tk()

#personnaliser la fenetre
root.title("ManagerStock.exe")
root.geometry("500x400")
root.resizable(False,False)
root.minsize(480, 360)

def home_page():
    home_page = Frame(main_frame)

    lb = Label(home_page, text='HomePage', font=('Bold', 13),bg='white',fg='black')
    lb.pack()

    home_page.pack(pady=20)

def histo_page():
    histo_page = Frame(main_frame)

    lb = Label(histo_page, text='HistoPage', font=('Bold', 13),bg='white',fg='black')
    lb.pack()
    histo_page.pack(pady=20)

def new_page():
    new_page = Frame(main_frame)
    lb = Label(new_page, text='Gestion du stock', font=('Bold', 13),bg='white',fg='black')
    lb.pack()
    new_page.pack(pady=20)

def transac_page():
    transac_page = Frame(main_frame)
    lb = Label(transac_page, text='Créer une nouvelle transaction', font=('Bold', 13),bg='white',fg='black')
    lb.pack()
    transac_page.pack(pady=20)

def hide_indicators():
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
main_btn = Button(option_frame, text='Home', font=('Bold',15), fg='#158aff',bd=0,bg='#c3c3c3', command=lambda: indicate(main_indicate, home_page))
main_btn.place(x=15,y=50)

#button histoPage
historique_btn = Button(option_frame, text='Historique', font=('Bold',15), fg='#158aff',bd=0,background='#c3c3c3',command=lambda: indicate(histo_indicate, histo_page))
historique_btn.place(x=15,y=100)

#button gestion
nt_btn = Button(option_frame, text='Gestion du Stock', font=('Bold',15), fg='#158aff',bd=0,background='#c3c3c3',command=lambda: indicate(new_indicate, new_page))
nt_btn.place(x=15,y=150)


#button trans
nt_btn = Button(option_frame, text='Transaction', font=('Bold',15), fg='#158aff',bd=0,background='#c3c3c3',command=lambda: indicate(transac_indicate, transac_page))
nt_btn.place(x=15,y=200)

#home indicator
main_indicate = Label(option_frame, text='', bg='#c3c3c3')
main_indicate.place(x=3, y=50, width=5, height=30)

#histo indicator
histo_indicate = Label(option_frame, text='', bg='#c3c3c3')
histo_indicate.place(x=3, y=100, width=5, height=30)

#new indicator
new_indicate = Label(option_frame, text='', bg='#c3c3c3')
new_indicate.place(x=3, y=150, width=5, height=30)

#transac indicator
transac_indicate = Label(option_frame, text='', bg='#c3c3c3')
transac_indicate.place(x=3, y=200, width=5, height=30)


option_frame.pack(side= LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=200,height=400)

#Frame principal
main_frame = Frame(root, highlightbackground='black',highlightthickness=2)
main_frame.pack(side=LEFT)
indicate(main_indicate, home_page)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=500,bg='white')
root.mainloop()
