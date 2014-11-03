#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
circle = drawpad.create_oval(10,10,50,50, fill="green")
circle2 = drawpad.create_oval(50,50,200,200, fill="green")
circle3 = drawpad.create_oval(400,400,500,500, fill="green")
# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="Down", background= "green")
       	    self.down.grid(row=1,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="Right", background= "green")
       	    self.right.grid(row=0,column=2)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="Left", background= "green")
       	    self.left.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    

       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
       	    self.animate()
            self.animate1()
            self.animate2()
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global circle
            x1, y1, x2, y2 = drawpad.coords(circle)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(circle, -800, 0)
                direction = 6
        
            drawpad.move(circle,6,0)
  
            drawpad.after(1, self.animate)
	def animate1(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global circle2
            x1, y1, x2, y2 = drawpad.coords(circle2)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(circle2, -800, 0)

        
            drawpad.move(circle2,1,0)
  
            drawpad.after(1, self.animate1)
            
        def animate2(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global circle3
            x1, y1, x2, y2 = drawpad.coords(circle3)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(circle3, -800, 0)

        
            drawpad.move(circle3,2,0)
  
            drawpad.after(1, self.animate2)
        	
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,10,0)
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-10,0)	


# Kick off our animation
		
app = MyApp(root)

root.mainloop()