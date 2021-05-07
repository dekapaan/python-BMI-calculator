from tkinter import *
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.geometry("700x600")
root.config(bg="#333")
header = Label(root, text='IDEAL BODY MASS INDEX CALCULATOR', bg='#333', fg='white')
header.place(x=220, y=20)

frame = Frame(root, width=500, height=200, relief='raised', bg='#222')
frame.place(relx=0.15, rely=0.1)

weight = Label(frame, text="Weight(kg):", bg='#222', fg='white')
weight.place(relx=0.1, rely=0.1)
weight_entry = Entry(frame)
weight_entry.place(relx=0.4, rely=0.1)

height = Label(frame, text="Height(cm):", bg='#222', fg='white')
height.place(relx=0.1, rely=0.3)
height_entry = Entry(frame)
height_entry.place(relx=0.4, rely=0.3)

gender = Label(frame, text="Gender:", bg='#222', fg='white')
gender.place(rely=0.53, relx=0.1)

age = Label(frame, text="Age:", bg='#222', fg='white')
age.place(rely=0.8, relx=0.1)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.8, relx=0.4)

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
gender_menu.place(relx=0.4, rely=0.5)


def bmi_calc():
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        if result_bmi < 18.5:
            category.config(text='Underweight')
        elif 18.5 <= result_bmi < 25:
            category.config(text='Healthy')
        elif 25 <= result_bmi < 30:
            category.config(text='Overweight')
        elif result_bmi >= 30:
            category.config(text='Obese')

    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()


calculate = Button(root, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(rely=0.45, relx=0.2)

bmi = Label(root, text="BMI:", bg='#333', fg="white")
bmi.place(rely=0.55, relx=0.1)
bmi_field = Entry(root, state='readonly')
bmi_field.place(rely=0.55, relx=0.2)
ideal_bmi = Label(root, text='Ideal BMI:', bg='#333', fg="white")
ideal_bmi.place(rely=0.55, relx=0.5)
ideal_field = Entry(root, state='readonly')
ideal_field.place(rely=0.55, relx=0.65)


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
    category.config(text='')


category_head = Label(root, text="Category:", bg='#333', fg='white')
category = Label(root, width=20, bg='#222', fg='white')
category.place(relx=0.38, rely=0.72)
category_head.place(relx=0.45, rely=0.67)
clear = Button(root, text='Clear', command=delete)
clear.place(rely=0.85, relx=0.1)
quit = Button(root, text='Exit', command='exit')
quit.place(rely=0.85, relx=0.83)
root.mainloop()
