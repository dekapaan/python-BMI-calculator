from tkinter import *
from PIL import Image
root = Tk()
root.title("BMI Calculator")
root.geometry("700x500")
header = Label(root, text='Ideal Body Mass Index Calculator')
header.place(relx=0, rely=0)

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
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.3, rely=0.4)


def bmi_calc(value):
    result_bmi = weight / ((height / 100)**2)
    bmi_field.config(state='normal')
    bmi_field.insert(0, result_bmi)
    bmi_field.config(state='readonly')
    if value != "Select...":
        if value == "Male":
            result = ((0.5*weight) / ((height/100)**2)) + 11.5
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
        elif value == "Female":
            result = ((0.5 * weight) / ((height / 100)**2)) + (0.03 * age) + 11
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')


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
    height_entry.delete(0, END)
    weight_entry.delete(0, END)


clear = Button(root, text='Clear')
clear.place(rely=0.85, relx=0.1)
quit = Button(root, text='Exit', command='exit')
quit.place(rely=0.85, relx=0.83)
root.mainloop()

