from tkinter import *


def miles_to_km(mile):
    return float(mile)*1.609


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)


#Entry
input = Entry(width=10)

print(input.get())
input.place(x=150,y=30)


#Label
miles = Label(text="Miles", font=("Arial", 12))
miles.place(x=250, y=35)

equal = Label(text="is equal to", font=("Arial", 12))
equal.place(x=80, y=70)

km_result = Label(text="0", font=("Arial", 12))
km_result.place(x=190, y=70)

km = Label(text="Km", font=("Arial", 12))
km.place(x=250, y=70)


#Button
def button_clicked():
    print("I got clicked")
    new_text = miles_to_km(input.get())
    km_result.config(text=new_text)

button = Button(text="Calculate", command=button_clicked)
button.place(x=170, y=100)
window.mainloop()