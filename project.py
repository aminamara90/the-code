import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#creation de base de donne de A
conn=sqlite3.connect('databaseA.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS adressA(
     A1 integer,
     A2 integer
     )""")
conn.commit()
conn.close()

#creation de base de donne de B
conn=sqlite3.connect('databaseB.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS adressB(
     B1 integer,
     B2 integer
     )""")
conn.commit()
conn.close()

#creation de base de donne de C
conn=sqlite3.connect('databaseC.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS adressC(
     C1 integer,
     C2 integer
     )""") 
conn.commit()
conn.close()

#creation de base de donne de D
conn=sqlite3.connect('databaseD.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS adressD(
     D1 integer,
     D2 integer
     )""")
conn.commit()
conn.close()

#fermer fenetre succeee et ouvrir fenetre de paiement
def destroy():
     login_success_screen.destroy()
     window2.destroy()
     functionpaiement()

#fenetre de succee
def login_sucess():
    global login_success_screen
    login_success_screen = Tk()
    login_success_screen.title("Success")
    login_success_screen.config(bg='#141414')
    login_success_screen.geometry("300x100")
    Label(login_success_screen, text="Connexion Reussie",fg='#63A375',bg='#141414',font=('Tw Cen MT',20)).pack()
    bttn(login_success_screen,100,50,"Ok",'#0077b6','#141414',destroy,('Tw Cen MT',15))

#fenetre de verification de mdp
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Tk()
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("200x100")
    Label(password_not_recog_screen, text="Mot De Passe Ou Nom Incorrect!!",fg='#63A375',bg='#141414',font=('Tw Cen MT',20)).pack()
    bttn(password_not_recog_screen,100,50,"Ok",'#0077b6','#141414',password_not_recog_screen.destroy,('Tw Cen MT',15))

#fenetre de verification de remplir toutes les informations
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Tk()
    user_not_found_screen.title("Error")
    user_not_found_screen.config(bg='#141414')
    user_not_found_screen.geometry("500x100")
    Label(user_not_found_screen, text="Remplit Toutes Les Donnees SVP",font=('Tw Cen MT',20),fg='Red',bg='#141414').pack()
    bttn(user_not_found_screen,200,50,"Ok",'#4169E1','#141414',user_not_found_screen.destroy,('Tw Cen MT',15))

#creer un animation pour toutes les button
def bttn(w,x,y,text,bcolor,fcolor,cmd,fnt):
     def enter(e):
          mbttn['bg']=bcolor
          mbttn['fg']=fcolor
     def leave(e):
          mbttn['bg']=fcolor
          mbttn['fg']=bcolor
     mbttn=Button(w,text=text,fg=fcolor,bg=bcolor,border=0,activeforeground=fcolor,activebackground=bcolor,command=cmd,font=(fnt))
     mbttn.bind("<Enter>",enter)
     mbttn.bind("<Leave>",leave)
     mbttn.place(x=x,y=y)

#fenetre de payer
def functionpayer():
#fenetre A
     def A():
          
          windowA=Tk()
          windowA.title('La Gestion Des Ressources Syndicales Dans Un Immeuble')
          windowA.geometry('700x500')
          windowA.config(bg='#141414')
          windowA.iconbitmap(r'icon.ico')
          Label(windowA,text='Choisir Un Appartement et payer 50dt',font=('Tw Cen MT',20),fg='white',bg='#141414').pack(pady=30)


          Label(windowA,text="Nom D'apartement:",font=('Tw Cen MT',15),fg='white',bg='#141414').place(x=20,y=100)


          A1=StringVar()
          A2=StringVar()

          A1_entry=ttk.Combobox(windowA,values=["A1","A2","A3","A4","A5"],textvariable=A1)
          A1_entry.place(x=250,y=110)
     
          Label(windowA,text='Le Montant:',font=('Tw Cen MT',15),fg='white',bg='#141414').place(x=40,y=135)
          A2_entry=Entry(windowA,textvariable=A2)
          A2_entry.place(x=250,y=140)
