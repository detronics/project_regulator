import serial
import tkinter as tk
from tkinter import messagebox as mb

class Tasks(tk.Frame):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.init_main()

    def init_main(self):
        self.pressure_inlet = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw',text='0.00 MPa')
        self.pressure_outlet = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw',text='0.00 MPa')
        self.regulator_position = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw', text='0 %')
        b_open = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='open')
        b_close = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='close')
        b_new_value = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='new value',command=self.input_box)
        b_start_rp = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362', text='start')
        self.pressure_inlet.place(x=0, y=50)
        self.pressure_outlet.place(x=150, y=50)
        self.regulator_position.place(x=115, y=100)
        b_open.place(x=100, y=150)
        b_close.place(x=160, y=150)
        b_new_value.place(x=210, y=150)
        b_start_rp.place(x=300, y=150)

    def input_box(self):
        # TODO "Сделать это окно поверх остальныx"
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
    root.geometry('500x400')
    root.resizable(False, False)
    root.mainloop()
