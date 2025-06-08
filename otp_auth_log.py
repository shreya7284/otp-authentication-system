import random
import tkinter as tk
from tkinter import messagebox
import time
import csv
from datetime import datetime

# Parameters
timeout_seconds = 30
max_attempts = 3

# Globals
otp = None
start_time = None
attempts = 0

def log_attempt(entered_otp, result):
    with open("otp_attempts_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, entered_otp, result])

def generate_otp():
    global otp, start_time, attempts
    otp = random.randint(100000, 999999)
    start_time = time.time()
    attempts = 0
    otp_label.config(text=f"Your OTP is: {otp}")
    otp_entry.delete(0, tk.END)
    info_label.config(text=f"You have {max_attempts} attempts and {timeout_seconds} seconds to verify.")

def verify_otp():
    global attempts
    current_time = time.time()

    if current_time - start_time > timeout_seconds:
        messagebox.showerror("Error", "OTP expired! Please click 'Resend OTP' to get a new one.")
        log_attempt(otp_entry.get(), "Failed - OTP expired")
        return

    entered = otp_entry.get()
    if entered.isdigit() and int(entered) == otp:
        messagebox.showinfo("Success", "OTP verified successfully! Access granted.")
        log_attempt(entered, "Success")
        root.destroy()
    else:
        attempts += 1
        attempts_left = max_attempts - attempts
        log_attempt(entered, "Failed - Incorrect OTP")
        if attempts_left <= 0:
            messagebox.showerror("Error", "Maximum attempts reached. Access denied.")
            root.destroy()
        else:
            messagebox.showerror("Error", f"Incorrect OTP. Attempts left: {attempts_left}")

# Setup GUI
root = tk.Tk()
root.title("OTP Authentication System")
root.geometry("350x250")

otp_label = tk.Label(root, text="", font=("Arial", 14))
otp_label.pack(pady=10)

info_label = tk.Label(root, text="")
info_label.pack(pady=5)

entry_label = tk.Label(root, text="Enter OTP:")
entry_label.pack()

otp_entry = tk.Entry(root)
otp_entry.pack()

verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=10)

resend_button = tk.Button(root, text="Resend OTP", command=generate_otp)
resend_button.pack()

# Generate the first OTP when the program starts
generate_otp()

root.mainloop()
