from tkinter import *

master = Tk()

def callback():
    print ("click!")

##f = Frame(master, height=1080, width=1920)
##f.pack_propagate(0) # don't shrink
##f.pack()
##
###b = Button(f, text="Sure!", command=callback,height=19, width=30)
##b.pack()
##backgroundImage=master.PhotoImage("L:\SmithBuffy\Computer Science\DataFilesforStudents\Games Backup\Pictures of Smith\Pic1.jpg")
w = Label(master, text="Welcome To BuffySTEAM", fg="Black")
w.pack(ipadx=80)
w.pack(pady=10)
w.pack(padx=200)
w = Button(master, text="Whack a Freshman", bg="red", fg="white")
w.pack(ipadx=80)
w.pack(pady=10)
w.pack(padx=900)
w = Button(master, text="Toast a Freshman", bg="green", fg="black")
w.pack(ipadx=80)
w.pack(pady=10)
w.pack(padx=20)
w = Button(master, text="Escape from Fort Smith", bg="blue", fg="white")
w.pack(ipadx=80)
w.pack(pady=10)
w.pack(padx=20)
w = Label(master, text="", bg="Black")
w.pack(ipady=500)
w.pack(ipadx=960)

mainloop()
