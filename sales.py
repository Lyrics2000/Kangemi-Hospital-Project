import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import csv
from datetime import date
from fpdf import FPDF
import datetime

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kangemi Hospital")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "Sales", font = ('Times', 50, 'bold' ), fg = 'white' , bg = "#052B7E" )
        titleLabel.pack(pady = 100)
       
        """Login LableFrame """
        self.LoginDetails = tk.LabelFrame(self, padx=150, pady=10,text="LOGIN", font = ('Times',21, 'bold') , 
         fg = 'white' ,  bg = '#052B7E')
        self.LoginDetails.pack(padx=10, pady=5)
        tk.Label(self.LoginDetails, text="Username", font = ('Times',14, 'bold') ,  fg = 'white' ,  bg = '#052B7E').grid(row=0)
        tk.Label(self.LoginDetails, text="Password",font = ('Times',14, 'bold') ,  fg = 'white' ,  bg = '#052B7E').grid(row=1)
        self.user = tk.Entry(self.LoginDetails  , font = ('Times',14, 'bold') )
        self.user.grid(row=0, column=1, sticky=tk.W)
        self.passw = tk.Entry(self.LoginDetails, font = ('Times',14, 'bold') , show = "*")
        self.passw.grid(row=1, column=1, sticky=tk.W)

        """creating a login button """ 
        frameButton = tk.Frame(self, bg = '#052B7E')

        self.loginButton = tk.Button(frameButton,text = "LOGIN" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.login)
        self.loginButton.pack(padx=10, pady=5, side = tk.LEFT)
        self.Reset = tk.Button(frameButton,text = "RESET" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.reset)
        self.Reset.pack(padx=10, pady=5 , side = tk.LEFT)
        frameButton.pack()
        """ creating patient details button for another window """
        patientsButton = tk.Frame(self, bg = '#052B7E')

        """OVER THE COUNTER """
        self.overthecounter = tk.Button(patientsButton,text = "OVER THE COUNTER" , 
        font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', state = tk.DISABLED , command = self.OverTheCounter)
        self.overthecounter.pack(padx=10, pady=5, side = tk.LEFT)

        """Patients Sales"""
        self.patientsSales = tk.Button(patientsButton,text = "Patients Sales" , font = ('Times',14, 'bold') , fg = 'white' , 
         bg = '#052B7E' , relief = 'raised',state = tk.DISABLED )
        self.patientsSales.pack(padx=10, pady=5 , side = tk.LEFT)
        patientsButton.pack()
        self.mydb = mysql.connect(
        host = 'localhost',
        user = 'root',
        password  = '',
        database =  'newhospital')
        
     
        
    def reset(self):
        self.user.delete(0 , tk.END)
        self.passw.delete(0, tk.END)
        self.user.focus_set()
    def login(self):
        if (len(self.user.get()) == 0) or(len(self.passw.get()) == 0):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        else:
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT * FROM user WHERE user_name = %s",([self.user.get()]))
           
            userr = cur.fetchall() 
            cur.close()
            
            if (userr[0][5] == self.passw.get()):
                message = "successfully logged in"
                mb.askokcancel(message= message ,  parent =  self)
                self.overthecounter.config(state = tk.NORMAL)
                self.patientsSales.config(state = tk.NORMAL)
                
                
                
            else:
                message = "Password entered is incorrect!!"
                mb.askokcancel(message= message ,  parent =  self)
                self.overthecounter.config(state = tk.DISABLED)
                self.patientsSales.config(state = tk.DISABLED)
                
   
    
    
    
    def OverTheCounter(self):
        window = OverTheCounter(self)
        window.grab_set()
"""Over The Counter """
class OverTheCounter(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("OVER THE COUNTER")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "OVER THE COUNTER", font = ('Times', 20, 'bold' ), fg = 'white' , bg = "#052B7E" )
        titleLabel.pack(pady = 20)
        frameContent = tk.Frame(self,bg = '#052B7E')
        
        
        frameContent.pack()
        """msql connection """
        self.mydb = mysql.connect(
        host = 'localhost',
        user = 'root',
        password  = '',
        database =  'newhospital')

        """Frame for labels """
        frameLabels = tk.LabelFrame(frameContent, pady=10,text="DETAILS", font = ('Times',21, 'bold') , 
         fg = 'white' ,  bg = '#052B7E' )
        frameLabels.pack(side = tk.RIGHT , padx = 0)
        """Labels for diffferent inputs """
        """Patients Name """
        self.PName = tk.Label(frameLabels, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E"  )
        self.PName.grid(row = 0 ,  column = 0 , padx = 10)
        self.PNameL = tk.Label(frameLabels, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PNameL.grid(row = 0 ,  column = 1 , padx = 10)
        
        """Drug Name """
        self.DrugName = tk.Label(frameLabels, text = "Drug Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E"  )
        self.DrugName.grid(row = 1 ,  column = 0 , padx = 10)
        self.DrugNameL = tk.Label(frameLabels, text = "Drug Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.DrugNameL.grid(row = 1 ,  column = 1 , padx = 10)

        """Quantity """
        self.qty = tk.Label(frameLabels, text = "Quantity", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E"  )
        self.qty.grid(row = 2 ,  column = 0 , padx = 10)
        self.qtyL = tk.Label(frameLabels, text = "Quantity", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.qtyL.grid(row = 2 ,  column = 1 , padx = 10)

        """Selling Price """
        self.price = tk.Label(frameLabels, text = "Selling Price", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E"  )
        self.price.grid(row = 3 ,  column = 0 , padx = 10)
        self.priceL = tk.Label(frameLabels, text = "Selling Price", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.priceL.grid(row = 3 ,  column = 1, padx = 10)

        """Payment Mode """
        self.paymentss = tk.Label(frameLabels, text = "Payment Method", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E"  )
        self.paymentss.grid(row = 4 ,  column = 0 , padx = 10)
        self.paymentssL = tk.Label(frameLabels, text = "Payment Method", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.paymentssL.grid(row = 4 ,  column = 1, padx = 10)

        """Total Price """
        self.total = tk.Label(frameLabels, text = "Total Price", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E"  )
        self.total.grid(row = 5,  column = 0 , padx = 10)
        self.totalL = tk.Label(frameLabels, text = "Total Price", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.totalL.grid(row = 5 ,  column = 1, padx = 10)
     
        """Print Details """
        framePrint = tk.Frame(frameLabels, bg  = '#052B7E' )
        framePrint.grid(row = 6 ,  sticky = 'nwse' )
        self.ButtonPrint = tk.Button(framePrint,text = "patients Report" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.print_details)
        self.ButtonPrint.grid(row=0, column=1, sticky=tk.W , padx = 10 ,  pady = 10)
        self.GeneralButtonPrint = tk.Button(framePrint,text = "General Report" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.general_report)
        self.GeneralButtonPrint.grid(row=0, column=2, sticky=tk.W , padx = 10 ,  pady = 10)


        frameInputs = tk.Frame(frameContent, bg  = '#052B7E' )
        frameInputs.pack(side = tk.LEFT)
        

        """Patients Name """
        self.PatientsName = tk.Label(frameInputs, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsName.grid(row = 0 ,  column = 0 , padx = 10)
        self.PatientsNameE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.PatientsNameE.insert(0,"Cash")
        self.PatientsNameE.grid(row = 0 ,  column = 1 , padx = 10 ,  pady = 5)
       
        """Drug combobox """
        drugs  = self.selectDrug()
        self.DrugName = tk.Label(frameInputs, text = "Drug Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.DrugName.grid(row = 1 ,  column = 0 , padx = 10)
        self.drugs = ttk.Combobox(frameInputs, values=drugs,font = ('Times', 14, 'bold' ))
        self.drugs.bind("<<ComboboxSelected>>")
        self.drugs.grid(row = 1, column = 1 , padx = 10,  pady = 5)
        
        """ Quantity """
        self.Quantity = tk.Label(frameInputs, text = "Quantity", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Quantity.grid(row = 2 ,  column = 0 , padx = 10)
        
        self.QuantityE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.QuantityE.grid(row = 2 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """Payments """
        payment  = ("CASH", "TILL", "MPESA","CHEQUE","OTHERS")
        self.payment = tk.Label(frameInputs, text = "Payment", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.payment.grid(row = 3 ,  column = 0 , padx = 10)
        self.payment = ttk.Combobox(frameInputs, values=payment,font = ('Times', 14, 'bold' ))
        self.payment.bind("<<ComboboxSelected>>", self.create_payment)
        self.payment.grid(row = 3 , column = 1 , padx = 10,  pady = 5)
        """payments Till """
        self.Till = tk.Label(frameInputs, text = "MPESA CODE", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Till.grid(row = 4 ,  column = 0 , padx = 10)
        self.Till.grid_forget()
        self.TillE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.TillE.grid(row = 4 ,  column = 1 , padx = 10 ,  pady = 5)
        self.TillE.grid_forget()

        """payments Cheque """
        self.cheque = tk.Label(frameInputs, text = "CHEQUE CODE", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.cheque.grid(row = 4 ,  column = 0 , padx = 10)
        self.cheque.grid_forget()
        self.chequeE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.chequeE.grid(row = 4 ,  column = 1 , padx = 10 ,  pady = 5)
        self.chequeE.grid_forget()

        """Other payments """
        self.others = tk.Label(frameInputs, text = "Others payments", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.others.grid(row = 4 ,  column = 0 , padx = 10)
        self.others.grid_forget()
        self.othersE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.othersE.grid(row = 4 ,  column = 1 , padx = 10 ,  pady = 5)
        self.othersE.grid_forget()


        
        

        """frame for button save and delete """
        frameButton = tk.Frame(self,bg = '#052B7E' )
        self.ButtonSave = tk.Button(frameButton,text = "SAVE" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.save)
        self.ButtonSave.grid(row=0, column=0, sticky=tk.W , padx = 10 ,  pady = 10)
        self.ButtonReset = tk.Button(frameButton,text = "RESET" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.reset)
        self.ButtonReset.grid(row=0, column=1, sticky=tk.W , padx = 10 ,  pady = 10)
        frameButton.pack()
        """SEARCH FRAME """
        frameSearch = tk.Frame(self,bg = '#052B7E' )
        frameSearch.pack()
        self.searchEntery = tk.Entry(frameSearch , font = ('Times',14, 'bold') )
        self.searchEntery.grid(row = 0  , column = 0 , padx = 10 ,  pady = 5 )
        self.SearchButton = tk.Button(frameSearch,text = "SEARCH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' , command =  self.search)
        self.SearchButton.grid(row=0, column=1, sticky=tk.W , padx = 10 ,  pady = 5)
        self.REFRESHButton = tk.Button(frameSearch,text = "REFRESH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' ,  command = self.Refresh)
        self.REFRESHButton.grid(row=0, column=2, sticky=tk.W , padx = 10 ,  pady = 5)


        """Tree """
        frameOthers = tk.Frame(self,bg = '#052B7E' )
        frameOthers.pack(side = tk.TOP )
        columns = ("#1", "#2", "#3" ,"#4", "#5") 
        self.tree = ttk.Treeview(frameOthers, show="headings", columns=columns )
        self.tree.heading("#1", text="Patients Name")
        self.tree.heading("#2", text="Drug Name")
        self.tree.heading("#3", text="Quantity")
        self.tree.heading("#4", text="Price")
        self.tree.heading("#5", text="Payments")
        ysb = ttk.Scrollbar(frameOthers, orient=tk.VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        self.trees()
        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=2, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        """total drugs """
        self.totalDrugs()
        
        
        
    
    """trees """
    def trees(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT PatientName,drugName,qty,price,cash FROM sales")
        userrr = cur.fetchall() 
        cur.close()
        

        for contact in userrr:
            self.tree.insert("", tk.END, values=contact)
            self.tree.bind("<<TreeviewSelect>>", self.print_section)
    
    def save(self):
        totalDrugs = []
        newDrugs = []


        if(self.payment.get() == "TILL"):
            if ((len(self.drugs.get()) == 0) or   (len(self.QuantityE.get()) == 0) or (len(self.payment.get()) == 0) or (len(self.TillE.get()) == 0)  ):
                message = "Please fill in the required details"
                mb.askokcancel(message = message , parent = self)
                totalDrugs.remove()
                newDrugs.remove()
            else:
                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT Quantity FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytill = cur.fetchall() 
                cur.close()
                for qt in qtytill:
                    totalDrugs.append(qt[0])
                
                alldrugsTill = sum(totalDrugs)

                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT qty FROM sales WHERE  drugName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytilld = cur.fetchall() 
                cur.close()
                for qtl in qtytilld:
                    newDrugs.append(qtl[0])
                
                allnewdrugsTill = sum(newDrugs)
                subtractdrugs = alldrugsTill - allnewdrugsTill
                print(newDrugs)
                print(totalDrugs)

                if subtractdrugs < 0:
                    message = "Drugs remaining are {}!".format(subtractdrugs)
                    mb.askokcancel(message = message , parent = self)
                else:
                    cur = self.mydb.cursor()
                    resultValue = cur.execute("SELECT SellingPrice FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                    sellingpr = cur.fetchone() 
                    cur.close()

                    cur = self.mydb.cursor()
                    cur.execute(" INSERT INTO sales(drugName,qty,price,cash,PatientName,mpesacode)"\
                    "VALUES (%s,%s,%s,%s,%s,%s)", (self.drugs.get(),self.QuantityE.get(),float(sellingpr[0]), self.payment.get(),self.PatientsNameE.get(),self.TillE.get() ))
                    self.mydb.commit()
                    cur.close()
                    self.tree.delete(*self.tree.get_children())
                    self.trees()
                    message = "Details Entered successfully!"
                    mb.askokcancel(message = message , parent = self)
                    self.reset()
                    self.Till.grid_forget()
                    self.TillE.grid_forget()



            
                
        elif(self.payment.get() == "CHEQUE"):
            if ((len(self.drugs.get()) == 0) or   (len(self.QuantityE.get()) == 0) or (len(self.payment.get()) == 0) or (len(self.chequeE.get()) == 0)  ):
                message = "Please fill in the required details"
                mb.askokcancel(message = message , parent = self)
            else:
                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT Quantity FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytill = cur.fetchall() 
                cur.close()
                for qt in qtytill:
                    totalDrugs.append(qt[0])
                
                alldrugsTill = sum(totalDrugs)

                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT qty FROM sales WHERE  drugName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytilld = cur.fetchall() 
                cur.close()
                for qtl in qtytilld:
                    newDrugs.append(qtl[0])
                
                allnewdrugsTill = sum(newDrugs)
                subtractdrugs = alldrugsTill - allnewdrugsTill
                print(newDrugs)
                print(totalDrugs)

                if subtractdrugs < 0:
                    message = "Drugs remaining are {}!".format(subtractdrugs)
                    mb.askokcancel(message = message , parent = self)
                else:
                    cur = self.mydb.cursor()
                    resultValue = cur.execute("SELECT SellingPrice FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                    sellingpr = cur.fetchone() 
                    cur.close()
                
                    cur = self.mydb.cursor()
                    cur.execute(" INSERT INTO sales(drugName,qty,price,cash,PatientName,chequecode)"\
                    "VALUES (%s,%s,%s,%s,%s,%s)", (self.drugs.get(),self.QuantityE.get(),float(sellingpr[0]), self.payment.get(),self.PatientsNameE.get(),self.chequeE.get() ))
                    self.mydb.commit()
                    cur.close()
                    self.tree.delete(*self.tree.get_children())
                    self.trees()
                    message = "Details Entered successfully!"
                    mb.askokcancel(message = message , parent = self)
                    self.reset()
                    self.cheque.grid_forget()
                    self.chequeE.grid_forget()
        elif(self.payment.get() == "OTHERS"):
            if ((len(self.drugs.get()) == 0) or   (len(self.QuantityE.get()) == 0) or (len(self.payment.get()) == 0) or (len(self.othersE.get()) == 0)  ):
                message = "Please fill in the required details"
                mb.askokcancel(message = message , parent = self)
            else:
                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT Quantity FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytill = cur.fetchall() 
                cur.close()
                for qt in qtytill:
                    totalDrugs.append(qt[0])
                
                alldrugsTill = sum(totalDrugs)

                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT qty FROM sales WHERE  drugName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytilld = cur.fetchall() 
                cur.close()
                for qtl in qtytilld:
                    newDrugs.append(qtl[0])
                
                allnewdrugsTill = sum(newDrugs)
                subtractdrugs = alldrugsTill - allnewdrugsTill
                print(newDrugs)
                print(totalDrugs)

                if subtractdrugs < 0:
                    message = "Drugs remaining are {}!".format(subtractdrugs)
                    mb.askokcancel(message = message , parent = self)
                else:
                    cur = self.mydb.cursor()
                    resultValue = cur.execute("SELECT SellingPrice FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                    sellingpr = cur.fetchone() 
                    cur.close()
                
                    cur = self.mydb.cursor()
                    cur.execute(" INSERT INTO sales(drugName,qty,price,cash,PatientName,otherscode)"\
                    "VALUES (%s,%s,%s,%s,%s,%s)", (self.drugs.get(),self.QuantityE.get(),float(sellingpr[0]), self.payment.get(),self.PatientsNameE.get(),self.othersE.get() ))
                    self.mydb.commit()
                    cur.close()
                    self.tree.delete(*self.tree.get_children())
                    self.trees()
                    message = "Details Entered successfully!"
                    mb.askokcancel(message = message , parent = self)
                    self.reset()
                    self.others.grid_forget()
                    self.othersE.grid_forget()
        else:
            if ((len(self.drugs.get()) == 0) or   (len(self.QuantityE.get()) == 0) or (len(self.payment.get()) == 0) ):
                message = "Please fill in the required details"
                mb.askokcancel(message = message , parent = self)
            else:
                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT Quantity FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytill = cur.fetchall() 
                cur.close()
                for qt in qtytill:
                    totalDrugs.append(qt[0])
                
                alldrugsTill = sum(totalDrugs)

                cur = self.mydb.cursor()
                resultValue = cur.execute("SELECT qty FROM sales WHERE  drugName LIKE BINARY '{}' ".format(self.drugs.get()))
                qtytilld = cur.fetchall() 
                cur.close()
                for qtl in qtytilld:
                    newDrugs.append(qtl[0])
                
                allnewdrugsTill = sum(newDrugs)
                subtractdrugs = alldrugsTill - allnewdrugsTill
                print(newDrugs)
                print(totalDrugs)

                if subtractdrugs < 0:
                    message = "Drugs remaining are {}!".format(subtractdrugs)
                    mb.askokcancel(message = message , parent = self)
                else:
                    cur = self.mydb.cursor()
                    resultValue = cur.execute("SELECT SellingPrice FROM product WHERE  productName LIKE BINARY '{}' ".format(self.drugs.get()))
                    sellingpr = cur.fetchone() 
                    cur.close()
                
                    cur = self.mydb.cursor()
                    cur.execute(" INSERT INTO sales(drugName,qty,price,cash,PatientName)"\
                    "VALUES (%s,%s,%s,%s,%s)", (self.drugs.get(),self.QuantityE.get(),float(sellingpr[0]), self.payment.get(),self.PatientsNameE.get() ))
                    self.mydb.commit()
                    cur.close()
                    self.tree.delete(*self.tree.get_children())
                    self.trees()
                    message = "Details Entered successfully!"
                    mb.askokcancel(message = message , parent = self)
                    self.reset()
    
    def reset(self):
        self.drugs.delete(0, tk.END)
        self.QuantityE.delete(0, tk.END)
        self.payment.delete(0,tk.END)
        self.drugs.focus_set()
    
    def search(self):
        if (len(self.searchEntery.get()) == 0):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        elif((len(self.searchEntery.get()) != 0)):
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT PatientName,drugName,qty,price,cash FROM sales WHERE  drugName LIKE '%{}%' ".format(self.searchEntery.get()))
            userrr = cur.fetchall() 
            cur.close()
            self.tree.delete(*self.tree.get_children())

            for contact in userrr:
                self.tree.insert("", tk.END, values=contact)
                self.tree.bind("<<TreeviewSelect>>")
        else:
            message = "Record Not Found!!"
            mb.askokcancel(message = message , parent = self)
            self.trees()
    

    def Refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.trees()
    """Selecting Drugs """
    def selectDrug(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT productName FROM product")
        userrr = cur.fetchall() 
        cur.close()

        return userrr[:]

    
    def print_details(self):
        pdf = FPDF()
        pdf.add_page()
       
        pdf.set_font("Times"  ,size= 15)
        pdf.cell(200, 10 , txt = "CARELINK MEDICAL CENTRE" , ln = 1 , align = 'C')
        pdf.cell(200, 10 , txt = "AT Mzee Juma's Flats " , ln = 2 , align = 'C')
        pdf.cell(200, 10 , txt = "Near Kangemi Memorial Park -  WARUKU" , ln = 3 , align = 'C')
        pdf.cell(200, 10 , txt = "P.O Box 14496-00800" , ln = 4 , align = 'C')
        pdf.cell(200, 10 , txt = "Nairobi" , ln = 5 , align = 'C')
        pdf.cell(200, 10 , txt = "Tell : 0727546794" , ln = 6 , align = 'C')

        pdf.set_font("Times"  ,'B' ,size= 15)
        pdf.cell(200, 10 , txt = "{}".format(self.paymentssL.cget("text")) , ln = 7 , align = 'C')

        pdf.set_font("Times" , 'B' ,size= 15)
        pdf.cell(200, 10 , txt = " Date : {} ".format(datetime.date.today()) , ln = 9 , align = 'L')
        
        
        pdf.set_font("Times" , 'B' ,size= 15)
        pdf.cell(40,10,'Patients Name ' ,2 , 0)
        pdf.cell(40,10,'Drug Name ' ,2 , 0)
        pdf.cell(40,10,'Quantity ' , 2, 0)
        pdf.cell(40,10,'Price ' ,2, 0)
        pdf.cell(40,10,'Total' ,2 , 0)

        pdf.set_font("Times"  ,size= 8)
        pdf.cell(40,10,'' ,2 , 1)
        pdf.cell(40,10,'{}'.format(self.PNameL.cget("text")) , 2, 0)
        pdf.cell(40,10,'{}'.format(self.DrugNameL.cget("text")) , 2, 0)
        pdf.cell(40,10,'{}'.format(self.qtyL.cget("text")) ,2, 0)
        pdf.cell(40,10,'Ksh : {}'.format(self.priceL.cget("text")) ,2 , 0)
        pdf.cell(40,10,'Ksh : {}'.format(self.totalL.cget("text")) ,2 , 0)

        pdf.set_font("Times"  ,'B' ,size= 12)
        pdf.cell(40,10, '' , 2 , 1 , 'R')
        
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, 'SIGN' , 2 , 0) 
        pdf.cell(40,10, '.............................' , 2 , 0)

        pdf.set_font("Times"  ,'B' ,size= 12)
        pdf.cell(40,10, '' , 2 , 1 , 'R')
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, 'STAMP' , 2 , 0) 
        pdf.cell(40,10, '.............................' , 2 , 0)

        pdf.cell(40,10,'' ,2 , 1)
        pdf.cell(200, 10 , txt = "...THANK YOU..."  , align = 'C')
        pdf.cell(40,10,'' ,2 , 1)
        pdf.cell(200, 10 , txt = "...GET WELL SOON..."  , align = 'C')



        """
        pdf.cell(200, 10 , txt = "Drug Name  : {}".format(self.DrugNameL.cget("text")) , ln = 1 , align = 'L')
        pdf.cell(200, 10 , txt = "Quantity  : {}".format(self.qtyL.cget("text")) , ln = 2 , align = 'L')
        pdf.cell(200, 10 , txt = "Price  :Ksh {}".format(self.priceL.cget("text")) , ln = 3 , align = 'L')
        pdf.cell(200, 10 , txt = "Total Price  :Ksh {}".format(self.totalL.cget("text")) , ln = 4 , align = 'L')
        pdf.cell(200, 10 , txt = "Payment Method : {}".format(self.paymentssL.cget("text")) , ln = 5 , align = 'L')
        pdf.cell(200, 10 , txt = "...THANK YOU..." , ln = 5 , align = 'C')
        pdf.cell(200, 10 , txt = "...GET WELL SOON..." , ln = 6 , align = 'C')
        """
        try:
            pdf.output("patient.pdf")
            message = "PDF Generated successfully!"
            mb.askokcancel(message = message , parent = self)
        except:
            message = "Close the open pdf!"
            mb.askokcancel(message = message , parent = self)


        
    def print_section(self, event):
        drugstock = []
        for selection in self.tree.selection():
            item = self.tree.item(selection)
            drugName = item["values"][1]
            quanty = item["values"][2]
            pr = item["values"][3]
            pay = item["values"][4]
            pN = item["values"][0]
            totalP = float(pr) * int(quanty)
            self.DrugNameL.config(text = drugName)
            self.qtyL.config(text = quanty)
            #paymentssL
            self.priceL.config(text = pr)
            self.totalL.config(text = totalP)
            self.paymentssL.config(text = pay)
            self.PNameL.config(text = pN)
            #PNameL
            #Patients Name
            print(str(drugName))
            cur = self.mydb.cursor()
            
            resultValue = cur.execute("SELECT Quantity FROM product WHERE  productName LIKE '%{}%' ".format(drugName))
            
            userrr = cur.fetchall()
             
            cur.close()
            
            for qt in userrr:
                print(str(qt[:]))
                drugstock.append(qt[0])
                print(drugstock)
    def create_payment(self,*args):
        if(self.payment.get() == "TILL"):
            self.Till.grid(row = 4 ,  column = 0 , padx = 10)
            self.TillE.grid(row = 4 ,  column = 1 , padx = 10 ,  pady = 5)
        elif(self.payment.get() == "CHEQUE"):
            self.Till.grid_forget()
            self.TillE.grid_forget()
            self.cheque.grid(row = 4 ,  column = 0 , padx = 10)
            self.chequeE.grid(row = 4 ,  column = 1 , padx = 10 ,  pady = 5)
        elif(self.payment.get() == "OTHERS"):
            self.Till.grid_forget()
            self.TillE.grid_forget()
            self.cheque.grid_forget()
            self.chequeE.grid_forget()
            self.others.grid(row = 4 ,  column = 0 , padx = 10)
            self.othersE.grid(row = 4 ,  column = 1 , padx = 10 ,  pady = 5)
        else:
            self.Till.grid_forget()
            self.TillE.grid_forget()
            self.cheque.grid_forget()
            self.chequeE.grid_forget()
            self.others.grid_forget()
            self.othersE.grid_forget()




        
    
    def general_report(self):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Times"  ,size= 15)
        pdf.cell(200, 10 , txt = "CARELINK MEDIACAL CENTRE" , ln = 1 , align = 'C')
        pdf.cell(200, 10 , txt = "AT Mzee Juma's Flats " , ln = 2 , align = 'C')
        pdf.cell(200, 10 , txt = "Near Kangemi Memorial Park -  WARUKU" , ln = 3 , align = 'C')
        pdf.cell(200, 10 , txt = "P.O Box 14496-00800" , ln = 4 , align = 'C')
        pdf.cell(200, 10 , txt = "Nairobi" , ln = 5 , align = 'C')
        pdf.cell(200, 10 , txt = "Tell : 0727546794" , ln = 6 , align = 'C')

        pdf.set_font("Times"  ,'B' ,size= 12)
        pdf.cell(200, 10 , txt = "Date  :{}".format(datetime.date.today()) , ln = 7 , align = 'L')
        pdf.set_font("Times" , 'B' ,size= 12)
        pdf.cell(40,10,'Patients Name ' ,1 , 0 , 'C')
        pdf.cell(40,10,'Drug Name ' ,1 , 0 , 'C')
        pdf.cell(40,10,'Quantity ' , 1, 0 , 'C')
        pdf.cell(40,10,'Price ' ,1, 0 , 'C')
        pdf.cell(40,10,'Total' ,1 , 0 , 'C')
        pdf.cell(40,10,'Payment Method' ,1 , 0 , 'C')

        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT PatientName,drugName,qty,price,cash FROM sales ")
        userrr = cur.fetchall() 
        cur.close()
        pdf.set_font("Times"  ,size= 8)
        """Creating drugs array """
        dru = []
        totalcash = []

        for user in userrr:
            pdf.cell(40,10,'' ,1 , 1)
            pdf.cell(40,10,'{}'.format(user[0]) , 1, 0 , 'C')
            pdf.cell(40,10,'{}'.format(user[1]) , 1, 0 , 'C')
            pdf.cell(40,10,'{}'.format(user[2]) ,1, 0 , 'C')
            pdf.cell(40,10,'Ksh : {}'.format(user[3]) ,1 , 0 , 'C')
            pdf.cell(40,10,'Ksh : {}'.format(user[3] * user[2]) ,1 , 0, 'C')
            pdf.cell(40,10,'{}'.format(user[4]) ,1, 0)
            dru.append(user[1])
            totalcash.append(user[3] * user[2])
        
        pdf.set_font("Times"  ,'B' ,size= 12)
        pdf.cell(40,10, '' , 2 , 1 , 'R')
        
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, 'Total Drugs' , 2 , 0) 
        pdf.cell(40,10, '{}'.format(len(dru)) , 2 , 0) 

        pdf.set_font("Times"  ,'B' ,size= 12)
        pdf.cell(40,10, '' , 2 , 1 , 'R')
        
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, 'Total ' , 2 , 0) 
        pdf.cell(40,10, '{}'.format(sum(totalcash)) , 2 , 0)     

        pdf.set_font("Times"  ,'B' ,size= 12)
        pdf.cell(40,10, '' , 2 , 1 , 'R')
        
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, 'SIGN' , 2 , 0) 
        pdf.cell(40,10, '.............................' , 2 , 0)

        pdf.set_font("Times"  ,'B' ,size= 12)
        pdf.cell(40,10, '' , 2 , 1 , 'R')
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, '' , 2 , 0) 
        pdf.cell(40,10, 'STAMP' , 2 , 0) 
        pdf.cell(40,10, '.............................' , 2 , 0)

        try:
            pdf.output("generalReport.pdf")
            message = "PDF Generated successfully!"
            mb.askokcancel(message = message , parent = self)
        except:
            message = "Close the open pdf!"
            mb.askokcancel(message = message , parent = self)
    
    




        
            

        

                
   






        


if __name__ == "__main__":
     app = App()
     app.mainloop()