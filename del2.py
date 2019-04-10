import tkinter as tk

class IngredientAdder(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("500x500+0+0")
        self.init_gui()

    # function to add new ingredients
    def add_ingredient_entry(self):
        entry = tk.Entry(self)
        entry.pack(side=tk.TOP)
        self.ingredient_entries.append(entry)

    # get contents of all entry boxes
    def save_recipe(self):
      file = open("new.txt","w") 
      for ingredient in self.ingredient_entries:
         file.write (ingredient.get() + "\n")
      print ("[Data saved]")
      file.close()
    # build initial widgets 
    def init_gui(self):

        # this is a list of ingredients entry boxes
        self.ingredient_entries = []

        # put a label at the top of the window and anchor it there
        tk.Label(self,text="Input parameters").pack(anchor=tk.N,side=tk.TOP)

        # Put these two buttons at the bottom of the window and anchor them there
        tk.Button(self,text="Save data",command=self.save_recipe).pack(anchor=tk.S,side=tk.BOTTOM)
        tk.Button(self,text="Add more data",command=self.add_ingredient_entry).pack(anchor=tk.S,side=tk.BOTTOM)

        # new ingredients will be added between the label and the buttons 
        self.add_ingredient_entry()

cookbook = IngredientAdder()
cookbook.mainloop()