#insertion de les informations dans A
          def saveA():
            conn=sqlite3.connect('databaseA.db')
            c=conn.cursor() 
            c.execute("SELECT A1 FROM adressA")
            n=c.fetchall()
            if A1_entry.get()=='' or A2_entry.get()=='' :
                    messagebox.showinfo('Info','Remplir Toutes Les Donnees SVP')    
            else:
               if A1_entry.get()!='A3': 
                   c.execute("INSERT INTO adressA VALUES(:A1, :A2)",
                         {
                                 'A1': A1_entry.get(),
                                 'A2': A2_entry.get()
                         })
                   conn.commit()
                   conn.close()
                   A1_entry.delete(0,END)
                   A2_entry.delete(0,END)
                   messagebox.showinfo('DONE','Paiement Reussi')
                   windowA.destroy()
               if A1_entry.get()=='A3':
                      messagebox.showerror('Error','Deja Payee') 
                              
          bttn(windowA,60,200,"Payer",'#00FF33','#141414',saveA,('Tw Cen MT',20))
          bttn(windowA,200,200,"Quitter",'#FF5C5C','#141414',windowA.destroy,('Tw Cen MT',20))
          window1.destroy()  
#fenetre B             
     def B():
       windowB=Tk()
       windowB.title('La Gestion Des Ressources Syndicales Dans Un Immeuble')
       windowB.geometry('700x500')
       windowB.config(bg='#141414') 
       windowB.iconbitmap(r'icon.ico')

       choose=Label(windowB,text='Choisir Un Appartement et payer 50dt',font=('Arial',20),fg='white',bg='#141414').pack(pady=30)

       B1=StringVar()
       B2=StringVar()

       B1_entry=ttk.Combobox(windowB,values=["B1","B2","B3","B4","B5"],textvariable=B1)
       B1_entry.place(x=250,y=110)
     
       Label(windowB,text='Le Montant:',font=('Tw Cen MT',15),fg='white',bg='#141414').place(x=40,y=135)
       B2_entry=Entry(windowB,textvariable=B2)
       B2_entry.place(x=250,y=140)
#insertion de les informations dans B
       def saveB():
            conn=sqlite3.connect('databaseB.db')
            c=conn.cursor() 
            c.execute("SELECT B1 FROM adressB")
            if B1_entry.get()=='' or B2_entry.get()=='' :
                    messagebox.showinfo('Info','Remplir Toutes Les Donnees SVP')    
            else:
                
               if B1_entry.get()!='B2' or B1_entry.get()!='B5': 
                   c.execute("INSERT INTO adressB VALUES(:B1, :B2)",
                         {
                                 'B1': B1_entry.get(),
                                 'B2': B2_entry.get()
                         })
                   conn.commit()
                   conn.close()
                   B1_entry.delete(0,END)
                   B2_entry.delete(0,END)
                   messagebox.showinfo('DONE','Paiement Reussi')
                   windowB.destroy()
               if B1_entry.get()=='B2' or B1_entry.get()=='B5':
                     messagebox.showerror('Error','Deja Payee') 
       bttn(windowB,60,200,"Payer",'#00FF33','#141414',saveB,('Tw Cen MT',20))
       bttn(windowB,200,200,"Quitter",'#FF5C5C','#141414',windowB.destroy,('Tw Cen MT',20))
       window1.destroy()
#fenetre C       
     def C():
       windowC=Tk()
       windowC.title('La Gestion Des Ressources Syndicales Dans Un Immeuble')
       windowC.geometry('700x500')
       windowC.config(bg='#141414')
       windowC.iconbitmap(r'icon.ico')
       choose=Label(windowC,text='Choisir Un Appartement et payer 50dt',font=('Tw Cen MT',20),fg='white',bg='#141414').pack(pady=30)

       C1=StringVar()
       C2=StringVar()

       C1_entry=ttk.Combobox(windowC,values=["C1","C2","C3","C4","C5"],textvariable=C1)
       C1_entry.place(x=250,y=110)
     
       Label(windowC,text='Le Montant:',font=('Tw Cen MT',15),fg='white',bg='#141414').place(x=40,y=135)
       C2_entry=Entry(windowC,textvariable=C2)
       C2_entry.place(x=250,y=140)
