import json as js
import tkinter as tk
from tkinter import ttk
from datetime import datetime

#Theme colors
blue = "#2780e3"
black = "black"
red = "red"
grey = "grey"


with open("family_data.json") as f:
    data = js.load(f)

def show_data(details, show):
    title = [member.values() for member in data["family"]]
    for index in range(len(title)):
        rows_data = tuple(title[index])
        details.insert("", tk.END, values=rows_data)
        show.config(state="disabled")

def show_single(single, details, show, items):
    """item = tuple([item for item in items])
    item = details.item(item)
    print(item["values"])"""
    title = [member.values() for member in data["family"]]
    for index in range(len(title)):
        if single in title[index]:
            #print(title[index])
            one = tuple(title[index])
            details.insert("", tk.END, values=one)
        else:
            continue
    show.config(state="disabled")

class FINANCIAL_STATUS(tk.Tk):
    def __init__(self, **args):
        tk.Tk.__init__(self, **args)

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        pages = (Home, second_page)
        for page in pages:
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.LabelFrame(self, labelanchor="n")
        frame.pack(fill="x")

        #WELCOME LABEL
        home_label = tk.Label(frame, text="FINANCIAL STATUS\nTRACKER", bd=0, fg=black, font=("Algerian",26, "normal"), pady=10,
                           padx=10)
        home_label.pack(side="left", padx=10)
        
        #Account button that shows who's account is it that is in use
        with open("family_data.json") as f:
            data = js.load(f)
        account = [member["Name"] for member in data["family"]]
        clicked = tk.StringVar()
        clicked.set(account[0])
        account_button = tk.OptionMenu(frame, clicked, *account) 
        account_button.config(bg="#2780E3", bd=0, fg="white", font=("arial",12, "bold"),pady=20, padx=20, width=30, indicatoron=False)
        account_button.pack(side="right", padx=(30,10), pady=20)

        #Showing details
        title = [member.keys() for member in data["family"]]
        columns_title =tuple(title[0])

        details = ttk.Treeview(self, columns=columns_title, show="headings")
        details.pack(fill="x", pady=10)

        for item in columns_title:
            details.heading(column=item, text=item)

        details.column(columns_title[0], width=80)
        details.column(columns_title[1], width=90)
        details.column(columns_title[2], width=90)
        details.column(columns_title[3], width=40)
        details.column(columns_title[4], width=80)
        details.column(columns_title[5], width=200)
        details.column(columns_title[6], width=150)
        details.column(columns_title[7], width=80)
        
        


        #Trying something else
        show = tk.Button(self, text="Show All", command= lambda: show_data(details, show), 
                         bg="#2780E3", bd=0, fg="white", font=("arial",12, "bold"), padx=20)
        show.pack(fill='x', pady=10)

        show_one = tk.Button(self, text="Show Details",
                         command= lambda: show_single(clicked.get(), details, show, details.get_children()), bg="#2780E3", bd=0, fg="white", 
                         font=("arial",12, "bold"), padx=20)
        show_one.pack()
        
class second_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_label = tk.Label(self, text="SECOND PAGE", bg="blue", anchor="w", bd=0)
        home_label.pack()

app = FINANCIAL_STATUS()
app.geometry("400x500")
app.title("Financial Status Tracker")
app.mainloop()