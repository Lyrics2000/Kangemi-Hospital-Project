import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import csv

from fpdf import FPDF
import datetime

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kangemi Hospital")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "Lab", font = ('Times', 50, 'bold' ), fg = 'white' , bg = "#052B7E" )
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

        
        

        frameInputs = tk.Frame(frameContent, bg  = '#052B7E' )
        frameInputs.pack(side = tk.LEFT)
        

        """Patients Name """
        self.PatientsName = tk.Label(frameInputs, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsName.grid(row = 0 ,  column = 0 , padx = 10)
        self.PatientsNameE = tk.Entry(frameInputs , font = ('Times',14, 'bold') )
        self.PatientsNameE.insert(0,"Cash")
        self.PatientsNameE.grid(row = 0 ,  column = 1 , padx = 10 ,  pady = 5)
        
        
        
        """Test"""
        drugs  = self.selectTest()
        self.DrugTestName = tk.Label(frameInputs, text = "Drug Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.DrugTestName.grid(row = 2 ,  column = 0 , padx = 10)
        self.drugs = ttk.Combobox(frameInputs, values=drugs,font = ('Times', 14, 'bold' ))
        self.drugs.bind("<<ComboboxSelected>>")
        self.drugs.grid(row = 2, column = 1 , padx = 10,  pady = 5)
        
        frameButton = tk.Frame(self,bg = '#052B7E' )
        self.ButtonSave = tk.Button(frameButton,text = "SAVE" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised',command = self.save)
        self.ButtonSave.grid(row=0, column=0, sticky=tk.W , padx = 10 ,  pady = 10)
        self.ButtonReset = tk.Button(frameButton,text = "RESET" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised')
        self.ButtonReset.grid(row=0, column=1, sticky=tk.W , padx = 10 ,  pady = 10)
        frameButton.pack()
        
        frameSearch = tk.Frame(self, bg = '#052B7E'  )
        self.SearchEntry = tk.Entry(frameSearch, font = ('Times',14, 'bold'))
        self.SearchEntry.grid(row=0, column=0, sticky=tk.W , padx =  10)
        self.SearchButton = tk.Button(frameSearch,text = "SEARCH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' )
        self.SearchButton.grid(row=0, column=1, sticky=tk.W , padx = 10)
        self.RefreshButton = tk.Button(frameSearch,text = "REFRESH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' )
        self.RefreshButton.grid(row=0, column=2, sticky=tk.W , padx = 10)
        frameSearch.pack(side = tk.TOP)
        """Tree """
        frameOthers = tk.Frame(self,bg = '#052B7E' )
        """Frame for search """
        
        columns = ("#1", "#2", "#3", "#4") 
        self.tree = ttk.Treeview(frameOthers, show="headings", columns=columns )
        self.tree.heading("#1", text="Test Name")
        self.tree.heading("#2", text="Price")
        self.tree.heading("#3", text="Date")
        self.tree.heading("#4", text="Customer Name")
       
        ysb = ttk.Scrollbar(frameOthers, orient=tk.VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        self.trees()
        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=2, sticky=tk.N + tk.S)
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        frameOthers.pack( pady = 10)
    
    
    
    """trees """
    def trees(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT testName,Price,Date,CustomerName FROM testlaboverthecounter")
        userrr = cur.fetchall() 
        cur.close()

        for contact in userrr:
            self.tree.insert("", tk.END, values=contact)
            self.tree.bind("<<TreeviewSelect>>", ) 
    """selecting the items"""
    def selectTest(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT testName FROM labtest")
        userrr = cur.fetchall() 
        cur.close()

        return userrr[:]
    
    """save items"""
    def save(self):
        if ((len(self.PatientsNameE.get()) == 0) or (len(self.drugs.get()) == 0)):
                message = "Please fill in the required details"
                mb.askokcancel(message = message , parent = self)
               
        else:
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT price FROM labtest WHERE  testName LIKE BINARY '{}' ".format(self.drugs.get()))
            sellingpr = cur.fetchone() 
            cur.close()
            
            x = datetime.datetime.now()
            """placing the data into the database"""
            cur = self.mydb.cursor()
            cur.execute(" INSERT INTO testlaboverthecounter(testName,Price,Date,CustomerName)"\
            "VALUES (%s,%s,%s,%s)", (self.drugs.get(),sellingpr[0],x,self.PatientsNameE.get()))
            self.mydb.commit()
            cur.close()
            message = "Details entered Successfully!!"
            mb.askokcancel(message = message , parent = self)
            
        
        
        
         

        


if __name__ == "__main__":
     app = App()
     app.mainloop()