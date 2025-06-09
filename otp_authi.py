import random
import time

def generate_otp():
    return random.randint(100000, 999999)

def verify_otp(sent_otp, timeout=30, max_attempts=3):
    start_time = time.time()
    attempts = 0

    while attempts < max_attempts:
        entered_otp = input("Enter the OTP: ")
        current_time = time.time()

        if current_time - start_time > timeout:
            print("OTP expired! Please request a new one.")
            return False

        if entered_otp.isdigit() and int(entered_otp) == sent_otp:
            print("OTP verified successfully!")
            return True
        else:
            attempts += 1
            print(f"Incorrect OTP. Try again. Attempts left: {max_attempts - attempts}")

    print("Maximum attempts reached. Access denied.")
    return False

def main():
    otp = generate_otp()
    print(f"Your OTP is: {otp}")  # Simulated sending

    if verify_otp(otp):
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
