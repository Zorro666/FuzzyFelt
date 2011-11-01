#!/usr/bin/python

from Tkinter import *

def roundRect(canvas, x0, y0, w, h, radius, penw, colour, string):
	x3 = x0 + w
	y3 = y0 + h
	radiusPixels = canvas.winfo_pixels(radius)
 	diameterPixels = 2 * radiusPixels

 	# Make sure that the radius of the curve is less than 3/4
	# size of the box!

 	maxr = 0.75

	if diameterPixels > maxr*w:
 		diameterPixels = maxr*w
	if diameterPixels > maxr*h:
		diameterPixels = maxr*h

	x1 = x0 + diameterPixels
 	x2 = x3 - diameterPixels
	y1 = y0 + diameterPixels
	y2 = y3 - diameterPixels

	canvas.create_polygon(x0, y0, x1, y0, x2, y0, x3, y0, 
												x3, y1, x3, y2, x3, y3, x2, y3,
												x1, y3, x0, y3, x0, y2, x0, y1,
												outline='black', width=penw,
												smooth=1,
												fill=colour)

	textx0 = x0+w/2
	texty0 = y0+h/2
	textw = w*0.9
	textfont=("Times", "24", "bold italic")
	canvas.create_text(textx0, texty0, text=string, justify=CENTER, width=textw, font=textfont)

class FuzzyFelt(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		m_canvas = self.createCanvas()
#		m_canvas.create_rectangle(20, 20, 350, 350, width=5, fill='red')
		roundRect(m_canvas, 50, 50, 200, 100, 50, 5, 'blue', 'AB: get the work down')
		roundRect(m_canvas, 50, 50+100, 200, 100, 50, 5, 'green', 'AB: before it is too late')
		master.update()
		m_canvas.postscript(file="test.ps", colormode='color')

	def createCanvas(self):
		canvas = Canvas(width=400, height=400, bg='white')
		canvas.pack(expand=YES, fill=BOTH)                
		return canvas

root = Tk()
app = FuzzyFelt(master=root)
app.mainloop()
