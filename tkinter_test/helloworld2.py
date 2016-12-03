import tkinter

#root widget. Create first. One per program
root_widget = tkinter.Tk()

#Label widget. displays text or image
label_widget = tkinter.Label(root_widget, text = 'Hello World!')

#size to fit, become visible (queues up for when loop is activated)
label_widget.pack()

#main tkinter loop
root_widget.mainloop()
