from tkinter import *
from tkcalendar import *





root = Tk()
root.geometry("1350x750+0+0")


cal = Calendar(root ,  selectmode = "day" , year = 2020 ,  month = 5 , day = 22)
cal.pack(pady = 20)

def grab_date():
    my_label.config(text  = cal.get_date())

my_Button = Button(root, text = " Get Date" , command = grab_date)
my_Button.pack(pady = 20)

my_label = Label(root , text = " ")
my_label.pack(pady = 20)





root.mainloop()