#insertion de les informations dans C
       def saveC():
            conn=sqlite3.connect('databaseC.db')
            c=conn.cursor() 
            c.execute("SELECT C1 FROM adressC")
            if C1_entry.get()=='' or C2_entry.get()=='' :
                    messagebox.showinfo('Info','Remplir Toutes Les Donnees SVP')    
            else:
                
               if C1_entry.get()!='C1': 
                   c.execute("INSERT INTO adressC VALUES(:C1, :C2)",
                         {
                                 'C1': C1_entry.get(),
                                 'C2': C2_entry.get()
                         })
                   conn.commit()
                   conn.close()
                   C1_entry.delete(0,END)
                   C2_entry.delete(0,END)
                   messagebox.showinfo('DONE','Paiement Reussi')
                   windowC.destroy()
               if C1_entry.get()=='C1':
                      messagebox.showerror('Error','Deja Payee')
       bttn(windowC,60,200,"Payer",'#00FF33','#141414',saveC,('Tw Cen MT',20))
       bttn(windowC,200,200,"Quitter",'#FF5C5C','#141414',windowC.destroy,('Tw Cen MT',20))
       window1.destroy()
  #fenetre D     
     def D():
       windowD=Tk()
       windowD.title('La Gestion Des Ressources Syndicales Dans Un Immeuble')
       windowD.geometry('700x500')
       windowD.config(bg='#141414')
       windowD.iconbitmap(r'icon.ico')
       choose=Label(windowD,text='Choisir Un Appartement et payer 50dt',font=('Tw Cen MT',20),fg='white',bg='#141414').pack(pady=30)

       D1=StringVar()
       D2=StringVar()

       D1_entry=ttk.Combobox(windowD,values=["D1","D2","D3","D4","D5"],textvariable=D1)
       D1_entry.place(x=250,y=110)
     
       Label(windowD,text='Le Montant:',font=('Tw Cen MT',15),fg='white',bg='#141414').place(x=40,y=135)
       D2_entry=Entry(windowD,textvariable=D2)
       D2_entry.place(x=250,y=140)
#insertion de les informations dans D
       def saveD():
            conn=sqlite3.connect('databaseD.db')
            c=conn.cursor() 
            c.execute("SELECT D1 FROM adressD")
            if D1_entry.get()=='' or D2_entry.get()=='' :
                    messagebox.showinfo('Info','Remplir Toutes Les Donnees SVP')    
            else:
                
               if D1_entry.get()!='D4': 
                   c.execute("INSERT INTO adressD VALUES(:D1, :D2)",
                         {
                                 'D1': D1_entry.get(),
                                 'D2': D2_entry.get()
                         })
                   conn.commit()
                   conn.close()
                   D1_entry.delete(0,END)
                   D2_entry.delete(0,END)
                   messagebox.showinfo('DONE','Paiement Reussi')
                   windowD.destroy()
               if D1_entry.get()=='D4':
                      messagebox.showerror('Error','Deja Payee')

       bttn(windowD,60,200,"Payer",'#00FF33','#141414',saveD,('Tw Cen MT',20))
       bttn(windowD,200,200,"Quitter",'#FF5C5C','#141414',windowD.destroy,('Tw Cen MT',20))
       window1.destroy()

 #window1  
     window1=Tk()
     window1.title('La Gestion Des Ressources Syndicales Dans Un Immeuble')
     window1.geometry('700x500')
     window1.config(bg='#141414')
     window1.iconbitmap(r'icon.ico')

     choose=Label(window1,text='Choisir Un Etage:',font=('Tw Cen MT',20),fg='white',bg='#141414')

     bttn(window1,300,70,"A",'#4169E1','#141414',A,('Tw Cen MT',20))
     bttn(window1,300,140,"B",'#4169E1','#141414',B,('Tw Cen MT',20))
     bttn(window1,300,210,"C",'#4169E1','#141414',C,('Tw Cen MT',20))
     bttn(window1,300,280,"D",'#4169E1','#141414',D,('Tw Cen MT',20))
     bttn(window1,270,350,"Quitter",'#FF5C5C','#141414',window1.destroy,('Tw Cen MT',20))
     choose.place(x=230,y=20)
