import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import csv
from datetime import date


 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kangemi Hospital")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "Kangemi Hospital", font = ('Times', 50, 'bold' ), fg = 'white' , bg = "#052B7E" )
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
        self.patientsDetails = tk.Button(patientsButton,text = "PATIENT REGISTRATION" , 
        font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', state = tk.DISABLED , command = self.patientsRegestration)
        self.patientsDetails.pack(padx=10, pady=5, side = tk.LEFT)
        self.account = tk.Button(patientsButton,text = "ACCOUNTS" , font = ('Times',14, 'bold') , fg = 'white' , 
         bg = '#052B7E' , relief = 'raised',state = tk.DISABLED ,command = self.reset)
        self.account.pack(padx=10, pady=5 , side = tk.LEFT)
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
                self.patientsDetails.config(state = tk.NORMAL)
                self.account.config(state = tk.NORMAL)
                
                
            else:
                message = "Password entered is incorrect!!"
                mb.askokcancel(message= message ,  parent =  self)
                self.patientsDetails.config(state = tk.DISABLED)
                self.account.config(state = tk.DISABLED)
    def patientsRegestration(self):
        window  = PatientsDetails(self)
        window.grab_set()

         
class PatientsDetails(tk.Toplevel):
    
    
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Patients Details")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "Kangemi Hospital", font = ('Times', 20, 'bold' ), fg = 'white' , bg = "#052B7E" )
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
        self.OPNumberL = tk.Label(frameLabels, text = "OP Number", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E"  )
        self.OPNumberL.grid(row = 0 ,  column = 0 , padx = 10)
        self.PatientsNameL = tk.Label(frameLabels, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsNameL.grid(row = 1 ,  column = 0 , padx = 10)
        self.AgeL = tk.Label(frameLabels, text = "Age", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.AgeL.grid(row = 2 ,  column = 0 , padx = 10)
        self.GenderL = tk.Label(frameLabels, text = "Gender", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.GenderL.grid(row = 3 ,  column = 0 , padx = 10)
        self.MaritalL = tk.Label(frameLabels, text = "Marital status", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.MaritalL.grid(row = 4 ,  column = 0 , padx = 10)
        self.PostalL = tk.Label(frameLabels, text = "Postal Adress", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PostalL.grid(row = 5 ,  column = 0 , padx = 10)
        self.PhysicalL = tk.Label(frameLabels, text = "Physical Address", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PhysicalL.grid(row = 6 ,  column = 0 , padx = 10)
        self.VisitingL = tk.Label(frameLabels, text = "Visiting Day", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.VisitingL.grid(row = 7 ,  column = 0 , padx = 10)
        self.TelephoneL = tk.Label(frameLabels, text = "Tell Number", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.TelephoneL.grid(row = 0 ,  column = 2 , padx = 10)
        self.EmailL = tk.Label(frameLabels, text = "Email", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.EmailL.grid(row = 1 ,  column = 2 , padx = 10)
        self.FoodL = tk.Label(frameLabels, text = "Food Allergies", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.FoodL.grid(row = 2 ,  column = 2 , padx = 10)
        self.DrugL = tk.Label(frameLabels, text = "Drug Allergies", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.DrugL.grid(row = 3 ,  column = 2 , padx = 10)
        self.OtherL = tk.Label(frameLabels, text = "Other Allergies", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.OtherL.grid(row = 4 ,  column = 2 , padx = 10)
        self.PaymentL = tk.Label(frameLabels, text = "Payment Method", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PaymentL.grid(row = 5 ,  column = 2 , padx = 10)
        self.EmployerL = tk.Label(frameLabels, text = "Employer", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.EmployerL.grid(row = 6 ,  column = 2 , padx = 10)

        

        frameRegestration = tk.Frame(frameContent,bg = '#052B7E' )
        self.OPNumber = tk.Label(frameRegestration, text = "OP Number", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.OPNumber.grid(row = 0 ,  column = 0 , padx = 10)
        self.OPNumberEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.OPNumberEntry.grid(row = 0 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """patients Name """
        self.PatientsName = tk.Label(frameRegestration, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsName.grid(row = 1 ,  column = 0 , padx = 10)
        self.PatientsNameEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.PatientsNameEntry.grid(row = 1 ,  column = 1 , padx = 10 , pady = 5)
        frameRegestration.pack(side = tk.LEFT)
        """patients Age """
        self.PatientsAge = tk.Label(frameRegestration, text = "Patients Age", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsAge.grid(row = 2 ,  column = 0 , padx = 10)
        self.PatientsAgeEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.PatientsAgeEntry.grid(row = 2 ,  column = 1 , padx = 10 , pady = 5)
        
        """gender combobox """
        gender  = ("Male", "Female")
        self.Gender = tk.Label(frameRegestration, text = "Gender", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Gender.grid(row = 3 ,  column = 0 , padx = 10)
        self.gender = ttk.Combobox(frameRegestration, values=gender,font = ('Times', 14, 'bold' ))
        self.gender.bind("<<ComboboxSelected>>", self.create_gender)
        self.gender.grid(row = 3 , column = 1 , padx = 10,  pady = 5)

        """Marital Status """
        marital  = ("Married", "Single" , "Divorced" , "Complicated")
        self.marital = tk.Label(frameRegestration, text = "Marital Status", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.marital.grid(row = 4 ,  column = 0 , padx = 10)
        self.marital = ttk.Combobox(frameRegestration, values=marital,font = ('Times', 14, 'bold' ))
        self.marital.bind("<<ComboboxSelected>>", self.create_marital)
        self.marital.grid(row = 4 , column = 1 ,padx = 10 ,  pady = 5)
        """Postal Address """
        self.PostalAddress = tk.Label(frameRegestration, text = "Postal Address", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PostalAddress.grid(row = 5 ,  column = 0 , padx = 10)
        self.PostalAddressEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.PostalAddressEntry.grid(row = 5 ,  column = 1 , padx = 10 , pady = 5)
        """Physical Address """
        self.PhysicalAddress = tk.Label(frameRegestration, text = "Physical Address", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PhysicalAddress.grid(row = 6 ,  column = 0 , padx = 10)
        self.PhysicalAddressEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.PhysicalAddressEntry.grid(row = 6 ,  column = 1 , padx = 10 , pady = 5)
        """Telephone Number """
        self.Tell = tk.Label(frameRegestration, text = "Telephone Number", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Tell.grid(row = 0 ,  column = 2 , padx = 10)
        self.TellEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.TellEntry.grid(row = 0 ,  column = 3 , padx = 10 , pady = 5)
        """Email """
        self.Email = tk.Label(frameRegestration, text = "Email", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Email.grid(row = 1 ,  column = 2 , padx = 10)
        self.EmailEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.EmailEntry.grid(row = 1 ,  column = 3 , padx = 10 , pady = 5)
        """Food Allergies """
        self.Food = tk.Label(frameRegestration, text = "Food Allergies", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Food.grid(row = 2 ,  column = 2 , padx = 10)
        self.FoodEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.FoodEntry.grid(row = 2 ,  column = 3 , padx = 10 , pady = 5)

        """Drug Allergies """
        self.Drug = tk.Label(frameRegestration, text = "Drug Allergies", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Drug.grid(row = 3 ,  column = 2 , padx = 10)
        self.DrugEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.DrugEntry.grid(row = 3 ,  column = 3 , padx = 10 , pady = 5)

        """Other Allergies """
        self.Other = tk.Label(frameRegestration, text = "Other Allergies", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Other.grid(row = 4 ,  column = 2 , padx = 10)
        self.OtherEntry = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.OtherEntry.grid(row = 4 ,  column = 3 , padx = 10 , pady = 5)

        """Payments """
        payment  = ("Cash", "Cooperate")
        self.payment = tk.Label(frameRegestration, text = "Payment", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.payment.grid(row = 5 ,  column = 2 , padx = 10)
        self.payment = ttk.Combobox(frameRegestration, values=payment,font = ('Times', 14, 'bold' ))
        self.payment.bind("<<ComboboxSelected>>", self.create_payment)
        self.payment.grid(row = 5 , column = 3 , padx = 10,  pady = 5)

        """Employer """
        self.Employer = tk.Label(frameRegestration, text = "Employer", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Employer.grid(row = 6 ,  column = 2 , padx = 10)
        self.Employer = tk.Entry(frameRegestration , font = ('Times',14, 'bold') )
        self.Employer.grid(row = 6 ,  column = 3 , padx = 10 , pady = 5)

        frameRegButtons = tk.Frame(self,bg = '#052B7E' )
        self.save = tk.Button(frameRegButtons,text = "SAVE" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' , command =  self.btnSave)
        self.save.pack(padx=10, pady=5, side = tk.LEFT )
        self.clear = tk.Button(frameRegButtons,text = "CLEAR" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' , command = self.clear)
        self.clear.pack(padx=10, pady=5 , side = tk.LEFT)
        frameRegButtons.pack(pady = 10 , )

        frameSearch = tk.Frame(self, bg = '#052B7E'  )
        self.SearchEntry = tk.Entry(frameSearch, font = ('Times',14, 'bold'))
        self.SearchEntry.grid(row=0, column=0, sticky=tk.W , padx =  10)
        self.SearchButton = tk.Button(frameSearch,text = "SEARCH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' ,  command = self.search)
        self.SearchButton.grid(row=0, column=1, sticky=tk.W , padx = 10)
        self.RefreshButton = tk.Button(frameSearch,text = "REFRESH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' , command = self.refresh)
        self.RefreshButton.grid(row=0, column=2, sticky=tk.W , padx = 10)
        frameSearch.pack(side = tk.TOP)
        """Tree """
        frameOthers = tk.Frame(self,bg = '#052B7E' )
        """Frame for search """
        
        columns = ("#1", "#2", "#3", "#4","#5" , "#6"  ) 
        self.tree = ttk.Treeview(frameOthers, show="headings", columns=columns )
        self.tree.heading("#1", text="OP Number")
        self.tree.heading("#2", text="Patients Name")
        self.tree.heading("#3", text="AGE")
        self.tree.heading("#4", text="Gender")
        self.tree.heading("#5", text="Marital Status")
        self.tree.heading("#6", text="Postal Address")
        ysb = ttk.Scrollbar(frameOthers, orient=tk.VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        self.trees()
        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=2, sticky=tk.N + tk.S)
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        frameOthers.pack(side = tk.TOP ,  fill = tk.X  ,padx = 50 )
        
        """
        cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT * FROM user WHERE user_name = %s",([self.user.get()]))
           
            userr = cur.fetchall() 
            cur.close()

            """

    
        

    """trees """
    def trees(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT OpNumber ,PatientName ,Age,Gender,MaritalStatus,PostalAddress FROM patients")
        userrr = cur.fetchall() 
        cur.close()

        for contact in userrr:
            self.tree.insert("", tk.END, values=contact)
            self.tree.bind("<<TreeviewSelect>>", self.print_selection) 
    """ Button save """
    def btnSave(self, *args):
        print(self.OPNumberEntry.get())
        print(self.PatientsNameEntry.get())
        print(self.PatientsAgeEntry.get())
        print(self.gender.get())
        print(self.marital.get())
        print(self.PostalAddressEntry.get())
        print(self.PhysicalAddressEntry.get())
        print(self.TellEntry.get())
        print(self.EmailEntry.get())
        print(self.FoodEntry.get())
        print(self.DrugEntry.get())
        print(self.OtherEntry.get())
        print(self.payment.get())
        print(self.Employer.get())
        print(self.PatientsAgeEntry.get())
        if (len(self.OPNumberEntry.get()) == 0) or (len(self.PatientsNameEntry.get()) == 0) or (len(self.PatientsAgeEntry.get()) == 0) or (len(self.gender.get()) == 0 ) or (len(self.marital.get()) == 0 ) or (len(self.PostalAddressEntry.get()) == 0) or (len(self.PhysicalAddressEntry.get()) == 0) or (len(self.TellEntry.get()) == 0 ) or (len(self.EmailEntry.get()) == 0) or (len(self.FoodEntry.get()) == 0) or (len(self.DrugEntry.get())== 0) or (len(self.OtherEntry.get()) == 0) or (len(self.payment.get())== 0) or (len(self.Employer.get()) == 0):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        else:
            cur = self.mydb.cursor()
            cur.execute(" INSERT INTO patients(OpNumber,PatientName,Age,Gender,MaritalStatus,PostalAddress,PhysicalAddress,VisitingDay,TellNumber,Email,FoodAllergies,DrugAllergies,OtherAllergies,PaymentMethod,Employer)"\
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.OPNumberEntry.get(),self.PatientsNameEntry.get(),self.PatientsAgeEntry.get(),self.gender.get(),self.marital.get(),self.PostalAddressEntry.get(),self.PhysicalAddressEntry.get(),date.today(),self.TellEntry.get(),self.EmailEntry.get(),self.FoodEntry.get(),self.DrugEntry.get(),self.OtherEntry.get(),self.payment.get(),self.Employer.get()))
            self.mydb.commit()
            cur.close()
            self.tree.delete(*self.tree.get_children())
            self.trees()
            message = "Details Entered successfully!"
            mb.askokcancel(message = message , parent = self)
            


        


    """CLEAR ENTRIES """ 
    def clear(self, *args):
        self.OPNumberEntry.delete(0, tk.END)
        self.PatientsNameEntry.delete(0, tk.END)
        self.PatientsAgeEntry.delete(0 , tk.END)
        self.gender.delete(0 , tk.END)
        self.marital.delete(0 , tk.END)
        self.PostalAddressEntry.delete(0, tk.END)
        self.PhysicalAddressEntry.delete(0 , tk.END)
        self.TellEntry.delete(0  , tk.END)
        self.EmailEntry.delete(0 , tk.END)
        self.FoodEntry.delete(0 , tk.END)
        self.DrugEntry.delete( 0  , tk.END)
        self.OtherEntry.delete( 0 , tk.END)
        self.payment.delete( 0 , tk.END)
        self.Employer.delete(0, tk.END)
        self.OPNumberEntry.focus_set()
    
    
    
    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.trees()

    def search(self):
        if (len(self.SearchEntry.get()) == 0):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        elif((len(self.SearchEntry.get()) != 0)):
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT OpNumber ,PatientName ,Age,Gender,MaritalStatus,PostalAddress FROM patients WHERE  PatientName LIKE '%{}%' ".format(self.SearchEntry.get()))
            userrr = cur.fetchall() 
            cur.close()
            self.tree.delete(*self.tree.get_children())

            for contact in userrr:
                self.tree.insert("", tk.END, values=contact)
                self.tree.bind("<<TreeviewSelect>>", self.print_selection)
        else:
            message = "Record Not Found!!"
            mb.askokcancel(message = message , parent = self)
            self.trees()

            




    def print_selection(self, event):
        for selection in self.tree.selection():
            item = self.tree.item(selection)
            opNumber = item["values"][0]
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT * FROM patients WHERE  OpNumber  = {} ".format(opNumber))
            userrr = cur.fetchone() 
            cur.close()
            self.OPNumberL.config(text = "OP NUMBER: {}" .format(userrr[1]))
            self.PatientsNameL.config(text = "PATIENTS Name: {}" .format(userrr[2]))
            self.AgeL.config(text = "PATIENTS Age: {}" .format(userrr[3]))
            self.GenderL.config(text = "PATIENTS Gender: {}" .format(userrr[4]))
            self.MaritalL.config(text = "Marital Status: {}" .format(userrr[5]))
            self.PostalL.config(text = "Postal Address: {}" .format(userrr[6]))
            self.PhysicalL.config(text = "Physical Address: {}" .format(userrr[7]))
            self.VisitingL.config(text = "Visiting day: {}" .format(userrr[8]))
            self.TelephoneL.config(text = "Tell No: {}" .format(userrr[9]))
            self.EmailL.config(text = "Email: {}" .format(userrr[10]))
            self.FoodL.config(text = "Food Allergies: {}" .format(userrr[11]))
            self.DrugL.config(text = "Drug Allergies: {}" .format(userrr[12]))
            self.OtherL.config(text = "Other Allergies: {}" .format(userrr[13]))
            self.PaymentL.config(text = "Payment: {}" .format(userrr[14]))
            self.EmployerL.config(text = "Employer: {}" .format(userrr[15]))

            
    def create_gender(self,*args):
        color = self.gender.get()
        print("Your selection is", color)
    def create_marital(self,*args):
        color = self.marital.get()
        print("Your selection is", color)
    def create_payment(self,*args):
        color = self.payment.get()
        print("Your selection is", color)
        

            

        

       

        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()