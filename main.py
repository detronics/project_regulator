import serial
import tkinter as tk

class Tasks(tk.Frame):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.init_main()

    def init_main(self):
        self.pressure_inlet = tk.Label(bg="grey",font=('times', 20), justify=tk.LEFT, anchor='nw',
                                       text='0.00 kgf/cm')
        self.pressure_inlet.place(x=0, y=50)
        self.pressure_outlet = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw',
                                       text='0.00 kgf/cm')
        self.pressure_outlet.place(x=150, y=50)
        self.regulator_position = tk.Label(bg="grey", font=('times', 20), justify=tk.LEFT, anchor='nw',
                                        text='0 %')
        self.regulator_position.place(x=115, y=100)
        b_open = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362',text='open')
        b_close = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362',text='close')
        b_new_value = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362',text='new value')
        b_start_rp = tk.Button(bg='#e6e7e4', bd=0, activebackground='#636362',text='start')
        b_open.place(x=110, y=150)
        b_close.place(x=150, y=150)
        b_new_value.place(x=190, y=150)
        b_start_rp.place(x=260, y=150)

if __name__ == '__main__':
    root = tk.Tk()
    app = Tasks(root)
    root.title('Главное окно')
    root.geometry('500x400')
    root.resizable(False, False)
    root.mainloop()
