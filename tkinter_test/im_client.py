import tkinter as tk


master = tk.Tk()


displayed_msg = tk.StringVar()
t1 = tk.Text(master, width = 50)
t1.grid(row=0, column=0, columnspan=5)



typed_msg=tk.StringVar()
e1 = tk.Entry(master, width = 30, textvariable = typed_msg)
e1.grid(row=1, column=0, columnspan=4)

row_index = 0.0
def send_msg ():
    t1.insert(row_index, typed_msg.get())




b1 = tk.Button(master, text = 'Send', command=send_msg)
b1.grid(row=1,column=4)



master.mainloop()
