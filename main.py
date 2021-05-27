
import Dfa
from tkinter import filedialog
from fsmdot.nfa import Nfa
import tkinter as tk

from PIL import Image

import matplotlib.pyplot as plt

import sys
try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk
try:
	import ttk
	py3 = False
except ImportError:
	import tkinter.ttk as ttk
	py3 = True
from PIL import Image, ImageTk
import main_support
import main_automate
import AFD
import os.path
class PlaceholderEntry(ttk.Entry):
	def __init__(self, container, placeholder, *args, **kwargs):
		super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
		self.placeholder = placeholder
		self.insert("0", self.placeholder)
		self.bind("<FocusIn>", self._clear_placeholder)
		self.bind("<FocusOut>", self._add_placeholder)

	def _clear_placeholder(self, e):
		if self["style"] == "Placeholder.TEntry":
			self.delete("0", "end")
			self["style"] = "TEntry"
		
	def _add_placeholder(self, e):
		if not self.get():
			self.insert("0", self.placeholder)
			self["style"] = "Placeholder.TEntry"
   
def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	top = Toplevel1 (root)
	main_support.init(root, top)
	root.option_add('*tearOff',False)
	root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
	'''Starting point when module is imported by another module.
	   Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
	global w, w_win, root
  
	#rt = root
	root = rt
	w = tk.Toplevel (root)
	top = Toplevel1 (w)
	main_support.init(w, top, *args, **kwargs)
	return (w, top)

def destroy_Toplevel1():
	global w
	w.destroy()
	w = None

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font11 = "-family {Courier New} -size 13"
font13 = "-family {Segoe UI} -size 12 -weight bold"
font14 = "-family {Microsoft New Tai Lue} -size 15 -weight bold"
font9 = "-family {Segoe UI} -size 11 -weight bold"
font99 = "-family {Segoe UI} -size 10 -weight bold"
font10 = "-family {Segoe UI} -size 11 -weight bold"
class Toplevel1:
	def __init__(self, top=None):
		self.style = ttk.Style()
		if sys.platform == "win32":
			self.style.theme_use('winnative')
		self.style.configure('.',background=_bgcolor)
		self.style.configure('.',foreground=_fgcolor)
		self.style.configure('.',font="TkDefaultFont")
		self.style.map('.',background=
			[('selected', _compcolor), ('active',_ana2color)])
		top.geometry("848x700+50+2")
		top.minsize(120, 1)
		top.maxsize(1370, 749)
		top.resizable(0,0)
		top.title("Projet Module TLC 2021")
		top.configure(background="#d9d9d9")

		self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
		top.configure(menu = self.menubar)
		self.menu = None
		self.container1 = tk.Frame(top)
		self.container1.place(relx=0.0, rely=0.0, relheight=1.012, relwidth=1.002)
		self.container1.configure(relief='groove')
		self.container1.configure(borderwidth="2")
		self.container1.configure(relief="groove")
		self.container1.configure(background="#d7d7d7")
		
		
		self.addEmpFrame = None
		self.HeaderFrame1 = None
		self.LoginFrame2 = None
		self.mainFrame = None
		self.displayAtt= None
  
		self.src_file =None
		self.addEmploye = None
		self.imageAdded =False
		self.removeEmployee = None
		self.headerView()
		self.loginFormView(top)
		
	def headerView(self):
		self.HeaderFrame1 = tk.Frame(self.container1)
		self.HeaderFrame1.place(relx=0.012, rely=0.016, relheight=0.237, relwidth=0.973)
		self.HeaderFrame1.configure(relief='groove')
		self.HeaderFrame1.configure(borderwidth="2")
		self.HeaderFrame1.configure(relief="groove")
		self.HeaderFrame1.configure(background="#cbe4e4")

		self.Label1 = tk.Label(self.HeaderFrame1)
		self.Label1.place(relx=0.29, rely=0.105, height=130, width=522)
		self.Label1.configure(activeforeground="#0482ff")
		self.Label1.configure(background="#ffffff")
		self.Label1.configure(borderwidth="1")
		self.Label1.configure(disabledforeground="#a3a3a3")
		self.Label1.configure(font=font14)
		self.Label1.configure(foreground="#0076ec")
		self.Label1.configure(text='''Projet Module TLC \n élaboré par :\n Hamdi Hassen & Mohamed Saidi''')

		self.TLabel3 = ttk.Label(self.HeaderFrame1)
		self.TLabel3.place(relx=0.056, rely=0.105, height=130, width=125)
		self.TLabel3.configure(background="#FFFFFF")
		self.TLabel3.configure(foreground="#000000")
		self.TLabel3.configure(font="TkDefaultFont")
		self.TLabel3.configure(relief="flat")
		self.TLabel3.configure(anchor='w')
		self.TLabel3.configure(justify='left')
		self.TLabel3.configure(text='''Tlabel''')
		photo_location = os.path.join("static/img","img.png")
		global _img0
		_img0 = ImageTk.PhotoImage(file=photo_location)
		self.TLabel3.configure(image=_img0)
	def loginFormView(self,top):
		def determiniserAutomate():
			S = self.alphabets.get().split(',')
			S.append(Nfa.EPSILON)
			Q = self.etats.get().split(',')
			transitions = self.transitions.get()
			q0 = self.etatInitail.get()
			F = self.etatsFinaux.get().split(',')
			dict= {}
			transitions = transitions.replace('$',Nfa.EPSILON)
			l = []
			d= {}
			for tr in transitions.split(' '):
				list = tr.split(',')
				if tr.split(',')[0] not in l:
					l.append(tr.split(',')[0])
					d[tr.split(',')[0]]={}
				# validate list items
				arrow = str(list[0])+","+str(list[1])
				if arrow not in dict:
					dict[arrow]= [list[2]]
				else :
					dict[arrow].append(list[2])
			for i in dict : 
				x = i.split(',')[0]
				y = i.split(',')[1]
				d[x][y] = dict[i]
			print(d)
			res = Dfa.Display(Q, S, d, q0, F)	
			print("message",res)
			if  res :			
				tk.messagebox.showinfo("Info","Cet automate est déjà déterministe")
			else:
				Dfa.Determiniser(Q, S, d, q0, F)
				im = Image.open("NfatoDfa.dot.png")
				im.show()				
				#determiniser automate 
				# aficher nfatodaf	

		def validate():
			# validate inputs
			return True
		def displayAutomate():
			# try :
			S = self.alphabets.get().split(',')
			S.append(Nfa.EPSILON)
			Q = self.etats.get().split(',')
			transitions = self.transitions.get()
			q0 = self.etatInitail.get()
			F = self.etatsFinaux.get().split(',')
			dict= {}
			transitions = transitions.replace('$',Nfa.EPSILON)
			l = []
			d= {}
			for tr in transitions.split(' '):
				list = tr.split(',')
				if tr.split(',')[0] not in l:
					l.append(tr.split(',')[0])
					d[tr.split(',')[0]]={}
				# validate list items
				arrow = str(list[0])+","+str(list[1])
				if arrow not in dict:
					dict[arrow]= [list[2]]
				else :
					dict[arrow].append(list[2])
			for i in dict : 
				x = i.split(',')[0]
				y = i.split(',')[1]
				d[x][y] = dict[i]
			print(d)
			res = Dfa.Display(Q, S, d, q0, F)
			if res == True:
				im = Image.open("dfa.dot.png")
			else :
				im = Image.open("nfa.dot.png")
			print("Graph created !")
			im.show()
			

			# except:
				# tk.messagebox.showwarning("warning","Veuillez introduire des valeurs correctes !")
				
		def testString():
			msg = self.InputString.get()
			S = self.alphabets.get().split(',')
			S.append(Nfa.EPSILON)
			Q = self.etats.get().split(',')
			transitions = self.transitions.get()
			q0 = self.etatInitail.get()
			F = self.etatsFinaux.get().split(',')
			dict= {}
			transitions = transitions.replace('$',Nfa.EPSILON)
			l = []
			d= {}
			for tr in transitions.split(' '):
				list = tr.split(',')
				if tr.split(',')[0] not in l:
					l.append(tr.split(',')[0])
					d[tr.split(',')[0]]={}
				# validate list items
				arrow = str(list[0])+","+str(list[1])
				if arrow not in dict:
					dict[arrow]= [list[2]]
				else :
					dict[arrow].append(list[2])
			for i in dict : 
				x = i.split(',')[0]
				y = i.split(',')[1]
				d[x][y] = dict[i]
			print(d)
			val = Dfa.Accepte(Q, S, d, q0, F,msg)	
			tk.messagebox.showinfo("resultat",f"Resultat: {val}")


				
		self.LoginFrame2 = tk.Frame(self.container1)
		self.LoginFrame2.place(relx=0.012, rely=0.276, relheight=0.696, relwidth=0.973)
		self.LoginFrame2.configure(relief='groove')
		self.LoginFrame2.configure(borderwidth="1")
		self.LoginFrame2.configure(relief="groove")
		self.LoginFrame2.configure(background="#cbe4e4")
		self.LoginFrame2.configure(highlightbackground="#dddddd")

		self.TLabel1 = ttk.Label(self.LoginFrame2)
		self.TLabel1.place(relx=0.08, rely=0.010, height=68, width=66)
		self.TLabel1.configure(background="#cbe4e4")
		self.TLabel1.configure(foreground="#000000")
		self.TLabel1.configure(font="TkDefaultFont")
		self.TLabel1.configure(relief="flat")
		self.TLabel1.configure(anchor='w')
		self.TLabel1.configure(justify='left')
		self.TLabel1.configure(text='''Tlabel''')
		
		photo_location1 = os.path.join("static/img","sigma.png")
		global _img1
		_img1 = ImageTk.PhotoImage(file=photo_location1)
		self.TLabel1.configure(image=_img1)

		

		self.alphabets = PlaceholderEntry(self.LoginFrame2," L'alphabet: example -> a,b,c")
		self.alphabets.place(relx=0.178, rely=0.05,height=30, relwidth=0.7)
		self.alphabets.configure(background="white")
		# self.alphabets.configure(disabledforeground="#a3a3a3")
		self.alphabets.configure(font=font11)
		self.alphabets.configure(foreground="#000000")
		# self.alphabets.configure(insertbackground="black")
		self.alphabets.configure(justify='left')

		self.etats = PlaceholderEntry(self.LoginFrame2," Les etats: example -> q0,q1,q2")
		self.etats.place(relx=0.178, rely=0.15,height=30, relwidth=0.7)
		self.etats.configure(background="white")
		# seletatsts.configure(disabledforeground="#a3a3a3")
		self.etats.configure(font=font11)
		self.etats.configure(foreground="#000000")
		# seletatsts.configure(insertbackground="black")
		self.etats.configure(justify='left')
		
		self.transitions = PlaceholderEntry(self.LoginFrame2," Transitions: exemple -> q0-a-q1 q1-b-q3")
		self.transitions.place(relx=0.178, rely=0.250,height=30, relwidth=0.7)
		self.transitions.configure(background="white")
		# self.transitions.configure(disabledforeground="#a3a3a3")
		self.transitions.configure(font=font11)
		self.transitions.configure(foreground="#000000")
		# self.transitions.configure(insertbackground="black")
		self.transitions.configure(justify='left')
		
		self.etatInitail = PlaceholderEntry(self.LoginFrame2," Etat Initial: ... ")
		self.etatInitail.place(relx=0.178, rely=0.350,height=30, relwidth=0.7)
		self.etatInitail.configure(background="white")
		# seletatInitailns.configure(disabledforeground="#a3a3a3")
		self.etatInitail.configure(font=font11)
		self.etatInitail.configure(foreground="#000000")
		# seletatInitailns.configure(insertbackground="black")
		self.etatInitail.configure(justify='left')

		self.etatsFinaux = PlaceholderEntry(self.LoginFrame2," etats Finaux: ...  ")
		self.etatsFinaux.place(relx=0.178, rely=0.450,height=30, relwidth=0.7)
		self.etatsFinaux.configure(background="white")
		self.etatsFinaux.configure(font=font11)
		self.etatsFinaux.configure(foreground="#000000")
		self.etatsFinaux.configure(justify='left')
		
		self.Button = tk.Button(self.LoginFrame2,command=displayAutomate)
		self.Button.place(relx=0.178, rely=0.550, height=36, width=180)
	
		self.Button.configure(activebackground="#f3c843")
		self.Button.configure(activeforeground="#000000")
		self.Button.configure(background="#f3c843")
		self.Button.configure(disabledforeground="#a3a3a3")
		self.Button.configure(font=font13)
		self.Button.configure(foreground="#000000")
		self.Button.configure(highlightbackground="#d9d9d9")
		self.Button.configure(highlightcolor="black")
		self.Button.configure(pady="0")
		self.Button.configure(cursor="hand2")
		self.Button.configure(text='''Afficher l'automate''')

		self.ButtonAFD = tk.Button(self.LoginFrame2,command=determiniserAutomate)
		self.ButtonAFD.place(relx=0.42, rely=0.550, height=36, width=220)

		self.ButtonAFD.configure(activebackground="#f3c843")
		self.ButtonAFD.configure(activeforeground="#000000")
		self.ButtonAFD.configure(background="#f3c843")
		self.ButtonAFD.configure(disabledforeground="#a3a3a3")
		self.ButtonAFD.configure(font=font13)
		self.ButtonAFD.configure(foreground="#000000")
		self.ButtonAFD.configure(highlightbackground="#d9d9d9")
		self.ButtonAFD.configure(highlightcolor="black")
		self.ButtonAFD.configure(pady="0")
		self.ButtonAFD.configure(cursor="hand2")
		self.ButtonAFD.configure(text='''Determiniser l'Automate''')



		# Test de chaine:
		self.TestStrinFrame = tk.Frame(self.LoginFrame2)
		self.TestStrinFrame.place(relx=0.178, rely=0.668, relheight=0.32, relwidth=0.7)
		self.TestStrinFrame.configure(relief='groove')
		self.TestStrinFrame.configure(borderwidth="1")
		self.TestStrinFrame.configure(relief="groove")
		self.TestStrinFrame.configure(background="#ebeae4")
		self.TestStrinFrame.configure(highlightbackground="#dddddd")

		# Input String
		self.InputString = PlaceholderEntry(self.TestStrinFrame," Chaine à tester : ... ")
		self.InputString.place(relx=0.05, rely=0.09,height=30, relwidth=0.7)
		self.InputString.configure(background="white")
		# selInputStringns.configure(disabledforeground="#a3a3a3")
		self.InputString.configure(font=font11)
		self.InputString.configure(foreground="#000000")
		# selInputStringns.configure(insertbackground="black")
		self.InputString.configure(justify='left')

		


		self.Button1 = tk.Button(self.TestStrinFrame,command=testString)
		self.Button1.place(relx=0.8, rely=0.075, height=30, width=70)
		
		self.Button1.configure(activebackground="#f3c843")
		self.Button1.configure(activeforeground="#000000")
		self.Button1.configure(background="#f3c843")
		self.Button1.configure(disabledforeground="#a3a3a3")
		self.Button1.configure(font=font13)
		self.Button1.configure(foreground="#000000")
		self.Button1.configure(highlightbackground="#d9d9d9")
		self.Button1.configure(highlightcolor="black")
		self.Button1.configure(pady="0")
		self.Button1.configure(cursor="hand2")
		self.Button1.configure(text='''OK''')

if __name__ == '__main__':
	vp_start_gui()





