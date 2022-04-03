import cgi
from cgitb import html, text
import email
from ssl import _PasswordType
from tkinter import*
import sqlite3
from turtle import width 
  
root = Tk()
root.title('login')
root.geometry('450*450')

#Database

conn=sqlite3.connect('login.db')
c= conn.cursor
c.execute("""CREATE TABLE user(
            prenom text,
            nom text,
            eemail text,
            password text
            }""")

def submit():
    conn = sqlite3.connect('login.db')
    c=conn.cursor

    c.execute("INSERT INTO user VALUES (:prenom, :nom, :mail, :password)",
    {
        'prenom': e_prenom.get(),
        'nom': e_nom.get(),
        'email': e_mail.get(),
        'password': e_password.get()
    }
    
    )
    conn.commit
    conn.close

def afficher():
    conn = sqlite3.connect('login.db')
    c=conn.cursor

    c.execute("SELECT*, iod FROM user")
records = c.fetchall()
p_records = ""
  
for record in records:
    p_records += str(record) + "\n"

query_label = Label(root, text=p_records)
query_label.grid(row=7, column=0, columnspan=2)
conn.commit
conn.close
prenom = Label(root, text="Prénom :")
nom = Label(root, text="Nom :")
eemail = Label(root, text="Email :")
password= Label(root, text="Password:")

e_prenom = Entry(root, width=35)
e_nom = Entry(root, width=35)
e_mail = Entry(root, width=35)
e_password = Entry(root, width=35)

prenom.grid(row=0, column=0, padx=15, pady=20 )
e_prenom.grid(row=0, column=1, padx=15,  pady=20 )

nom.grid(row=1, column=0, padx=15,  pady=20 )
e_nom.grid(row=1, column=1, padx=15 )

eemail.grid(row=3, column=0, padx=15,  pady=20 )
e_mail.grid(row=3, column=1, padx=15 )

password.grid(row=4, column=0, padx=15,  pady=20 )
e_password.grid(row=4, column=1, padx=15 )

save = Button(root, text="Enregistrer", width=30, command=submit)
save.grid(row=5, column=1, columnspan=2)

show_records =Button(root, text="voir les enregistrements",  width=30, command=afficher)
show_records.grid(row=6, column=1, columnspan=2, pady=15) 

conn.commit
conn.close

root.mainloop()