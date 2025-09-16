from tkinter import *

window = Tk()
window.title("MY FIRST GUI PROGRAM")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

#Enrty

km = Entry(width=10)
km.insert(END, "0")
print(km.get())
km.grid(column=1, row=0)

#label

label = Label(text="Miles", font=("Arial", 14))
label.grid(column=2, row=0)

result_label = Label(text=km.get(), font=("Arial", 14))
result_label.grid(column=1, row=1)

label2 = Label(text="is equal to", font=("Arial", 14))
label2.grid(column=0, row=1)

label3 = Label(text="Km", font=("Arial", 14))
label3.grid(column=2, row=1)


#BUTTON
def clicked():
    km_int = float(km.get())
    result = round(km_int * 1.6, 2)
    result_label["text"] = f"{result}"


button = Button(text="Calculate", command=clicked)
button.grid(column=1, row=2)

window.mainloop()
