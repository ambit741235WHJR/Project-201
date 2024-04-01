from tkinter import *

# Create the parent window
root = Tk()

# Set the size and title of the window
root.geometry("400x400")
root.title("Simple Interest Calculator")

# Configuring the window
root.configure(bg="light blue")

# Creating a function to calculate the simple interest
def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    interest = (principal * rate * time) / 100
    round_interest = round(interest, 2)
    result_label.destroy()

    message = Label(result_frame, text=f"The simple interest on the principal amount of\n{principal} at the rate of {rate}% for {time} years is {round_interest}", font=("Arial", 12), fg="black", bg="light blue", width=41, height=5)
    message.place(x=20, y=40)
    message.pack()

# Creating the heading label
heading_label = Label(root, text="Simple Interest Calculator", font=("Arial", 16), fg="black", bg="light blue")
heading_label.place(x=80, y=10)

# Creating the principal label
principal_label = Label(root, text="Enter Principal Amount:", font=("Arial", 12), fg="black", bg="light blue")
principal_label.place(x=10, y=50)

# Creating the principal entry
principal_entry = Entry(root, font=("Arial", 12), fg="black", bg="white")
principal_entry.place(x=200, y=50)

# Creating the rate label
rate_label = Label(root, text="Enter Rate of Interest:", font=("Arial", 12), fg="black", bg="light blue")
rate_label.place(x=10, y=80)

# Creating the rate entry
rate_entry = Entry(root, font=("Arial", 12), fg="black", bg="white")
rate_entry.place(x=200, y=80)

# Creating the time label
time_label = Label(root, text="Enter Time Period:", font=("Arial", 12), fg="black", bg="light blue")
time_label.place(x=10, y=110)

# Creating the time entry
time_entry = Entry(root, font=("Arial", 12), fg="black", bg="white")
time_entry.place(x=200, y=110)

# Creating the calculate button
calculate_button = Button(root, text="Calculate", font=("Arial", 12), fg="black", bg="light green", command=calculate_interest)
calculate_button.place(x=150, y=150)

# Creating the result frame container
result_frame = LabelFrame(root, text="Result", font=("Arial", 12), fg="black", bg="light blue")
result_frame.pack(padx=20, pady=20)
result_frame.place(x=10, y=200)

# Creating the result label
result_label = Label(result_frame, text="Result will be displayed here", font=("Arial", 12), fg="black", bg="light blue", width=41, height=5)
result_label.place(x=20, y=20)
result_label.pack()

# Running the main event loop
root.mainloop()