
from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Clicker game by HOUMR")
root.geometry("250x100")
root.resizable(width=FALSE, height=FALSE)

class Player: 
		def __init__(self,cookies,multiplier,multiplierprice,autoclicker,autoclickerprice):
				self.cookies = cookies
				self.multiplier = multiplier
				self.multiplierprice = multiplierprice
				self.autoclicker = autoclicker
				self.autoclickerprice = autoclickerprice
				
class Upgrades: 
	def __init__(self,x3profit): 
			self.x3profit = x3profit
				
stat = Player(0,1,10,0,100) 
upgrade = Upgrades(FALSE) 

def add_cookie(): 
		stat.cookies += 1 * stat.multiplier
		lb_cookiecounter = Label(root,text="Clicks: " + str(stat.cookies))
		lb_cookiecounter.grid(row=0,column=0)

def buy_multiplier(): 
	if (stat.cookies >= stat.multiplierprice): 
		stat.cookies -= stat.multiplierprice
		stat.multiplier += 1
		stat.multiplierprice *= 2
		lb_cookiecounter = Label(root,text="Clicks: " + str(stat.cookies))
		lb_cookiecounter.grid(row=0,column=0) 
		lb_pricemultiplier = Label(root,text="Price: "+ str(stat.multiplierprice),fg="green")
		lb_pricemultiplier.grid(row=2,column=1)
		lb_countmultiplier = Label(root, text="Count: "+ str(stat.multiplier))
		lb_countmultiplier.grid(row=2,column=2)
	else:
		messagebox.showinfo("oops!","You don't have enough Clicks to buy this!") 
	  
def buy_autoclicker():
	if (stat.cookies >= stat.autoclickerprice):
		stat.cookies -= stat.autoclickerprice
		stat.autoclicker += 1
		stat.autoclickerprice += random.randint(50,150)
		lb_cookiecounter = Label(root,text="Clicks: " + str(stat.cookies))
		lb_cookiecounter.grid(row=0,column=0)
		lb_priceautoclicker = Label(root,text="Price: "+ str(stat.autoclickerprice),fg="green")
		lb_priceautoclicker.grid(row=3,column=1)
		lb_countautoclicker = Label(root,text="Count: "+ str(stat.autoclicker))
		lb_countautoclicker.grid(row=3,column=2)
	else:
		 messagebox.showinfo("oops!","You don't have enough clicks to buy this!")    
		
def autoclick():
		stat.cookies += stat.autoclicker
		lb_cookiecounter = Label(root,text="Clicks: " + str(stat.cookies))
		lb_cookiecounter.grid(row=0,column=0)
		root.after(1000,autoclick)

lb_cookiecounter = Label(root,text="Clicks: " + str(stat.cookies)) 
bt_addcookie = Button(root,text="CLICK ME!",command=add_cookie) 
bt_buymultiplier = Button(root,text="Buy Multiplier",command=buy_multiplier) 
lb_pricemultiplier = Label(root,text="Price: "+ str(stat.multiplierprice),fg="green") 
lb_countmultiplier = Label(root,text="Count: "+ str(stat.multiplier)) 
bt_buyautoclicker = Button(root,text="Buy Autoclicker",command=buy_autoclicker) 
lb_priceautoclicker = Label(root,text="Price: "+ str(stat.autoclickerprice), fg="green") 
lb_countautoclicker = Label(root,text="Count: "+ str(stat.autoclicker)) 
lb_upgradestitle = Label(root,text="Upgrades") 

lb_cookiecounter.grid(row=0,column=0)
bt_addcookie.grid(row=1,column=0)
bt_buymultiplier.grid(row=2,column=0)
lb_pricemultiplier.grid(row=2,column=1)
lb_countmultiplier.grid(row=2,column=2)
bt_buyautoclicker.grid(row=3,column=0)
lb_priceautoclicker.grid(row=3,column=1)
lb_countautoclicker.grid(row=3,column=2)

#Add achievments




autoclick()
		
root.mainloop()

