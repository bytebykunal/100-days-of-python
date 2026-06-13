import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady= 20)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_result_label = tkinter.Label(text= 0)
km_result_label.grid(column=1, row= 1)

def miles_to_km():
    km = float(miles_input.get())*1.60934
    km_result_label.config(text=round(km, 2))

calculate_button = tkinter.Button(text= "Calculate", command= miles_to_km)
calculate_button.grid(column=1, row=2)


miles_input = tkinter.Entry(width=10)
miles_input.insert(0, string="0")
miles_input.grid(column=1, row=0)




window.mainloop()