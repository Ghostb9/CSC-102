from tkinter import *

def clickExitButton(self):
    exit()
class App(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.label1 = Label(window, text ="Team 1", borderwidth=3,relief="solid")
        self.label1.grid(row=0, column= 0,ipadx =60 , ipady=5)
        self.label5 = Label(window, text ="Cups Left  ")
        self.label5.grid(row=2, column= 0)
        self.label7 = Button(self, text = "Rerack",commmand=self.clickExitButton)
        self.label7.grid(row=3, column= 0)
    def clickExitButton(self):
        exit()

window = Tk()
window.title("Auto Pong")
g = App(window)
#window.config(bg='white')
window.mainloop()
#testing