"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PROGRAM TO MAKE A GUI REGISTRATION PAGE USING TKINTER PYTHON INTERFACING WITH SQLITE3 DATABASE
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from tkinter import *
from PIL import Image,ImageTk
import time
import sqlite3
import DB

# global pasw, User, var, var1, var2

# def Display():
# 	self.top = Tk()
# 	self.top.geometry('800x480')
# 	self.top.title('Display')

# 	self.top.mainloop()

class Framewrk():


	def __init__(self):
		self.Register()


	def Register(self):
		self.top = Tk()
		self.top.geometry('800x480')
		self.top.configure(bg='skyblue3')
		self.top.title('Registration')
		
		self.fstName = StringVar()
		self.lstName = StringVar()
		self.gmail = StringVar()
		self.usrName = StringVar()
		self.pswrd = StringVar()

		img1 = PhotoImage(file='Bluesky_2.png')
		Label(self.top, image=img1).place(relx=0, rely=0, relwidth=1, relheight=1)

		Label(self.top, text='First Name:', bg='white', fg='black', font=('Calibre',15), width=12).place(relx=0.31, rely=0.05)
		fst_ent = Entry(self.top, textvariable=self.fstName, font=('Calibre',15)).place(relx=0.5, rely=0.05)
		Label(self.top, text='Last Name:', bg='white', fg='black', font=('Calibre',15), width=12).place(relx=0.31, rely=0.25)
		lst_ent = Entry(self.top, textvariable=self.lstName, font=('Calibre',15)).place(relx=0.5, rely=0.25)
		Label(self.top, text='Gmail:', bg='white', fg='black', font=('Calibre',15), width=12).place(relx=0.31, rely=0.45)
		mail_ent = Entry(self.top, textvariable=self.gmail, font=('Calibre',15)).place(relx=0.5, rely=0.45)
		Label(self.top, text='Username:', bg='white', fg='black', font=('Calibre',15), width=12).place(relx=0.31, rely=0.65)
		usr_ent = Entry(self.top, textvariable=self.usrName, font=('Calibre',15)).place(relx=0.5, rely=0.65)
		Label(self.top, text='Password:', bg='white', fg='black', font=('Calibre',15), width=12).place(relx=0.31, rely=0.85)
		pswrd_ent = Entry(self.top, textvariable=self.pswrd, show='*', font=('Calibre',15)).place(relx=0.5, rely=0.85)

		# if self.var==0 and self.var1==0 and self.var2 == 0:
		# 	Label(self.top, text='All the details are Mandatory', bg='white', fg='black').place(relx=0.35, rely=0.05) 
		# else:
		submit = Button(self.top, text='> > >', bg='Red', fg='black', activebackground='green', font=('Calibre', 15), width=4, command=self.logIn).place(relx=0.935, rely=0.28, relheight=0.4)
		# clk = Label(self.top, text=time.strftime('%H : %M : %S  %p'), font=('Calibre', 10), bg='black', fg='white').place(relx=0.875, rely=0.96)


		self.top.mainloop()

	def logIn(self):

		DB.insert(self.fstName.get(), self.lstName.get(), self.gmail.get(), self.usrName.get(), self.pswrd.get())
		print(DB.view())

		self.top.destroy()
		self.top = Tk()
		self.top.geometry('800x480')
		self.top.configure(bg='sky blue')
		self.top.title('Log In')

		img = PhotoImage(file='Bluesky_1.png')
		Label(self.top, image=img).place(relx=0, rely=0, relwidth=1, relheight=1)

		# self.User = ('bhaskar246')
		# self.pasw = ('123')

		self.var = StringVar()
		self.var1 = StringVar()
		self.var2 = StringVar()

		name = Label(self.top, text='UserName:', bg='white', fg='black', font=('Calibre', 15)).place(relx=0.25, rely=0.15)
		name_ent = Entry(self.top, textvariable=self.var, bg='white', fg='black', font=('Calibre', 15)).place(relx=0.5, rely=0.15)
		psw = Label(self.top, text='Password:', bg='white', fg='black', font=('Calibre', 15)).place(relx=0.25, rely=0.3)
		psw_ent = Entry(self.top, textvariable=self.var1, show='*', bg='white', fg='black', font=('Calibre', 15)).place(relx=0.5, rely=0.3)
		repsw = Label(self.top, text='Re-enter Password:', bg='white', fg='black', font=('Calibre', 15)).place(relx=0.25, rely=0.45)
		repsw_ent = Entry(self.top, textvariable=self.var2, show='*', bg='white', fg='black', font=('Calibre', 15)).place(relx=0.5, rely=0.45)


		# clk = Label(self.top, text=time.strftime('%H : %M : %S  %p'), font=('Calibre', 10), bg='black', fg='white').place(relx=0.875, rely=0.96)
		# self.clk.after(1000, self.logIn)

		# Button(self.top, text='Submit', bg='Red', fg='black', font=('Calibre', 15), command=Display).place(relx=0.35, rely=0.75)
		submit = Button(self.top, text='> > >', bg='Red', fg='black', activebackground='green', font=('Calibre', 15), width=22, command=self.try_login).place(relx=0.37, rely=0.6)
		

		self.top.mainloop()


	# def clock(self):
	# 	string = time.strftime('%H : %M : %S  %p')
	# 	clk.config(text=string)
	# 	clk.after(1000, clock)

	def try_login(self):
		
		if self.usrName.get() == self.var.get() and self.pswrd.get() == self.var1.get() and self.pswrd.get() == self.var2.get():
			self.nxtPage()
		else:
			Label(self.top, text=' Wrong Password.. !!!', bg='white', fg='Red', font=('Calibre',15)).place(relx=0.35, rely=0.05)


	def nxtPage(self):
		self.top.destroy()
		self.top = Tk()
		self.top.geometry('800x480')
		self.top.configure(bg='cyan')
		self.top.title('Next Page')



		Button(self.top, text='Next Page', bg='red', fg='black', font=('Calibre',15), width=22, command=self.nxtPage1).place(relx=0.4, rely=0.6)

		self.top.mainloop()

	def nxtPage1(self):
		self.top.destroy()
		self.top = Tk()
		self.top.geometry('800x480')
		self.top.configure(bg='skyblue1')
		self.top.title('Next Page 1')

		

		Button(self.top, text='Prev Page', bg='red', fg='black', font=('Calibre',15), width=22, command=self.nxtPage).place(relx=0.4, rely=0.6)
		Button(self.top, text='QUIT', bg='red', fg='black', font=('Calibre',15), width=22, command=self.top.destroy).place(relx=0.4, rely=0.7)


		self.top.mainloop()




a=Framewrk()