import tkinter as tk
import random

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.tk_value = tk.StringVar()
        self.tk_value.set("test")
        self.blink_status = 1

        self.tx_label = tk.Label(self,textvariable = self.tk_value, relief = tk.GROOVE  , width = 4 , height = 2)
        self.tx_label.grid(row = 0 , column = 4 , sticky = tk.E)
        self.blink_tx()

    def blink_tx_step_2(self, color = None):
        if color != None:
            self.tx_label["bg"] = color
        self.after(35 , self.blink_tx)
    
    def blink_tx(self):
        if self.blink_status == 1:
            self.tx_label["bg"] = 'green'
            self.tk_value.set('Tx')
            self.blink_status = random.randint(0,2)
            self.after(10, self.blink_tx_step_2, 'blue')
        elif self.blink_status == 0:
            self.tx_label["bg"] = 'red'
            self.tk_value.set('*')
            self.blink_status = random.randint(0,2)
            self.after(20, self.blink_tx_step_2, 'orange')
        else:
            self.tx_label["bg"] = 'red'
            self.tk_value.set('x')
            self.blink_status = random.randint(0,2)
            self.after(200, self.blink_tx_step_2)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()




