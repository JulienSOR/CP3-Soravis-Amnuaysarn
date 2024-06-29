from tkinter import *
from tkinter import ttk
import local_forex
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import numpy as np

def countMonth(month):
    date = datetime.now()
    date = datetime(date.year, date.month, date.day)
    date_month_ago = date - relativedelta(months=month)
    days_difference = (date - date_month_ago).days
    dayS = [date]
    for i in range(days_difference-1):
        da = date - timedelta(days=1 + i)
        dayS.append(da)
    return dayS

def pricePer(perform):
    if perform == '1M':
        timeSerie = countMonth(1)
    elif perform == '2M':
        timeSerie = countMonth(2)
    elif perform == '6M':
        timeSerie = countMonth(6)
    elif perform == '1Y':
        timeSerie = countMonth(12)
    elif perform == '5Y':
        timeSerie = countMonth(60)
    elif perform == '10Y':
        timeSerie = countMonth(120)
    return timeSerie

class MyProgram:
    def __init__(self, mainwin):
        self.mainwin = mainwin
        self.mainwin.title("Currency exchange rate")
        self.mainwin.geometry('800x700')

        self.__baseCur = StringVar(value="Choose your Base Currency")
        self.__lastCur = StringVar(value="Choose your Currency")
        self.__pricePer = StringVar(value="Price Performance")

    def bot_label(self):
        lb0 = Label(text='Base Currency')
        lb0.grid(row=0, column=0)
        lb1 = Label(text='To Currency')
        lb1.grid(row=0, column=2)
        lb2 = Label(text='Price Performance')
        lb2.grid(row=1, column=0)

        self.combo0 = ttk.Combobox(textvariable=self.__baseCur)
        self.combo0['value'] = (
            'USD', 'GBP', 'CAD', 'JPY'
            , 'SEK', 'SGD', 'HKD', 'AUD'
            , 'CHF', 'KRW', 'CNY', 'TRY'
            , 'NZD', 'EUR', 'RUB', 'INR'
            , 'MXN', 'BRL', 'ZAR', 'IDR')
        self.combo0.grid(row=0, column=1)
        self.combo1 = ttk.Combobox(textvariable=self.__lastCur)
        self.combo1['value'] = (
            'USD', 'GBP', 'CAD', 'JPY'
            , 'SEK', 'SGD', 'HKD', 'AUD'
            , 'CHF', 'KRW', 'CNY', 'TRY'
            , 'NZD', 'EUR', 'RUB', 'INR'
            , 'MXN', 'BRL', 'ZAR', 'IDR')
        self.combo1.grid(row=0, column=3)

        self.combo2 = ttk.Combobox(textvariable=self.__pricePer)
        self.combo2['value'] = ('1M', '2M', '6M', '1Y','5Y','10Y')
        self.combo2.grid(row=1, column=1)
        self.button1 = Button(mainwin, text="Plot", command=self.calculate)
        self.button1.grid(row=1, column=2)

        self.plot_frame = Frame(self.mainwin)
        self.plot_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)


    def calculate(self):
        # time axis-x
        self.performance = self.__pricePer.get()
        self.list_date = pricePer(self.performance)
        self.list_date = np.array(self.list_date)
        self.list_date = np.sort(self.list_date)
        self.list_date = list(self.list_date)
        self.list_date_str = [i.strftime('%d-%m-%Y') for i in self.list_date]
        print(self.list_date_str)
        print(len(self.list_date_str))

        # currency axis-y
        self.basecur = self.__baseCur.get()
        self.lastcur = self.__lastCur.get()
        print('แปลง', self.basecur, 'เป็น', self.lastcur)

        fx = local_forex.ForexRates()
        self.online_rates = fx.fetch_boc_rates()
        fx.update_from_boc_rates(self.online_rates)
        fx.save_rates_to_file()

        self.list_price = []
        for time in self.list_date:
            rate = fx.get_conversion_rate(base=self.basecur, quote=self.lastcur,date=time)
            self.list_price.append(f'{rate:.3f}')
        print(self.list_price)
        print(len(self.list_price))

        for widget in self.plot_frame.winfo_children():
            widget.destroy()


        fig, ax = plt.subplots(figsize=(8, 7))
        ax.plot(self.list_date_str, self.list_price, marker='o', linestyle='-', color='b', label=f'{self.basecur}-{self.lastcur}')
        ax.set_xlabel('Time')
        ax.set_ylabel('Exchange Rate')
        ax.set_title('Exchange Rate Over Time')
        ax.grid(True)
        ax.legend()

        plt.xticks(rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)



mainwin = Tk()
app = MyProgram(mainwin)
app.bot_label()
mainwin.mainloop()
