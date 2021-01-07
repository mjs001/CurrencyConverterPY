import pip._vendor.requests as requests, json
import tkinter as tk
import config
from tkinter import *

amount_entry1 = None
amount_entry2 = None

def createWidgets():
    
    country_list = ["Australia (AUD)", "Austria (EUR)", "Belgium (EUR)", "Canada (CAD)","Chile (CLP)", "China (CNY)", "Denmark (DKK)", "Finland (EUR)", "France (EUR)", "Germany (EUR)", "Greece (EUR)", "Iceland (EUR)", "India (INR)", "Israel (ILS)", "Italy (EUR)", "Japan (JPY)", "Korea (KRW)", "Mexico (MXN)", "Netherlands (EUR)", "Portugal (EUR)", "Spain (EUR)", "Sweden (SEK)", "Switzerland (CHF)", "Taiwan (TWD)" "Turkey (TRY)", "Thailand (THB)", "United Kingdom (GBP)", "United States (USD)"   ]
    
    text_label = Label(root, text="What currency would you like to convert today?", fg="#333333", bg="#75ABBC")
    text_label.grid(row=1, column=1, pady=10)
    text_label.config(font=('Helvetica', 14, 'bold'))
    
    amount_label = Label(root, text="Enter amount: ", fg="#6153CC", bg="#75ABBC")
    amount_label.grid(row=2, column=0, padx=20, pady=10)
    amount_label.config(font=('Helvetica', 12, 'bold'))
    
    global amount_entry1
    amount_entry1 = Entry(root, width=40, textvariable=amount1)
    amount_entry1.grid(row=2, column=1, padx=20, pady=10)
    
    from_country = Label(root, text="From Country: ", fg="#6153CC", bg="#75ABBC")
    from_country.grid(row=3, column=0, padx=20, pady=10)
    from_country.config(font=('Helvetica', 12, 'bold'))
    
    from_menu = OptionMenu(root, variable1, *country_list )
    from_menu.grid(row=3, column=1, padx=20, pady=10)
    
    to_country = Label(root, text="To Country: ", fg="#6153CC", bg="#75ABBC")
    to_country.grid(row=4, column=0, padx=20, pady=10)
    to_country.config(font=('Helvetica', 12, 'bold'))
    
    to_menu = OptionMenu(root, variable2, *country_list )
    to_menu.grid(row=4, column=1, padx=20, pady=10)
    
    convert_button = Button(root, width=15, text="Convert", command=Calculate , bg="#D62839")
    convert_button.grid(row=5, column=1, padx=20, pady=10)
    
    converted_text = Label(root, text="Converted Amount: ", fg="#6153CC", bg="#75ABBC")
    converted_text.grid(row=6, column=0, padx=20, pady=10)
    converted_text.config(font=('Helvetica', 12, 'bold'))
    
    global amount_entry2
    amount_entry2 = Entry(root, width=40)
    amount_entry2.grid(row=6, column=1, pady=10)
    
    clear_button= Button(root, text="Clear", width=10, command=clear, bg="#EDAE49")
    clear_button.grid(row=8, column=1, padx=20, pady=10)
    
def data(str):
    for i in str:
        if i =="(":
            start = str.index(i)+1
        if i==")":
            end = str.index(i)
    return str[start:end]
    
def Calculate():
    # https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    var1 = data(variable1.get())
    var2 = data(variable2.get())
    
    main_url= base_url+"&from_currency="+var1+"&to_currency="+var2+"&apikey="+config.api_key
    req_ob = requests.get(main_url)
    result = req_ob.json()
    Exchange_rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    amount = float(amount1.get())
    new_amount = round(amount*Exchange_rate, 3)
    
    amount_entry2.insert(0, str(new_amount))
    
def clear():
    amount_entry1.delete(0, END)
    amount_entry2.delete(0, END)
    
root = tk.Tk()
root.geometry("650x380")
root.title("Simple Currency Converter")
root.config(background="#75ABBC")

amount1 = StringVar()
variable1 = StringVar()
variable2 = StringVar()
variable1.set("From Country")
variable2.set("To Country")

createWidgets()


root.mainloop()