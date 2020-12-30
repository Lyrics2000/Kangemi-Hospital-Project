import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import csv

from fpdf import FPDF
import datetime
from listitems import ListFrame
from datetime import date

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

        """TEST RECORDS"""
        self.testRecord = tk.Button(patientsButton,text = "Test Records" , 
        font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', state = tk.DISABLED , command = self.TestRecords)
        self.testRecord.pack(padx=10, pady=5, side = tk.LEFT)
        
        """OVER THE COUNTER """
        self.overthecounter = tk.Button(patientsButton,text = "Over The Counter" , 
        font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', state = tk.DISABLED, command = self.OverCounter )
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
                self.testRecord.config(state = tk.NORMAL)
                
                
                
            else:
                message = "Password entered is incorrect!!"
                mb.askokcancel(message= message ,  parent =  self)
                self.overthecounter.config(state = tk.DISABLED)
                self.patientsSales.config(state = tk.DISABLED)
                
   
    
    
    
    def TestRecords(self):
        window = TestRecords(self)
        window.grab_set()
        
    def OverCounter(self):
        window = OverTheCounterAndPatientsWindow(self)
        window.grab_set()
        
"""Test Record """
class TestRecords(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Test Records")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = "Test Records", font = ('Times', 20, 'bold' ), fg = 'white' , bg = "#052B7E" )
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
        self.RefreshButton = tk.Button(frameSearch,text = "REFRESH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised', command = self.refresh)
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
    
    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.trees()
            

class OverTheCounterAndPatientsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Kangemi Hospital Lab")
        self.geometry("1350x750+0+0")
        self.configure(background = "#052B7E" )
        """ creating a title label """
        titleLabel = tk.Label(self, text = " Lab ", font = ('Times', 20, 'bold' ), fg = 'white' , bg = "#052B7E" )
        titleLabel.pack(pady = 20)
        frameContent = tk.Frame(self,bg = '#052B7E')
        frameContent.pack()
        """msql connection """
        self.mydb = mysql.connect(
        host = 'localhost',
        user = 'root',
        password  = '',
        database =  'newhospital')
        
        self.TEST_RESULTS = None
        self.ttest = None
        self.var = None
        
        frameOne = tk.Frame(frameContent, bg  = '#247FFF' )
        frameOne.pack(side = tk.LEFT, fill=tk.BOTH)
        self.loginButton = tk.Button(frameOne,text = "Over The Counter" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised',command = self.forgetPack)
        self.loginButton.pack(padx=10, pady=5, side = tk.LEFT)
        
        frameTwo = tk.Frame(frameContent, bg  = '#FFF' )
        frameTwo.pack(side = tk.LEFT, fill=tk.BOTH)
        self.loginButton = tk.Button(frameTwo,text = "Patients" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised',command = self.PatientFramePack)
        self.loginButton.pack(padx=10, pady=5, side = tk.LEFT)
       
        self.frameThree = tk.Frame(self, bg  = '#052B7E' )
        self.frameThree.pack(padx=10, pady=5,side = tk.TOP, fill=tk.BOTH)
        
        self.frameFour = tk.Frame(self.frameThree, bg = '#052B7E' )
        self.frameFour.pack(side = tk.TOP, fill=tk.BOTH)
        
        """ container for tree view of patients detail """
        self.framePatientsDetailstree = tk.Frame(self.frameFour, bg = '#052B7E' )
        self.framePatientsDetailstree .pack(side = tk.LEFT, fill=tk.BOTH)
        
        """ Frame container for search button and refresh button """
        self.frametreepatentsseacrh = tk.Frame(self.framePatientsDetailstree, bg = '#052B7E' )
        self.frametreepatentsseacrh.pack(side = tk.TOP, fill=tk.BOTH)
        
        self.SearchEntry = tk.Entry(self.frametreepatentsseacrh, font = ('Times',14, 'bold'))
        self.SearchEntry.grid(row=0, column=0, sticky=tk.W , padx =  10)
        self.SearchButton = tk.Button(self.frametreepatentsseacrh,text = "SEARCH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' , command = self.search )
        self.SearchButton.grid(row=0, column=1, sticky=tk.W , padx = 10)
        self.RefreshButton = tk.Button(self.frametreepatentsseacrh,text = "REFRESH" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised' , command = self.refresh )
        self.RefreshButton.grid(row=0, column=2, sticky=tk.W , padx = 10)
        
        
        """ frame container for the trees """
        self.frametreepatents = tk.Frame(self.framePatientsDetailstree, bg = '#052B7E' )
        self.frametreepatents.pack(side = tk.TOP, fill=tk.BOTH)
        
        columns = ("#1", "#2", ) 
        self.tree = ttk.Treeview(self.frametreepatents, show="headings", columns=columns )
        self.tree.heading("#1", text="OP Number")
        self.tree.heading("#2", text="Patients Name")
        ysb = ttk.Scrollbar(self.frametreepatents, orient=tk.VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        self.trees()
        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=2, sticky=tk.N + tk.S)
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        """ Frame container printing results """
        self.framepatientientprintresults = tk.Frame(self.frameFour, bg = '#052B7E' )
        self.framepatientientprintresults.pack(side = tk.LEFT, fill=tk.BOTH)
        self.OpN = None
        self.agerp = None
        self.genderp = None
        """Bio data container """
        self.framepatientientBiodata = tk.Frame(self.framepatientientprintresults, bg = '#052B7E' )
        self.framepatientientBiodata.pack(side = tk.LEFT, fill=tk.BOTH)
        """personal infor """
        self.framepatientientBiodatabbh = tk.Frame(self.framepatientientBiodata, bg = '#052B7E' )
        self.framepatientientBiodatabbh.pack(side = tk.TOP, fill=tk.BOTH)
        
        """patients Name """
        self.PatientsInName = tk.Label(self.framepatientientBiodatabbh, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsInName.grid(row = 0 ,  column = 0 , padx = 10)
        self.PatientsInNameL = tk.Label(self.framepatientientBiodatabbh, text = " ", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsInNameL.grid(row = 0 ,  column = 1 , padx = 10)
        
        """ Patients Lab No """
        self.PatientsInNameLab = tk.Label(self.framepatientientBiodatabbh, text = "Patients Lab No", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsInNameLab.grid(row = 1 ,  column = 0 , padx = 10)
        self.PatientsInNamLo = tk.Label(self.framepatientientBiodatabbh, text = " ", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsInNamLo.grid(row = 1 ,  column = 1 , padx = 10)
        
        """listbox """
        self.framepatientientBiodatalistbox = tk.Frame(self.framepatientientBiodata, bg = '#052B7E' )
        self.framepatientientBiodatalistbox.pack(side = tk.TOP, fill=tk.BOTH)
        
        alt = self.alltes()
        self.frame_ap = ListFrame(self.framepatientientBiodatalistbox, alt)
        self.frame_bp = ListFrame(self.framepatientientBiodatalistbox)
        self.btn_rightp = tk.Button(self.framepatientientBiodatalistbox, text=">",command=self.move_rightp)
        self.btn_leftp = tk.Button(self.framepatientientBiodatalistbox, text="<",command=self.move_leftp)
        self.frame_ap.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_bp.pack(side=tk.RIGHT, padx=10, pady=10)
        self.btn_rightp.pack(expand=True, ipadx=5)
        self.btn_leftp.pack(expand=True, ipadx=5)
        
        self.frameoverBtnp = tk.Frame(self.framepatientientBiodata, bg = '#052B7E' )
        self.frameoverBtnp.pack(padx=10, pady=5,side = tk.TOP, fill=tk.BOTH)
        self.resultsp = tk.Button(self.frameoverBtnp,text = "Results" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised',command = self.resultssp)
        self.resultsp.pack(padx=10, pady=5, side = tk.LEFT)
        
        """ frame biodata results """
        self.framepatientientBiodataresults = tk.Frame(self.framepatientientprintresults, bg = '#052B7E' )
        self.framepatientientBiodataresults.pack(side = tk.LEFT, fill=tk.BOTH)
        
        self.resultSelectionp = tk.Frame(self.framepatientientBiodataresults, bg = '#052B7E')
        self.resultSelectionp.pack(padx=10, pady=5,side = tk.LEFT, fill=tk.BOTH)
        self.TestNamep = tk.Label(self.resultSelectionp, text = "None Selected", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.TestNamep.pack(padx = 10)
        
        self.createbtnp()
        
        
        
        
        
        
        
        self.frameFive = tk.Frame(self.frameThree, bg = '#052B7E' )
        self.frameFive.pack_forget()
        #frame for result selection
        self.selfselection = tk.Frame(self.frameFive , bg = '#052B7E' )
        self.selfselection.pack(padx=10, pady=5,side = tk.LEFT, fill=tk.BOTH)
        
        """Patients Name """
        self.frameoverthecounterpatient = tk.Frame(self.selfselection, bg = '#052B7E' )
        self.frameoverthecounterpatient.pack(padx=10, pady=5,side = tk.TOP, fill=tk.BOTH)
        self.PatientsName = tk.Label(self.frameoverthecounterpatient, text = "Patients Name", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsName.grid(row = 0 ,  column = 0 , padx = 10)
        self.PatientsNameE = tk.Entry(self.frameoverthecounterpatient, font = ('Times',14, 'bold') )
        
        self.PatientsNameE.grid(row = 0 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """gender combobox """
        gender  = ("Male", "Female")
        self.Gender = tk.Label(self.frameoverthecounterpatient, text = "Gender", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.Gender.grid(row = 1 ,  column = 0 , padx = 10)
        self.gender = ttk.Combobox(self.frameoverthecounterpatient, values=gender,font = ('Times', 14, 'bold' ))
        self.gender.bind("<<ComboboxSelected>>", self.create_gender)
        self.gender.grid(row = 1 , column = 1 , padx = 10,  pady = 5)
        
        """Age """
        self.PatientsAge = tk.Label(self.frameoverthecounterpatient, text = "Patients Age", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsAge.grid(row = 2 ,  column = 0 , padx = 10)
        self.PatientsAgeE = tk.Entry(self.frameoverthecounterpatient, font = ('Times',14, 'bold') )
        self.PatientsAgeE.grid(row = 2 ,  column = 1 , padx = 10 ,  pady = 5)
        
        """ Lab No """
        self.PatientsLabNo = tk.Label(self.frameoverthecounterpatient, text = "Lab No", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsLabNo.grid(row = 3 ,  column = 0 , padx = 10)
        self.PatientsLabNo = tk.Label(self.frameoverthecounterpatient, text = " ", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.PatientsLabNo.grid(row = 3 ,  column = 1 , padx = 10)

       
        
        """ Test Records """
        self.frameoverthecounterrecords = tk.Frame(self.selfselection, bg = '#052B7E' )
        self.frameoverthecounterrecords.pack(padx=10, pady=5,side = tk.TOP, fill=tk.BOTH)
        months = self.alltest()
        self.frame_a = ListFrame(self.frameoverthecounterrecords, months)
        self.frame_b = ListFrame(self.frameoverthecounterrecords)
        self.btn_right = tk.Button(self.frameoverthecounterrecords, text=">",command=self.move_right)
        self.btn_left = tk.Button(self.frameoverthecounterrecords, text="<",command=self.move_left)
        self.frame_a.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_b.pack(side=tk.RIGHT, padx=10, pady=10)
        self.btn_right.pack(expand=True, ipadx=5)
        self.btn_left.pack(expand=True, ipadx=5)
        
        """Frame Buttons """
        self.frameoverBtn = tk.Frame(self.selfselection, bg = '#052B7E' )
        self.frameoverBtn.pack(padx=10, pady=5,side = tk.TOP, fill=tk.BOTH)
        self.results = tk.Button(self.frameoverBtn,text = "Results" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised',command = self.resultss)
        self.results.pack(padx=10, pady=5, side = tk.LEFT)
        
        #result selection 
       
        self.resultSelection = tk.Frame(self.frameFive, bg = '#052B7E')
        self.resultSelection.pack(padx=10, pady=5,side = tk.LEFT, fill=tk.BOTH)
        self.TestName = tk.Label(self.resultSelection, text = "None Selected", font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#052B7E" )
        self.TestName.pack(padx = 10)
        # self.var = None
        self.createbtn()
        
        
        
        
        
    """trees """
    def trees(self):
        cur = self.mydb.cursor()
        resultValue = cur.execute("SELECT OpNumber ,PatientName FROM patients")
        userrr = cur.fetchall() 
        cur.close()

        for contact in userrr:
            self.tree.insert("", tk.END, values=contact)
            self.tree.bind("<<TreeviewSelect>>", self.print_selection )    
        
    
    def forgetPack(self):
        self.frameFour.pack_forget()
        self.frameFive.pack(padx=10, pady=5,side = tk.TOP, fill=tk.BOTH)
        
    def PatientFramePack(self):
        self.frameFour.pack(padx=10, pady=5,side = tk.TOP, fill=tk.BOTH)
        self.frameFive.pack_forget()
    
    
    def print_selection(self, event):
        for selection in self.tree.selection():
            item = self.tree.item(selection)
            opNumber = item["values"][0]
            cur = self.mydb.cursor()
            resultValue = cur.execute("SELECT * FROM patients WHERE  OpNumber  = {} ".format(opNumber))
            userrr = cur.fetchone() 
            cur.close()
            self.OpN = userrr[1]
            
            self.PatientsInNameL.config(text = "{}" .format(userrr[2]))
            self.agerp = userrr[3]
            self.genderp = userrr[4]
    def move_right(self):
        self.move(self.frame_a, self.frame_b)
    def move_left(self):
        self.move(self.frame_b, self.frame_a)
    
    def move_rightp(self):
        self.move(self.frame_ap, self.frame_bp)
    def move_leftp(self):
        self.move(self.frame_bp, self.frame_ap)
    
    def move(self, frame_from, frame_to):
        value = frame_from.pop_selection()
        if value:
            frame_to.insert_item(value)
    
    def resultss(self):
        test = self.frame_b.get_index_list()
        print(test[0])
        if (len(self.PatientsNameE.get()) == 0) or  (len(self.gender.get()) == 0 ) or (len(self.PatientsAgeE.get()) == 0 ) or (len(self.PatientsLabNo.cget("text"))== 0):
            message = "Please fill in the required details"
            mb.askokcancel(message = message , parent = self)
        else:
            if test[0] == 'pregnancy':
                result = [("Positive", "positive"), ("Negative" , "negative")]
                self.TEST_RESULTS = result
                self.var = tk.StringVar()
                self.TestName.config(text = test )
                self.ttest = test[0]
                self.var.set("positive")
            elif test[0] == 'Hiv test':
                result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
                self.TEST_RESULTS = result
                self.var = tk.StringVar()
                self.TestName.config(text = test )
                self.ttest = test[0]
                self.var.set("reactive")
            elif test[0] == 'salmonela test':
                result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
                self.TEST_RESULTS = result
                self.var = tk.StringVar()
                self.TestName.config(text = test )
                self.ttest = test[0]
                self.var.set("reactive")
            elif test[0] == 'Blood Group':
                result = [("A", "A"), ("B" , "B"),("O" , "O"),("AB" , "AB")]
                self.TEST_RESULTS = result
                self.var = tk.StringVar()
                self.TestName.config(text = test )
                self.ttest = test[0]
                self.var.set("A")
            elif test[0] == 'VDRL':
                result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
                self.TEST_RESULTS = result
                self.var = tk.StringVar()
                self.TestName.config(text = test )
                self.ttest = test[0]
                self.var.set("reactive")
            elif test[0] == 'HABSG':
                result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
                self.TEST_RESULTS = result
                self.var = tk.StringVar()
                self.TestName.config(text = test )
                self.ttest = test[0]
                self.var.set("reactive")
            elif test[0] == 'PSA':
                result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
                self.TEST_RESULTS = result
                self.var = tk.StringVar()
                self.TestName.config(text = test )
                self.ttest = test[0]
                self.var.set("reactive")
                
                
            self.createbtn()
            
    def resultssp(self):
        test = self.frame_bp.get_index_list()
        if test[0] == 'pregnancy':
            result = [("Positive", "positive"), ("Negative" , "negative")]
            self.TEST_RESULTS = result
            self.var = tk.StringVar()
            self.TestNamep.config(text = test )
            self.ttest = test[0]
            self.var.set("positive")
        elif test[0] == 'Hiv test':
            result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
            self.TEST_RESULTS = result
            self.var = tk.StringVar()
            self.TestNamep.config(text = test )
            self.ttest = test[0]
            self.var.set("reactive")
        elif test[0] == 'salmonela test':
            result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
            self.TEST_RESULTS = result
            self.var = tk.StringVar()
            self.TestNamep.config(text = test )
            self.ttest = test[0]
            self.var.set("reactive")
        elif test[0] == 'Blood Group':
            result = [("A", "A"), ("B" , "B"),("O" , "O"),("AB" , "AB")]
            self.TEST_RESULTS = result
            self.var = tk.StringVar()
            self.TestNamep.config(text = test )
            self.ttest = test[0]
            self.var.set("A")
        elif test[0] == 'VDRL':
            result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
            self.TEST_RESULTS = result
            self.var = tk.StringVar()
            self.TestNamep.config(text = test )
            self.ttest = test[0]
            self.var.set("reactive")
        elif test[0] == 'Hepatitis-B':
            result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
            self.TEST_RESULTS = result
            self.var = tk.StringVar()
            self.TestNamep.config(text = test )
            self.ttest = test[0]
            self.var.set("reactive")
        elif test[0] == 'Prostrate Specific Antigen (PSA)':
            result = [("Reactive", "reactive"), ("NonReactive" , "non Reactive")]
            self.TEST_RESULTS = result
            self.var = tk.StringVar()
            self.TestNamep.config(text = test )
            self.ttest = test[0]
            self.var.set("reactive")
            
            
        self.createbtnp()
            
        
    
    def createbtn(self):
        if self.TEST_RESULTS:
            resultRadiobtn = [self.create_radio(c) for c in self.TEST_RESULTS]
            for button in resultRadiobtn:
                button.pack(anchor=tk.W, padx=10, pady=5)
            self.printButton= tk.Button(self.resultSelection,text = "Print Results" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised',command  =  self.print_details)
            self.printButton.pack(anchor=tk.W, padx=10, pady=5)
    
    def createbtnp(self):
        if self.TEST_RESULTS:
            resultRadiobtn = [self.create_radiop(c) for c in self.TEST_RESULTS]
            for button in resultRadiobtn:
                button.pack(anchor=tk.W, padx=10, pady=5)
            self.printButton= tk.Button(self.resultSelectionp,text = "Print Results" , font = ('Times',14, 'bold') , fg = 'white' ,  bg = '#052B7E' , relief = 'raised',command  =  self.print_detailsp)
            self.printButton.pack(anchor=tk.W, padx=10, pady=5)
        
    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(self.resultSelection,text=text, value=value,command=self.print_option,variable=self.var, font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#247FFF")
    
    def create_radiop(self, option):
        text, value = option
        return tk.Radiobutton(self.resultSelectionp,text=text, value=value,command=self.print_option,variable=self.var, font = ('Times', 14, 'bold' ), fg = 'white' , bg = "#247FFF")
        
    def print_option(self):
        print(self.var.get())
    
    def resultsPrint(self):
        print(self.var.get())
    def print_details(self):
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Times"  ,size= 15)
        pdf.cell(200, 10 , txt = "CARELINK MEDICAL CENTRE" , ln = 1 , align = 'C')
        pdf.cell(200, 10 , txt = "AT Mzee Juma's Flats " , ln = 2 , align = 'C')
        pdf.cell(200, 10 , txt = "Waruku bypass Near Kangemi Memorial Park -  WARUKU" , ln = 3 , align = 'C')
        pdf.cell(200, 10 , txt = "P.O Box 14496-00800" , ln = 4 , align = 'C')
        pdf.cell(200, 10 , txt = "Nairobi" , ln = 5 , align = 'C')
        pdf.cell(200, 10 , txt = "Tell : 0727546794" , ln = 6 , align = 'C')

        pdf.set_font("Times"  ,'B' ,size= 15)
        # pdf.cell(200, 10 , txt = "{}".format(self.paymentssL.cget("text")) , ln = 7 , align = 'C')

        pdf.set_font("Times" , 'B' ,size= 15)
        pdf.cell(200, 10 , txt = " Date : {} ".format(datetime.date.today()) , ln = 9 , align = 'L')
        pdf.cell(200, 10 , txt = 'Patients Name : {} '.format(self.PatientsNameE.get()) , ln = 9 , align = 'L')
        
        
        
        
        pdf.set_font("Times" , 'B' ,size= 15)
        pdf.cell(40,10,'Gender : {}'.format(self.gender.get()),2 , 0)
        pdf.cell(40,10,'Age: {}'.format(self.PatientsAgeE.get()) , 2, 0)
        pdf.cell(40,10,'Lab No : {}'.format(self.PatientsLabNo.cget("text")) ,2, 0)
        

      
        
        pdf.set_font("Times"  ,size= 12)
        pdf.cell(40,10,'' ,2 , 1)
        pdf.cell(40,10,'{}'.format(self.ttest ) , 2, 0)
        pdf.cell(40,10,'{}'.format(self.var.get()) , 2, 0)
       

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



       
        try:
            pdf.output("lab_results_walkin.pdf")
            message = "PDF Generated successfully!"
            mb.askokcancel(message = message , parent = self)
        except:
            message = "Close the open pdf!"
            mb.askokcancel(message = message , parent = self)
    def print_detailsp(self):
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Times"  ,size= 15)
        pdf.cell(200, 10 , txt = "CARELINK MEDICAL CENTRE" , ln = 1 , align = 'C')
        pdf.cell(200, 10 , txt = "AT Mzee Juma's Flats " , ln = 2 , align = 'C')
        pdf.cell(200, 10 , txt = "Waruku bypass Near Kangemi Memorial Park -  WARUKU" , ln = 3 , align = 'C')
        pdf.cell(200, 10 , txt = "P.O Box 14496-00800" , ln = 4 , align = 'C')
        pdf.cell(200, 10 , txt = "Nairobi" , ln = 5 , align = 'C')
        pdf.cell(200, 10 , txt = "Tell : 0727546794" , ln = 6 , align = 'C')

        pdf.set_font("Times"  ,'B' ,size= 15)
        # pdf.cell(200, 10 , txt = "{}".format(self.paymentssL.cget("text")) , ln = 7 , align = 'C')

        pdf.set_font("Times" , 'B' ,size= 15)
        pdf.cell(200, 10 , txt = " Date : {} ".format(datetime.date.today()) , ln = 9 , align = 'L')
        pdf.cell(200, 10 , txt = 'Patients Name : {} '.format(self.PatientsInNameL.cget("text")) , ln = 9 , align = 'L')
        
        
        
        
        pdf.set_font("Times" , 'B' ,size= 15)
        pdf.cell(40,10,'Gender : {}'.format(self.genderp),2 , 0)
        pdf.cell(40,10,'Age: {}'.format(self.agerp) , 2, 0)
        pdf.cell(40,10,'Lab No : {}'.format(self.PatientsInNamLo.cget("text")) ,2, 0)
        

      
        
        pdf.set_font("Times"  ,size= 12)
        pdf.cell(40,10,'' ,2 , 1)
        pdf.cell(40,10,'{}'.format(self.ttest ) , 2, 0)
        pdf.cell(40,10,'{}'.format(self.var.get()) , 2, 0)
       

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



       
        try:
            pdf.output("lab_results_patients.pdf")
            message = "PDF Generated successfully!"
            mb.askokcancel(message = message , parent = self)
        except:
            message = "Close the open pdf!"
            mb.askokcancel(message = message , parent = self)



    
    def create_gender(self,*args):
        color = self.gender.get()
        print("Your selection is", color)    
    
        
    def alltest(self):
        tests = []
        cur = self.mydb.cursor()
        result = cur.execute("SELECT testName FROM labtest")
        userrr = cur.fetchall() 
        cur.close()
        for use in userrr:
            tests.append(use)
        return tests

    def alltes(self):
        tests = []
        cur = self.mydb.cursor()
        result = cur.execute("SELECT testName FROM labtest")
        userrr = cur.fetchall() 
        cur.close()
        for use in userrr:
            tests.append(use)
        return tests

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
            
        
        
        
        
         

        


if __name__ == "__main__":
     app = App()
     app.mainloop()