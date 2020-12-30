import tkinter as tk


class ListFrame(tk.Frame):
    def __init__(self, master, items=[]):
        super().__init__(master)
        self.list = tk.Listbox(self)
        self.scroll = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.list.yview)
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.insert(0, *items)
        self.list.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        
    def pop_selection(self):
        index = self.list.curselection()
        if index:
            value = self.list.get(index)
            self.list.delete(index)
            return value
    def insert_item(self, item):
        self.list.insert(tk.END, item)
    
    def get_index_list(self):
        index = self.list.curselection()
        return self.list.get(index)
        