#fenetre de paiement
def functionpaiement():
     window1=Tk()
     window1.title('La Gestion Des Ressources Syndicales Dans Un Immeuble')
     window1.geometry('1100x600')
     window1.config(bg='#141414')
     window1.iconbitmap(r'icon.ico')


     choose=Label(window1,text='Choisir Un Etage:',font=('Tw Cen MT',20),fg='white',bg='#141414').pack()
     def queryA():
       conn=sqlite3.connect('databaseA.db')
       c=conn.cursor()
       c.execute("SELECT * FROM adressA")
       records=c.fetchall()
       print_record=" "
       for x in records:
        print_record=print_record+'Appartement:'+str(x[0])+'\n'+' Paiement: '+str(x[1])+" \n " + '---------------------- \n'
       label=Label(window1,text=print_record,font=('courier',9),fg='white',bg='#141414')
       label.place(x=50,y=70)
       conn.commit()
       conn.close()

     def queryB():
       conn=sqlite3.connect('databaseB.db')
       c=conn.cursor()
       c.execute("SELECT * FROM adressB")
       records=c.fetchall()
       print(records)
       print_record=''
       for x in records:
        print_record=print_record+'Appartement:'+str(x[0])+'\n'+' Paiement: '+str(x[1])+" \n " + '---------------------- \n'
       label=Label(window1,text=print_record,font=('courier',9),fg='white',bg='#141414')
       label.place(x=200,y=70)
       conn.commit()
       conn.close()

     def queryC():
       conn=sqlite3.connect('databaseC.db')
       c=conn.cursor()
       c.execute("SELECT * FROM adressC")
       records=c.fetchall()
       print(records)
       print_record=''
       for x in records:
        print_record=print_record+'Appartement:'+str(x[0])+'\n'+' Paiement: '+str(x[1])+" \n " + '---------------------- \n'
       label=Label(window1,text=print_record,font=('courier',9),fg='white',bg='#141414')
       label.place(x=350,y=70)
       conn.commit()
       conn.close()

     def queryD():
       conn=sqlite3.connect('databaseD.db')
       c=conn.cursor()
       c.execute("SELECT * FROM adressD")
       records=c.fetchall()
       print(records)
       print_record=''
       for x in records:
        print_record=print_record+'Appartement:'+str(x[0])+'\n'+' Paiement: '+str(x[1])+" \n " + '---------------------- \n'
       label=Label(window1,text=print_record,font=('courier',9),fg='white',bg='#141414')
       label.place(x=500,y=70)
       conn.commit()
       conn.close()

     bttn(window1,10,70,"A",'#4169E1','#141414',queryA,('Tw Cen MT',20))
     bttn(window1,10,140,"B",'#4169E1','#141414',queryB,('Tw Cen MT',20))
     bttn(window1,10,210,"C",'#4169E1','#141414',queryC,('Tw Cen MT',20))
     bttn(window1,10,280,"D",'#4169E1','#141414',queryD,('Tw Cen MT',20))
     bttn(window1,1000,500,"Quitter",'#FF5C5C','#141414',window1.destroy,('Tw Cen MT',20))
#fenetre de session president
def functionpresident():
     global window2
     window2=Tk()
     window2.title("Session president")
     window2.geometry('700x500')
     window2.config(bg='#141414')
     window2.iconbitmap(r'icon.ico')
     Label(window2,text="Login",font=('sophia morgant',60),fg='#FFCB5A',bg='#141414').place(x=200)
     Label(window2,text="Nom D'ustilsateur:",font=('Tw Cen MT',15),fg='white',bg='#141414').place(x=20,y=200)
     Label(window2,text="Mot De Passe:",font=('Tw Cen MT',15),fg='white',bg='#141414').place(x=20,y=250)
     e2=StringVar()
     e1=StringVar()
     e1_entry=Entry(window2,textvariable=e1)
     e1_entry.place(x=190,y=200)
     e2_entry=Entry(window2,textvariable=e2,show="*")
     e2_entry.place(x=190,y=250)
     def login():
        uname=e1_entry.get()
        pwd=e2_entry.get()
        if uname!='Amin' or pwd!='0000':
             user_not_found()
        else:
             if uname=='Amin' and pwd=='0000':
                   login_sucess()
             else:
                  password_not_recognised()          


     bttn(window2,300,400,"Quitter",'#FF5C5C','#141414',window2.destroy,('Tw Cen MT',20))
     bttn(window2,100,400,"connexion",'#4169E1','#141414',login,('Tw Cen MT',20))
#fenetre principale
mainwindow=Tk()
mainwindow.title("La Gestion Des Ressources Syndicales Dans Un Immeuble")
mainwindow.geometry('700x500')
mainwindow.config(bg='#141414')
mainwindow.iconbitmap(r'icon.ico')
Welcome=Label(mainwindow,text=("Bienvenue"),font=('sophia morgant',60),fg='#00FF33',bg='#141414').place(x=160,y=10)
bttn(mainwindow,300,300,"Quitter",'#FF5C5C','#141414',mainwindow.destroy,('Tw Cen MT',20))
bttn(mainwindow,100,200,"Session Client",'#4169E1','#141414',functionpayer,('Tw Cen MT',20))
bttn(mainwindow,400,200,"Session President",'#4169E1','#141414',functionpresident,('Tw Cen MT',20))

mainwindow.mainloop()