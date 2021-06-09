import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        Label(window, text='샌드위치 (5000원)').pack()
        Label(window, text='케이크 (20000원)').pack()

        self.sand_entry = Entry(window)
        self.sand_entry.pack()
        self.cake_entry = Entry(window)
        self.cake_entry.pack()
        Button(window, text="주문하기", command=self.send_order).pack()


    def send_order(self):
        val1 = self.sand_entry.get()
        if val1.isdigit() is False or int(val1) < 0 or int(val1) == 0:
            order_t1 = ""
        else:
            order_t1 = " 샌드위치 (5000원) " + val1 + "개"

        val2 = self.cake_entry.get()
        if val2.isdigit() is False or int(val2) < 0 or int(val2) == 0 :
            order_t2 = ""
        else:
            order_t2 = " 케이크 (20000원) " + val2 + "개"

        if order_t1 != "" and order_t2 != "":
            order_text = self.name + ":" + order_t1 + "," + order_t2
            self.bakeryView.add_order(order_text)
        elif order_t1 == "" and order_t2 == "":
            order_text = ""
        else:
            order_text = self.name + ":" + order_t1 + order_t2
            self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
