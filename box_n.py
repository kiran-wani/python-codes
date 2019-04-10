from tkinter import *
from tkinter import ttk,filedialog,messagebox
from tkinter.filedialog import askopenfilename
from astropy.io import fits
import os,sys
from glob import glob


class header_edit:
    DEFAULT_FONT_FAMILY   = ("MS", "Serif", "Serif")
    MONOSPACE_FONT_FAMILY = ("Sans")
    DEFAULT_FONT_SIZE     = 16
    BIG_FONT_SIZE         = 20
    SMALL_FONT_SIZE       =  14
    CODEBOX_FONT_SIZE     =  14
    TEXTBOX_FONT_SIZE     = DEFAULT_FONT_SIZE

    def __init__(self,master):
        self.fil=glob("*fits")
        master.geometry("800x600")
        
# THE COMPONENTS THAT WILL BE THERE ON THE SCREEN:
        
        #TEXT:
        
        self.lb1=Label(master,text=" ##A basic GUI for Header editing procedure## ")
        self.lb1.place(x=200,y=20)
        
        self.lb1=Label(master,text=" ##PLEASE CHOOSE THE VALUES FOR THE GIVEN KEYWORDS## ")
        self.lb1.place(x=200,y=100)
        
        self.lbl=Label(master,text="KEYWORDS")
        self.lbl.place(x=30, y=120)
        
        self.lb1=Label(master,text=" FILTER1: ")
        self.lb1.place(x=25,y=150)


        self.lb1=Label(master,text="FILTER2: ")
        self.lb1.place(x=30,y=200)


        self.lb1=Label(master,text="GRISM:")
        self.lb1.place(x=30,y=250)


        self.lb1=Label(master,text="SLIT:")
        self.lb1.place(x=30,y=300)

        self.lb1=Label(master,text=" USER: ")
        self.lb1.place(x=25,y=350)
        
        self.lbl=Label(master,text="COMMENTS:")
        self.lbl.place(x=30, y=400)
        
       
        
        
        # BUTTONS
        
        self.b1=Button(master, text='Load file',command=self.load_file)
        self.b1.place(x=150,y=50)
        
        self.b2=Button(master, text='Batch load',command=self.see_header)
        self.b2.place(x=250,y=50)
        
        
        self.b3=Button(master, text='See header',command=self.see_header)
        self.b3.place(x=550,y=150)
        
        self.btn = Button(master, text="Save",command=self.saving)
        self.btn.place(x=200,y=500)
        
        self.btn = Button(master, text="Undo",command=self.remove)
        self.btn.place(x=280,y=500)
        
        self.btn = Button(master, text="Quit",command=master.quit)
        self.btn.place(x=340,y=500)
        
        self.textbox1()
        #self.bind("<Return>", (lambda event: self.input_val()))
        self.textbox2()
        
 # DROP DOWN MENU       
        
        self.f1 = ttk.Combobox()
        self.f1['values']= ("--SELECT-","u", "g", "v","i", "z")
        self.f1.current(0) #set the selected item
        self.f1.place(x=200,y=150)
        
        self.f2 = ttk.Combobox()
        self.f2['values']= ("--SELECT-","HA1", "HA2", "HB1","HB2")
        self.f2.current(0) #set the selected item
        self.f2.place(x=200,y=200)
        
        self.g1 = ttk.Combobox()
        self.g1['values']= ("--SELECT-","770R", "676R", "132R")
        self.g1.current(0) #set the selected item
        self.g1.place(x=200,y=250)
        
        slit = ttk.Combobox()
        slit['values']= ("--SELECT-", "0.4", "0.8","1.2", "1.6")
        slit.current(0) #set the selected item
        slit.place(x=200,y=300)
        self.slit=slit
        
        
# The processing part here all the processing for above events will take place.    
    def textbox1(self):
        self.textBox=Text(height=2,width=20)
        self.textBox.place(x=200,y=350)
        self.buttonc=Button(text="Enter",command=lambda:self.input_val1())
        self.buttonc.place(x=350,y=350)
        #print(self.inputval1)
  
    def textbox2(self):
        self.textBox=Text(height=5,width=40)
        self.textBox.place(x=150,y=400)
        self.buttonc=Button(text="Enter",command=lambda:self.input_val2())
        self.buttonc.place(x=450,y=400)
  
  
  
    def check_val(self):
        T = Text(root, height=30, width=30)
        T.place(x=550,y=250)
        T.insert(END,self.f1.get(),"    ",self.f2.get(),"   ",self.g1.get(),"  ",self.slit.get())
        T.insert(self.inputval2)
        #print("the entered value==>",self.f1.get(),self.f2.get(),self.g1.get(),self.slit.get())
       # print("user==>",b)
        #print("comment==>",c)
        
    def input_val1(self):
        self.inputval1=self.textBox.get("1.0","end-1c")
        print(self.inputval1)
        
        
    def input_val2(self):
        self.inputval2=self.textBox.get("1.0","end-1c")
        print(self.inputval2)
        
    def saving(self):
        self.data,self.b=fits.getdata(self.fname,header=True)
        self.b.insert('NAXIS1',("FILTER1",self.f1.get()))
        self.b.insert('NAXIS1',("FILTER2",self.f2.get()))
        self.b.insert('NAXIS1',("GRISM",self.g1.get()))
        self.b.insert('NAXIS1',("SLIT",self.slit.get()))
        fits.writeto(self.fname,self.data,self.b,overwrite=True)
        print('header saved!!!!')
      
    def remove(self):
        self.b.remove("FILTER1")
        self.b.remove("FILTER2")
        self.b.remove("GRISM")
        self.b.remove("SLIT")
        fits.writeto(self.fname,self.data,self.b,overwrite=True)
        print('header deleted!!')
    
    def see_header(self):
         messagebox.showinfo('HEADER INFO',self.b)
         
    def load_file(self):
        self.fname = askopenfilename(filetypes=(("FITS files", "*fits"),
                                           ("All files", "*.*") ))
        
    def extra_header(self):
        self.b.insert('NAXIS1',("TELESCOPE","3.6m ARIES DOT"))
        self.b.insert('NAXIS1',("INSTRUMENT","ADFOSC"))
        fits.writeto(self.fname,self.data,self.b,overwrite=True) 


root=Tk()
  


C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "/home/vivek/Pictures/abc.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

all=header_edit(root)  
root.title("GUI for FITS headers")
root.pack_propagate(0)
root.mainloop()

 
