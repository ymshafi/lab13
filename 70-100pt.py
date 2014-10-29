#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.button1 = Button(self.myContainer1)
       	    self.button1.configure(text="up", background= "green")
       	    self.button1.pack(side=LEFT)
       	    self.button1.bind("<Button-1>", self.up)
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    	
		
	def up(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
		
myapp = MyApp(root)
root.mainloop()