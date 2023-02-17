from tkinter import *
class App(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.label1 = Label(window, text ="Team 1", borderwidth=3,relief="solid")
        self.label1.grid(row=0, column= 0,ipadx =60 , ipady=5)
        self.label2 = Label(window, text ="Team 2",borderwidth=3,relief="solid")
        self.label2.grid(row=0, column= 1,ipadx =60 , ipady=5)
        self.label3 = Label(window, text ="Score")
        self.label3.grid(row=1, column= 0)
        self.label4 = Label(window, text ="Score")
        self.label4.grid(row=1, column= 1)
        self.label5 = Label(window, text ="  X  X ")
        self.label5.grid(row=2, column= 0)
        self.label6 = Label(window, text ="  X  X ")
        self.label6.grid(row=2, column= 1)
        self.label7 = Label(window, text ="Cups Left  X")
        self.label7.grid(row=3, column= 0)
        self.label8 = Label(window, text ="Cups Left  X")
        self.label8.grid(row=3, column= 1)



window = Tk()
window.title("Auto Pong")
g = App(window)
#window.config(bg='white')
window.mainloop()
#testing