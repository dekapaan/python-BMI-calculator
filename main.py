from tkinter import *
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.geometry("700x500")
header = Label(root, text='Ideal Body Mass Index Calculator')
header.place(x=250, y=0)

frame = Frame(root, width=500, height=200, borderwidth=1, relief='ridge')
frame.place(relx=0.15, rely=0.1)

weight = Label(frame, text="Weight(kg):")
weight.place(relx=0, rely=0)
weight_entry = Entry(frame)
weight_entry.place(relx=0.3, rely=0)

height = Label(frame, text="Height(cm):")
height.place(relx=0, rely=0.2)
height_entry = Entry(frame)
height_entry.place(relx=0.3, rely=0.2)

gender = Label(frame, text="Gender:")
gender.place(rely=0.43, relx=0)

age = Label(frame, text="Age:")
age.place(rely=0.7, relx=0)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.7, relx=0.3)

options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])


def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.3, rely=0.4)


def bmi_calc():
    try:
        int(weight_entry.get())
        int(height_entry.get())
        int(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * int(weight_entry.get())) / ((int(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = int(weight_entry.get()) / ((int(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * int(weight_entry.get())) / ((int(height_entry.get()) / 100) ** 2)) + (
                        0.03 * int(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = int(weight_entry.get()) / ((int(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()


calculate = Button(root, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(rely=0.52, relx=0.2)

bmi = Label(root, text="BMI:")
bmi.place(rely=0.7, relx=0.1)
bmi_field = Entry(root, state='readonly')
bmi_field.place(rely=0.7, relx=0.2)
ideal_bmi = Label(root, text='Ideal BMI:')
ideal_bmi.place(rely=0.7, relx=0.5)
ideal_field = Entry(root, state='readonly')
ideal_field.place(rely=0.7, relx=0.65)


def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])


clear = Button(root, text='Clear', command=delete)
clear.place(rely=0.85, relx=0.1)
quit = Button(root, text='Exit', command='exit')
quit.place(rely=0.85, relx=0.83)
root.mainloop()
