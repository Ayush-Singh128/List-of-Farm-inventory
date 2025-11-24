import tkinter as tk
from tkinter import messagebox
import json
import os

class FarmTracker:
    def __init__(self, window):
        self.window = window
        self.window.title("Farm Inventory")
        self.window.geometry("700x500")
        
        self.storagefile = "farmitems.json"
        self.allitems = []
        self.getsaveditems()
        
        self.setupinterface()
        self.displayitems()
    
    def setupinterface(self):
        # Item details section
        tk.Label(self.window, text=" Item ").place(x=20, y=20)
        self.itemname = tk.Entry(self.window, width=20)
        self.itemname.place(x=150, y=20)
        
        tk.Label(self.window, text=" Quantity ").place(x=20, y=50)
        self.itemcount = tk.Entry(self.window, width=10)
        self.itemcount.place(x=150, y=50)
        
        tk.Label(self.window, text=" Type").place(x=20, y=80)
        self.itemtype = tk.StringVar(value="Tools")
        categories = ["Tools", "Seeds", "Fertilizers"]
        self.typeselector = tk.OptionMenu(self.window, self.itemtype, *categories)
        self.typeselector.place(x=150, y=75)
        
        # Action buttons
        tk.Button(self.window, text="Add ", command=self.savenewitem, width=12, bg="orange").place(x=20, y=120)
        tk.Button(self.window, text="Remove", command=self.removeitem, width=12, bg="yellow").place(x=140, y=120)
       # Your items list
        self.itemsdisplay = tk.Listbox(self.window, width=60, height=12)
        self.itemsdisplay.place(x=20, y=190)
    
    def savenewitem(self):
        name = self.itemname.get().strip()
        count = self.itemcount.get().strip()
        newitemid = len(self.allitems) + 1
        newitem = {
            "id": newitemid,
            "name": name,
            "count": count,
            "category": self.itemtype.get()
        }
        self.allitems.append(newitem)
        self.savetofile()
        self.displayitems()
        self.resetform()
        messagebox.showinfo("Done", f" {name} Added")
    
    def removeitem(self):
        try:
            selectedindex = self.itemsdisplay.curselection()[0]
            itemtoremove = self.itemsdisplay.get(selectedindex).split(" - ")[1]
            
            if messagebox.askyesno("DELETION", f"Removing {itemtoremove} "):
                del self.allitems[selectedindex]
                self.savetofile()
                self.displayitems()
                self.resetform()
        except:
            messagebox.showerror("Error", "Kindly select the item to be removed")
    
   
    def displayitems(self):
        self.itemsdisplay.delete(0, tk.END)
        for item in self.allitems:
            displaytext = f"{item['id']} - {item['name']} - {item['count']} - {item['category']}"
            self.itemsdisplay.insert(tk.END, displaytext)
    
    def resetform(self):
        self.itemname.delete(0, tk.END)
        self.itemname.delete(0, tk. END)
    def getsaveditems(self):
        if os.path.exists(self.storagefile):
            try:
                with open(self.storagefile, 'r') as file:
                    self.allitems = json.load(file)
            except:
                self.allitems = []
    
    def savetofile(self):
        with open(self.storagefile, 'w') as file:
            json.dump(self.allitems, file)

# Start the application
if __name__ == "__main__":
    mainwindow = tk.Tk()
    farmapp = FarmTracker(mainwindow)
    mainwindow.mainloop()