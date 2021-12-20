import serial
import tkinter as tk
from tkinter import messagebox as mb

class Tasks(tk.Frame):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.init_main()
        self.pressure_inlet = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw',text='0.00 MPa')
        self.pressure_outlet = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw',text='0.00 MPa')
        self.regulator_position = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw', text='0 %')
        self.pressure_inlet.place(x=30, y=50)
        self.pressure_outlet.place(x=250, y=50)
        self.regulator_position.place(x=200, y=120)

    def init_main(self):
        self.background = tk.PhotoImage(file='images/Back.png')
        background_label = tk.Label(image=self.background)
        background_label.place(x=0,y=0)
        heading_inlet = tk.Label( font=('times', 12),bg='black', fg='green', justify=tk.LEFT, anchor='nw',text='Давление до регулятора')
        heading_outlet = tk.Label(font=('times', 12), justify=tk.LEFT, anchor='nw', text='Давление после регулятора')
        needle_position = tk.Label(font=('times', 12), justify=tk.LEFT, anchor='nw', text='Положение иглы-дозатора')
        p_min = tk.Label(font=('times', 12), justify=tk.LEFT, anchor='nw', text='P min 0.00 MPa')
        p_max = tk.Label(font=('times', 12), justify=tk.LEFT, anchor='nw', text='P max 0.00 MPa')
        p_value = tk.Label(font=('times', 12), justify=tk.LEFT, anchor='nw', text='P уст 0.00 MPa')
        b_open = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='открыть регулятор')
        b_close = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='закрыть регулятор')
        b_pmin = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='Редактировать',command=self.input_box)
        b_pmax = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='Редактировать',command=self.input_box)
        b_new_value = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='Редактировать',command=self.input_box)
        b_start_rp = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='Старт')
        b_stop_rp = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='Стоп')
        b_open.place(x=10, y=300)
        b_close.place(x=330, y=300)
        b_pmin.place(x=150, y=200)
        b_pmax.place(x=150, y=260)
        b_new_value.place(x=150, y=230)
        b_start_rp.place(x=300, y=230)
        b_stop_rp.place(x=400,y=230)
        heading_inlet.place(x=0, y=10)
        heading_outlet.place(x=220, y=10)
        needle_position.place(x=110, y=100)
        p_min.place(x=10, y=200)
        p_max.place(x=10,y=260)
        p_value.place(x=10, y=230)

    def input_box(self):
        self.window = tk.Toplevel()
        self.window.attributes('-topmost', True)
        self.window.geometry('300x200')
        self.window.resizable(False, False)
        self.window.title('Установка нового значения давления')
        Description = tk.Label(self.window, text='Введите новое значение давления')
        Description.place(x=30, y=50)
        self.new_value = tk.Entry(self.window, width=5, background='white',)
        self.new_value.place(x=130, y=90)
        confirmation = tk.Button(self.window, bg='#e6e7e4', bd=0, activebackground='#636362', text='OK', command=self.close_window)
        confirmation.place(x=130, y=120)

    def close_window(self):
        if self.new_value.get().isdigit() and float(self.new_value.get()) < 7.5:
            print(self.new_value.get())
            self.window.destroy()
        elif not self.new_value.get().isdigit():
            mb.showerror("Ошибка", "Должно быть введено число")
        elif float(self.new_value.get()) > 7.5:
            mb.showerror("Ошибка", "Значение должно быть меньше 7,5 кгс/см2")


if __name__ == '__main__':
    root = tk.Tk()
    app = Tasks(root)
    root.title('Главное окно')
    root.geometry('1095x400')
    root.resizable(False, False)
    root.mainloop()
