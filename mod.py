from tkinter import *
class Window(object):
 def __init__(self,master):
     self.master=master
     self.master.title("Nice one!!")
     self.master.geometry("400x400+300+200")
     self.master.config(bg="#fff")
     self.AddWidgets()

 def AddWidgets(self):
      self.TopFrame=Frame (self.master,bg="#42f498",width=400, height=100)
      self.TopFrame.grid(column=0,row=1)
      self.SayHello= Button(self.master , text= "Say Hello", width=10,height=2, bd=0, bg=" #42f498")
      self.SayHello.grid(column=0,row=2, padx=10,pady=10)
      
      
 def showHelloBox(self):
     print("hi")

window.mainloop()
