import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import csv
from datetime import datetime
import random
import datetime as dt

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kangemi Hospital")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "PHARMACY", font = ('Times', 50, 'bold' ), fg = 'white' , bg = "#052B7E" )
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

        """PRODUCTS """
        self.products = tk.Button(patientsButton,text = "PRODUCTS" , 
        font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', state = tk.DISABLED , command = self.Products)
        self.products.pack(padx=10, pady=5, side = tk.LEFT)

        """SUPPLIERS """
        self.suppliers = tk.Button(patientsButton,text = "SUPPLIERS" , font = ('Times',14, 'bold') , fg = 'white' , 
         bg = '#052B7E' , relief = 'raised',state = tk.DISABLED ,command = self.Suppliers)
        self.suppliers.pack(padx=10, pady=5 , side = tk.LEFT)

        """INVETORY"""
        self.inventory = tk.Button(patientsButton,text = "INVENTORY" , font = ('Times',14, 'bold') , fg = 'white' , 
         bg = '#052B7E' , relief = 'raised',state = tk.DISABLED )
        self.inventory.pack(padx=10, pady=5 , side = tk.LEFT)
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
                self.products.config(state = tk.NORMAL)
                self.suppliers.config(state = tk.NORMAL)
                self.inventory.config(state = tk.NORMAL)
                
                
            else:
                message = "Password entered is incorrect!!"
                mb.askokcancel(message= message ,  parent =  self)
                self.products.config(state = tk.DISABLED)
                self.suppliers.config(state = tk.DISABLED)
                self.inventory.config(state = tk.DISABLED)
    def patientsRegestration(self):
        window  = PatientsDetails(self)
        window.grab_set()
    
    def Suppliers(self):
        window = Suppliers(self)
        window.grab_set()
    
    def Products(self):
        window = Product(self)
        window.grab_set()

class Suppliers(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Supplier")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "SUPPLIERS", font = ('Times', 20, 'bold' ), fg = 'white' , bg = "#052B7E" )
        titleLabel.pack(pady = 20)
        frameContent = tk.Frame(self,bg = '#052B7E')
        
        frameContent.pack()
        """msql connection """
        self.mydb = mysql.connect(
        host = 'localhost',
        user = 'root',
        password  = '',
        database =  'newhospital')
        frameInputs = tk.Frame(frameContent, bg  = '#052B7E' )
        frameInputs.pack(side = tk.LEFT)
        
        """Company Name"""
        self.companyName = tk.Label(frameInputs, text = "Company Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.companyName.grid(row = 0 ,  column = 0 , padx = 10)
        self.companyNameE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.companyNameE.grid(row = 0 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """ Email """
        self.Email = tk.Label(frameInputs, text = "Email", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Email.grid(row = 1 ,  column = 0 , padx = 10)
        self.EmailE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.EmailE.grid(row = 1 ,  column = 1 , padx = 10 ,  pady = 5)
        """ Phone Number """
        self.PhoneNumber = tk.Label(frameInputs, text = "Phone Number", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PhoneNumber .grid(row = 2 ,  column = 0 , padx = 10)
        self.PhoneNumberE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.PhoneNumberE.grid(row = 2 ,  column = 1 , padx = 10 ,  pady = 5)

        """frame for button save and delete """
        frameButton = tk.Frame(self,bg = '#052B7E' )
        self.ButtonSave = tk.Button(frameButton,text = "SAVE" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.save)
        self.ButtonSave.grid(row=0, column=0, sticky=tk.W , padx = 10 ,  pady = 10)
        self.ButtonReset = tk.Button(frameButton,text = "RESET" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.reset)
        self.ButtonReset.grid(row=0, column=1, sticky=tk.W , padx = 10 ,  pady = 10)
        frameButton.pack()
        """sEARCH FRAME """
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
        columns = ("#1", "#2", "#3") 
        self.tree = ttk.Treeview(frameOthers, show="headings", columns=columns )
        self.tree.heading("#1", text="Company Name")
        self.tree.heading("#2", text="Email")
        self.tree.heading("#3", text="Phone Number")
        ysb = ttk.Scrollbar(frameOthers, orient=tk.VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        self.trees()
        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=2, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
    
    """trees """
    def trees(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT CompanyName,Email,PhoneNumber FROM supplier")
        userrr = cur.fetchall() 
        cur.close()

        for contact in userrr:
            self.tree.insert("", tk.END, values=contact)
            self.tree.bind("<<TreeviewSelect>>")
    
    def save(self):
        if (  (len(self.companyNameE.get()) == 0) or   (len(self.EmailE.get()) == 0)  or (len(self.PhoneNumberE.get()) == 0)):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        else:
            cur = self.mydb.cursor()
            cur.execute(" INSERT INTO supplier(CompanyName,Email,PhoneNumber)"\
            "VALUES (%s,%s,%s)", (self.companyNameE.get(),self.EmailE.get(),self.PhoneNumberE.get()))
            self.mydb.commit()
            cur.close()
            self.tree.delete(*self.tree.get_children())
            self.trees()
            message = "Details Entered successfully!"
            mb.askokcancel(message = message , parent = self)
            self.reset()
    
    def reset(self):
        self.companyNameE.delete(0, tk.END)
        self.EmailE.delete(0, tk.END)
        self.PhoneNumberE.delete(0, tk.END)
        self.companyNameE.focus_set()
    
    def search(self):
        if (len(self.searchEntery.get()) == 0):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        elif((len(self.searchEntery.get()) != 0)):
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT CompanyName,Email,PhoneNumber FROM supplier WHERE  CompanyName LIKE '%{}%' ".format(self.searchEntery.get()))
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


""" Product """

class Product(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Products")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "PRODUCTS", font = ('Times', 20, 'bold' ), fg = 'white' , bg = "#052B7E" )
        titleLabel.pack(pady = 20)
        frameContent = tk.Frame(self,bg = '#052B7E')
        self.tk_value = tk.StringVar()
        self.tk_value.set("OK")
        self.blink_status = 1
        
        
        frameContent.pack()
        """msql connection """
        self.mydb = mysql.connect(
        host = 'localhost',
        user = 'root',
        password  = '',
        database =  'newhospital')
        frameInputs = tk.Frame(frameContent, bg  = '#052B7E' )
        frameInputs.pack(side = tk.LEFT)
        
        """product Name"""
        self.productName = tk.Label(frameInputs, text = "Product Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.productName.grid(row = 0 ,  column = 0 , padx = 10)
        self.productNameE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.productNameE.grid(row = 0 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """ Supplier Name """
        self.SupplierName = tk.Label(frameInputs, text = "Supplier Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.SupplierName.grid(row = 1 ,  column = 0 , padx = 10)
        self.SupplierNameE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.SupplierNameE.insert(0,"Philmed")
        self.SupplierNameE.grid(row = 1 ,  column = 1 , padx = 10 ,  pady = 5)
        """ Batch Number"""
        self.BatchNumber = tk.Label(frameInputs, text = "Batch Number", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.BatchNumber.grid(row = 2 ,  column = 0 , padx = 10)
        self.BatchNumberE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.BatchNumberE.insert(0,"0.00")
        self.BatchNumberE.grid(row = 2 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """Manufactured Date """
        self.ManufacturedDate = tk.Label(frameInputs, text = "Manufactured Date", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.ManufacturedDate.grid(row = 3 ,  column = 0 , padx = 10)
        self.ManufacturedDateE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.ManufacturedDateE.insert(0, "3/2020")
        self.ManufacturedDateE.grid(row = 3 ,  column = 1 , padx = 10 ,  pady = 5)

        """Invoice Number """
        self.InvoiceNumber = tk.Label(frameInputs, text = "Invoice Number", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.InvoiceNumber.grid(row = 4,  column = 0 , padx = 10)
        self.InvoiceNumberE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.InvoiceNumberE.insert(0,"CC122067225")
        self.InvoiceNumberE.grid(row = 4 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """Invoice Date """
        self.InvoiceDate = tk.Label(frameInputs, text = "Invoice Date", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.InvoiceDate .grid(row = 5,  column = 0 , padx = 10)
        self.InvoiceDateE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.InvoiceDateE.insert(0,"4/2/2020")
        self.InvoiceDateE.grid(row = 5 ,  column = 1 , padx = 10 ,  pady = 5)


        """Expiry Date """
        self.ExpiryDate = tk.Label(frameInputs, text = "Expiry Date", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.ExpiryDate.grid(row = 0 ,  column = 2 , padx = 10)
        self.ExpiryDateE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.ExpiryDateE.insert(0,"5/2023")
        self.ExpiryDateE.grid(row = 0 ,  column = 3 , padx = 10 ,  pady = 5)

        """Quantity """
        self.Quantity = tk.Label(frameInputs, text = "Quantity", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Quantity.grid(row = 1 ,  column = 2 , padx = 10)
        self.QuantityE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.QuantityE.grid(row = 1 ,  column = 3 , padx = 10 ,  pady = 5)

        """Buying Price """
        self.BuyingPrice = tk.Label(frameInputs, text = "Buying Price", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.BuyingPrice.grid(row = 2 ,  column = 2 , padx = 10)
        self.BuyingPriceE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.BuyingPriceE.insert(0,"0.00")
        self.BuyingPriceE.grid(row = 2 ,  column = 3 , padx = 10 ,  pady = 5)

        """Selling Price """
        self.SellingPrice = tk.Label(frameInputs, text = "Selling Price", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.SellingPrice.grid(row = 3 ,  column = 2 , padx = 10)
        self.SellingPriceE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.SellingPriceE.insert(0,"0.00")
        self.SellingPriceE.grid(row = 3 ,  column = 3 , padx = 10 ,  pady = 5)

        """Expiry Frame """
        frameExpiry = tk.Frame(frameInputs,bg = '#052B7E' )
        frameExpiry.grid(row = 0 , column = 4 , padx = 10 ,  pady = 5 , rowspan = 7 )
        columns = ("#1") 
        self.expiry = ttk.Treeview(frameExpiry, show="headings", columns=columns )
        self.expiry.heading("#1", text="Expired Drugs(Less than 20 days)")
        ysbb = ttk.Scrollbar(frameExpiry, orient=tk.VERTICAL,command=self.expiry.yview)
        self.expiry.configure(yscroll=ysbb.set)
        
        self.expiry.grid(row=0, column=0)
        ysbb.grid(row=0, column=2, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        

        """frame for button save and delete """
        frameButton = tk.Frame(self,bg = '#052B7E' )
        self.ButtonSave = tk.Button(frameButton,text = "SAVE" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.save)
        self.ButtonSave.grid(row=0, column=0, sticky=tk.W , padx = 10 ,  pady = 10)
        self.ButtonReset = tk.Button(frameButton,text = "RESET" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.reset)
        self.ButtonReset.grid(row=0, column=1, sticky=tk.W , padx = 10 ,  pady = 10)
        frameButton.pack()
        """sEARCH FRAME """
        frameSearch = tk.Frame(self,bg = '#052B7E' )
        frameSearch.pack()
        self.tx_label = tk.Label(frameSearch,textvariable = self.tk_value, relief = tk.GROOVE  ,  height = 2 , bg = 'green')
        self.tx_label.grid(row = 0 , column = 0 , sticky = tk.E)
        self.searchEntery = tk.Entry(frameSearch , font = ('Times',14, 'bold') )
        self.searchEntery.grid(row = 0  , column = 1 , padx = 10 ,  pady = 5 )
        self.SearchButton = tk.Button(frameSearch,text = "SEARCH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' , command =  self.search)
        self.SearchButton.grid(row=0, column=2, sticky=tk.W , padx = 10 ,  pady = 5)
        self.REFRESHButton = tk.Button(frameSearch,text = "REFRESH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' ,  command = self.Refresh)
        self.REFRESHButton.grid(row=0, column=3, sticky=tk.W , padx = 10 ,  pady = 5)

        
            
        
        """Tree """
        frameOthers = tk.Frame(self,bg = '#052B7E' )
        frameOthers.pack(side = tk.TOP )
        columns = ("#1", "#2", "#3" ,"#4", "#5", "#6" ) 
        self.tree = ttk.Treeview(frameOthers, show="headings", columns=columns )
        self.tree.heading("#1", text="product Name")
        self.tree.heading("#2", text="Supplier Name")
        self.tree.heading("#3", text="BatchNumber")
        self.tree.heading("#4", text="Manufactured Date")
        self.tree.heading("#5", text="Expiry Date")
        self.tree.heading("#6", text="Quantity")
        
        
        ysb = ttk.Scrollbar(frameOthers, orient=tk.VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        self.trees()
        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=2, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        """Regular checking date """
        self.waiting()
        
    
  
    """trees """
    def trees(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT productName,SupplierName,BatchNumber,ManufacturedDate,ExpiryDate,Quantity FROM product")
        userrr = cur.fetchall() 
        cur.close()

        for contact in userrr:
            self.tree.insert("", tk.END, values=contact)
            self.tree.bind("<<TreeviewSelect>>")
    
    def save(self):
        if (  (len(self.productNameE.get()) == 0) or   (len(self.SupplierNameE.get()) == 0)  or (len(self.BatchNumberE.get()) == 0) or (len(self.ManufacturedDateE.get()) == 0) or (len(self.ExpiryDateE.get()) == 0) or (len(self.QuantityE.get()) == 0) or (len(self.BuyingPriceE.get()) == 0)  or (len(self.InvoiceNumberE.get()) == 0) or (len(self.InvoiceDateE.get()) == 0) or (len(self.SellingPriceE.get()) == 0) ):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        else:
            manufactured = str(self.ManufacturedDateE.get())
            Expiry = str(self.ExpiryDateE.get())
            Invoiced =  str(self.InvoiceDateE.get())
            manufactureDateTime = datetime.strptime(manufactured,'%m/%Y')
            expiryDateTime = datetime.strptime(Expiry,'%m/%Y')
            invoicedDateTime =  datetime.strptime(Invoiced,'%d/%m/%Y')

            cur = self.mydb.cursor()
            cur.execute(" INSERT INTO product(productName,SupplierName,BatchNumber,ManufacturedDate,ExpiryDate,Quantity,BuyingPrice, InvoiceNumber ,InvoicedDate,SellingPrice)"\
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.productNameE.get(),self.SupplierNameE.get(),self.BatchNumberE.get(),manufactureDateTime,expiryDateTime,self.QuantityE.get(),self.BuyingPriceE.get() ,self.InvoiceNumberE.get(),invoicedDateTime,self.SellingPriceE.get() ))
            self.mydb.commit()
            cur.close()
            self.tree.delete(*self.tree.get_children())
            self.trees()
            message = "Details Entered successfully!"
            mb.askokcancel(message = message , parent = self)
            self.reset()
    
    def reset(self):
        self.productNameE.delete(0, tk.END)
        self.SupplierNameE.delete(0, tk.END)
        self.BatchNumberE.delete(0, tk.END)
        self.ManufacturedDateE.delete(0, tk.END)
        self.ExpiryDateE.delete(0, tk.END)
        self.QuantityE.delete(0, tk.END)
        self.BuyingPriceE.delete(0, tk.END)
        
        self.InvoiceDateE.delete(0, tk.END)
        self.InvoiceNumberE.delete(0, tk.END)
        self.SellingPriceE.delete(0, tk.END)


        self.productNameE.focus_set()
    
    def search(self):
        if (len(self.searchEntery.get()) == 0):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        elif((len(self.searchEntery.get()) != 0)):
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT productName,SupplierName,BatchNumber,ManufacturedDate,ExpiryDate,Quantity FROM product WHERE  productName LIKE '%{}%' ".format(self.searchEntery.get()))
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
    
    def waiting(self):
        self.after(380,self.checkingExp())
    
    
            

            

        
    
    def blink_tx_step_2(self, color = None):
        if color != None:
            self.tx_label["bg"] = color
        self.after(350 , self.blink_tx)
    
    def blink_tx(self):
        if self.blink_status == 1:
            self.tx_label["bg"] = 'green'
            self.tk_value.set('EXPIRING DRUG ALEART!!')
            self.blink_status = random.randint(0,2)
            self.after(100, self.blink_tx_step_2, 'blue')
        elif self.blink_status == 0:
            self.tx_label["bg"] = 'red'
            self.tk_value.set('EXPIRING DRUG ALEART!!')
            self.blink_status = random.randint(0,2)
            self.after(200, self.blink_tx_step_2, 'orange')
        else:
            self.tx_label["bg"] = 'red'
            self.tk_value.set('EXPIRING DRUG ALEART!!')
            self.blink_status = random.randint(0,2)
            self.after(200, self.blink_tx_step_2)
    
    def checkingExp(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT ManufacturedDate,ExpiryDate,productName FROM product ")
        userrr = cur.fetchall() 
        cur.close()
        #print(dt.date.today())
        currentDate = datetime.combine(dt.date.today(), datetime.min.time())
        expired = None
        for dates in userrr:
            sub = dates[1]- currentDate
            print(sub)
            if sub.days <= 20:
                self.expiry.insert("", tk.END, values=dates[2])
                self.expiry.bind("<<TreeviewSelect>>")

                self.blink_tx()


    










        


if __name__ == "__main__":
     app = App()
     app.mainloop()