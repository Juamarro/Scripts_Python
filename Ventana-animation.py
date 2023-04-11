import ttkbootstrap as tb
from random import choice

class SlidePanel(tb.Frame):
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent,bootstyle="info")

		# general attributes 
		self.start_pos = start_pos - 0.05
		self.end_pos = end_pos - 0.03
		self.width = abs(start_pos - end_pos)

		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# layout
		self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.9)

	def animate(self):
		if self.in_start_pos:
			self.animate_forward()
		else:
			self.animate_backwards()

	def animate_forward(self):
		if self.pos < self.end_pos:
			self.pos += 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos > self.start_pos:
			self.pos -= 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True

# window 
window = tb.Window()
window.title('Animated Widgets')
window.geometry('600x400')

# animated widget
animated_panel = SlidePanel(window, -0.25, 0.05)
tb.Label(animated_panel, text = 'Label 1',bootstyle="inverse-info").pack(expand = True, fill = 'both', padx = 2, pady = 10)
tb.Label(animated_panel, text = 'Label 2',bootstyle="inverse-info").pack(expand = True, fill = 'both', padx = 2, pady = 10)
tb.Button(animated_panel, text = 'Button', bootstyle="info").pack(expand = True, fill = 'both', pady = 10)

# button
button_x = 0.5
button = tb.Button(window, text = 'toggle sidebar', command = animated_panel.animate)
button.place(relx = button_x, rely = 0.5, anchor = 'center')

# run
window.mainloop()