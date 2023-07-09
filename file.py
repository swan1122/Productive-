from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.calender = None
        self.combobox = None
        # Rest of the code...

    # Rest of the code...

    def create_widgets(self):
        # Create an instance of ttk.Style
        style = ttk.Style()

        # Configure style options
        style.configure("Custom.TLabel", background="#7895CB", font=("Arial", 12))
        style.configure("Custom.TButton", background="#F0F0F0", font=("Arial", 12))

        # Set colors
        LINE_COLOR = "#C2C2C2"

        # Set fonts
        LABEL_FONT = ("San Francisco", 20)
        ENTRY_FONT = ("San Francisco", 20)

        # Set padding and spacing
        PADDING_X = 10
        PADDING_Y = 10

        # Configure window background color
        self.root.configure(bg="#7895CB")

        # Create entry and labels
        self.entry = Entry(self.root, width=12, font=ENTRY_FONT, fg="white")
        self.entry.grid(row=3, column=1, columnspan=4)
        self.entry.focus()

        line_frame_horizontal = Frame(self.root, height=2, bg=LINE_COLOR)
        line_frame_horizontal.grid(row=1, column=0, columnspan=8, padx=PADDING_X, pady=PADDING_Y, sticky="ew")

        self.result_Entry = Entry(self.root, width=12, font=ENTRY_FONT)
        self.result_Entry.grid(row=4, column=1, columnspan=4)

        # Create clear button
        self.clearButton = Button(self.root, text="Clear", style="Custom.TButton", command=self.clearing)
        self.clearButton.bind("<KeyPress-c>", self.clearing)
        self.clearButton.grid(row=3, column=0)

        # Create equal button
        self.equalButton = Button(self.root, text="Equal", style="Custom.TButton", command=self.calculator)
        self.equalButton.grid(row=4, column=0, padx=PADDING_X, pady=PADDING_Y)

        # Create clock label
        self.clock_label = Label(self.root, style="Custom.TLabel", font=LABEL_FONT, fg="cyan", bg="#7895CB", width=25)
        self.clock_label.grid(row=0, column=0, columnspan=3)

        # Create password manager button
        self.password_manager = Button(self.root, style="Custom.TButton", text="Password Manager", command=self.open_password_manager)
        self.password_manager.grid(row=6, column=0)

        # Rest of the code...

cal = Calculator()
cal.root.mainloop()
