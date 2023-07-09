import time
from tkinter import messagebox
import pyperclip
import json
import string
import secrets
from tkinter import *
import math
from _datetime import datetime
from tkcalendar import Calendar
from tkinter import ttk
from dataclasses import dataclass
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TODAY = datetime.today().strftime("%Y-%m-%d")

# UI Formatting
class Calculator:
    def __init__(self):
        self.calender = None
        self.combobox = None
        self.cal = None
        self.tomato = None
        self.password_manager = None
        self.clock_label = None
        self.date = None
        self.equalButton = None
        self.clearButton = None
        self.result_Entry = None
        self.entry = None
        self.labeling = None
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("800x500")
        # self.root.config(background="#7895CB")
        self.create_widgets()

    def create_widgets(self):
        # Set colors
        """#F0F0F0"""
        LINE_COLOR = "#C2C2C2"

        # Set fonts
        LABEL_FONT = ("San Francisco", 20)
        ENTRY_FONT = ("San Francisco", 20)

        # Set padding and spacing
        PADDING_X = 10
        PADDING_Y = 10

        # Configure window background colo
        # Create entry and labels
        self.entry = Entry(self.root, width=12, font=ENTRY_FONT, fg="white")
        self.entry.grid(row=3, column=1, columnspan=4)
        self.entry.focus()

        line_frame_horizontal = Frame(self.root, height=2, bg=LINE_COLOR)
        line_frame_horizontal.grid(row=1, column=0, columnspan=8, padx=PADDING_X, pady=PADDING_Y, sticky="ew")

        self.result_Entry = Entry(self.root, width=12, font=ENTRY_FONT)
        self.result_Entry.grid(row=4, column=1, columnspan=4)

        # Create clear button
        self.clearButton = Button(self.root, text="Clear",
                                  command=self.clearing)

        self.clearButton.bind("<KeyPress-c>", self.clearing)
        self.clearButton.grid(row=3, column=0)

        # Create equal button
        self.equalButton = Button(self.root, text="equal", command=self.calculator)
        self.equalButton.grid(row=4, column=0, padx=PADDING_X, pady=PADDING_Y)

        # Create clock label
        self.clock_label = Label(self.root, font=LABEL_FONT, fg="cyan", bg="black", width=25)
        self.clock_label.grid(row=0, column=0, columnspan=3)
        self.date = Label(self.root, text=TODAY)
        self.date.grid(row=0, column=4)
        self.update_clock()
        line_frame_horizontal1 = Frame(self.root, height=2, bg=LINE_COLOR)
        line_frame_horizontal1.grid(row=5, column=0, columnspan=8, padx=PADDING_X, pady=PADDING_Y, sticky="ew")

        # Create password manager button
        self.password_manager = Button(self.root, text="Password Manager", command=self.open_password_manager)
        self.password_manager.grid(row=6, column=0)

        line_frame = Frame(self.root, width=2, bg=LINE_COLOR)
        line_frame.grid(row=0, column=5, rowspan=20, padx=PADDING_X, pady=PADDING_Y, sticky="ns")

        # Create pomodoro timer button
        self.tomato = Button(self.root, text="POMODORO TIMER", command=self.open_pomo)
        self.tomato.grid(row=6, column=1)
        line_frame_horizontal2 = Frame(self.root, height=2, bg=LINE_COLOR)
        line_frame_horizontal2.grid(row=7, column=0, columnspan=8, padx=PADDING_X, pady=PADDING_Y, sticky="ew")

        self.combobox = ttk.Combobox(self.root, values=["Calendar"])
        self.combobox.grid(row=8, column=1)

        self.combobox.bind("<<ComboboxSelected>>", self.show_calendar)

    def open_calendar(self):
        if self.calender is None:
            self.calender = Calendar(self.root, background="black", disabledbackground="black",
                                     borderbackground="white", headersbackground="black", normalbackground="black")
            self.calender.config(background="black")
        self.calender.grid(row=9, column=0, columnspan=8)

    def show_calendar(self, event):
        if self.combobox.get() == "Calendar":
            self.open_calendar()

    def handle_keypress(self, event):
        if event.char.lower() == "c":
            self.clearing()

    def open_pomo(self):
        pomo_window = Toplevel(self.root)
        TimerApp(pomo_window)

    def open_password_manager(self):
        password_manager_window = Toplevel(self.root)
        PasswordManager(password_manager_window)

    def clearing(self):
        self.entry.delete(0, END)
        self.result_Entry.delete(0, END)

    def calculator(self):
        operation = self.entry.get()
        try:
            result = eval(operation)
            self.result_Entry.delete(0, END)
            self.result_Entry.insert(END, str(result))
        except Exception as e:
            messagebox.showinfo("Alert", 'Operation must be\n integers')

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def run(self):
        self.root.mainloop()


#  Creating the Password APP


class PasswordManager:
    def __init__(self, password_manager_window):
        self.window = password_manager_window
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(self.window, height=200, width=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        self.website_label = Label(self.window, text="Website:")
        self.website_label.grid(row=1, column=0)
        self.email_label = Label(self.window, text="Email/Username:")
        self.email_label.grid(row=2, column=0)
        self.password_label = Label(self.window, text="Password:")
        self.password_label.grid(row=3, column=0)

        self.website_entry = Entry(self.window, width=21)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()
        self.email_entry = Entry(self.window, width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, "swanhtet102002@gmail.com")
        self.password_entry = Entry(self.window, width=21)
        self.password_entry.grid(row=3, column=1)

        self.search_button = Button(self.window, text="Search", width=13, command=self.find_password)
        self.search_button.grid(row=1, column=2)
        self.generate_password_button = Button(self.window, text="Generate Password", command=self.generate_password)
        self.generate_password_button.grid(row=3, column=2)
        self.add_button = Button(self.window, text="Add", width=36, command=self.save)
        self.add_button.grid(row=4, column=1, columnspan=2)

    def generate_password(self):
        letters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase
        password = "".join(secrets.choice(letters) for _ in range(16))
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)

    def find_password(self):
        website = self.website_entry.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    def run(self):
        self.window.mainloop()


# Error in Timer

class TimerApp:
    def __init__(self, pomo_window):
        self.reps = 0
        self.timer = None

        self.window = pomo_window
        self.window.title("Timer App")
        self.window.config(padx=100, pady=50, bg="#37306B")
        self.window.resizable(False, False)

        self.timer_label = Label(self.window, text="Timer", font=(FONT_NAME, 50, "bold"), bg="#D23369", fg="white")
        self.timer_label.grid(column=2, row=0)

        self.canvas = Canvas(self.window, width=200, height=224)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
        self.canvas.grid(column=2, row=2)

        self.start_button = Button(self.window, text='Start', highlightthickness=0, command=self.start_timer)
        self.start_button.grid(column=0, row=3)

        self.end_button = Button(self.window, text="End", highlightthickness=0, command=self.reset_timer)
        self.end_button.grid(column=5, row=3)

        self.check_marks = Label(self.window, bg="black", fg="white")
        self.check_marks.grid(column=2, row=4)

    def start_timer(self):
        self.reps += 1
        working_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.timer_label.config(text="Break", fg=RED)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.timer_label.config(text="Short", fg=PINK)
        else:
            self.count_down(working_sec)
            self.timer_label.config(text="Work", fg=GREEN)

    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            marking = ""
            for _ in range(math.floor(self.reps / 2)):
                marking += "✔"
            self.check_marks.config(text=marking)

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.check_marks.config(text="")
        self.reps = 0

    def run(self):
        self.window.mainloop()


calc = Calculator()
calc.run()
