import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox, Menu




class fits_header(tk.Tk):
 window=tk.Tk()
 window.title(" To add/edit/append the header to a fits file.")
 window.geometry('1024x768')




 def op10():
  messagebox.showinfo('RESPONSE', 'Option no 10 executed here...')

 def response():
  tk.configure(text='Thanks for your review!')
  chk.grid(column=1, row=5)

def init_gui(self):

	tk.Label(window,text="This is a simple GUI for fits headers       ",font=("Sans ",15))

	tk.Button(window, text="The list of files present here.",command=op10).pack(anchor=tk.side,side=tk.BOTTOM)
 
	chk_state = BooleanVar()
#chk_state.set(False) #set check state

	tk.Label(window,text=" Add a header keyword==>",font=("Sans ",15))

	chk = Checkbutton(window, text=' Yes', var=chk_state,command=response) 
	
	chk = Checkbutton(window, text='No', var=chk_state,command=response) 
	
	tk.Entry(window,width=10)
	
	tk.Button(window, text="save",command=op11)
	tk.Button(window, text="clear",command=op10)

	chk_state = BooleanVar()
	chk_state.set(False) #set check state



hedit=fits_header()
hedit.mainloop()
