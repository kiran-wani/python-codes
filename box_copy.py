from tkinter import *
from tkinter import ttk, filedialog,messagebox
from astropy.io import fits
import os
from glob import glob
import sys

DEFAULT_FONT_FAMILY   = ("MS", "Serif", "Serif")
MONOSPACE_FONT_FAMILY = ("Courier")
DEFAULT_FONT_SIZE     = 15
BIG_FONT_SIZE         = 18
SMALL_FONT_SIZE       =  12
CODEBOX_FONT_SIZE     =  12
TEXTBOX_FONT_SIZE     = DEFAULT_FONT_SIZE

class header_editing:
 def __init__(window,master):
     window.master=window
     window=title("A simple GUI")
     window.gemoetry('800x600')
#filename = filedialog.asksaveasfilename()
#dirname = filedialog.askdirectory()

#getting the files either using glob or user input:
#os.chdir('directry of your choice')
 file=glob("*fits")

#data, a= fits.getdata(file[11],header=True)



 #window=Tk()
 #window.title(" A sample GUI written in PYTHON")
 #window.geometry('800x600')

'''
C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file = "/home/vivek/Pictures/abc.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

 def open_file():
      a= filedialog.askopenfilename()
      b=fits.getheader(a[0])
      print(b)
'''
 def input_val():
     inputval=textBox.get("1.0","end-1c")
     print(inputval)
     file = open("new.txt","w") 
     file.write (inputval)
     print ("[Data saved]")
     file.close()
     return inputval      

 def see_header():
  b=fits.getheader(file[11],0)
  messagebox.showinfo('HEADER INFO',b)
  print(inputval)  
#b.rename_keyword('NAXIS',inputval)
  


  #os.system("ds9 %a"%a)
 #showing=Label(window,text=" You have opened the file at location:%a"%a)
 #showing.pack(side=LEFT,anchor=W,expand=N)
bd=ttk.Button(window, text='Open File',style='Fun.TButton', command=lambda:open_file())
bd.place(x=50,y=10)
#bd.pack(side=TOP, anchor=W, fill=X, expand=NO)
 def save_file():
  b= filedialog.asksaveasfilename()
  print("file saved")


 lb1=Label(window,text=" Would you like to modify the values? ")
 lb1.place(x=500,y=80)

 lb1=Label(window,text=" ##A basic GUI for Header editing procedure## ")
 lb1.place(x=200,y=20)

 see=Button(window, text='See header',command=see_header)
 see.place(x=100,y=50)


 b1=Button(window, text='Menu')
 b1.place(x=20,y=50)

 lb1=Label(window,text=" Modify Header data: ")
 lb1.place(x=10,y=100)


 lb1=Label(window,text=" Add new Header: ")
 lb1.place(x=10,y=200)


 lb1=Label(window,text=" Remove Header: ")
 lb1.place(x=10,y=300)


 lb1=Label(window,text=" Change Header name:")
 lb1.place(x=10,y=400)

 lb1=Label(window,text=" Add comment: ")
 lb1.place(x=10,y=500)



 var1 = IntVar()
 cb1=Checkbutton(window, text="Yes", variable=var1)
 cb1.place(x=600,y=100)
 var2 = IntVar()
 cb2=Checkbutton(window, text="No", variable=var2)
 cb2.place(x=660,y=100)


 def var_states():
  c=var1.get()
  if (c==1):
   textBox=Text(window,height=2,width=20)
   textBox.place(x=200,y=100)
   buttonc=Button(window,text="Enter",command=lambda:input_val())
   window.bind("<Return>", (lambda event: input_val()))
   buttonc.place(x=350,y=100)
   lb=Label(window,text="Kindly enter the modified header value")
   lb.place(x=400,y=140)
  
  
  

  else:
   elfg=Label(window,text=" You did not want to enter right?")
   elfg.place(x=400,y=140)
 
 window.bind("<Return>", (lambda event: var_states()))


 bs=Button(window, text='Save', command=lambda:save_file())
 bs.place(x=600,y=550)



 bd=Button(window, text='Quit', command=window.quit)
 bd.place(x=650,y=550)


 lb1=Label(window,text=" Written by Vivek Jha at ARIES Nainital.")
 lb1.place(x=10,y=550)
'''

#header editing functions:


# To add a new header value.
def add_header():
 	
	lb.configure(os.system("gedit ~/Documents/box.py"))    

#To modify existing header values
def modify_header():
 
    messagebox.showinfo('RESPONSE', ' Option no 2 executed here...')

# To remove a given header
def remove_header():
 
    messagebox.showinfo('RESPONSE', 'Option no 3 executed here...')

# To rename a given header

def rename_header():
 
    messagebox.showinfo('RESPONSE', 'Option no 4 executed here...')

# To add comment to given header.

def add_comment():
 
    messagebox.showinfo('RESPONSE', 'Option no 5 executed here...')


'''













root=Tk()
my_gui=header_editing(root)
root.mainloop()

