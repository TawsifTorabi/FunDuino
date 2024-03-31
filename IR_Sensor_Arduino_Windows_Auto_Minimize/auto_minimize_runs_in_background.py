#Auto minimize when recieves "done" in serial.
#Runs in the background

import serial
import threading
import time
import pyautogui

# Define the COM port and baud rate
COM_PORT = 'COM3'  # Change this to your COM port
BAUD_RATE = 9600  # Change this to your baud rate

# Function to simulate keyboard press and release after 10 seconds
def simulate_keyboard():
    pyautogui.hotkey('win', ',')  # Press win + ,
    time.sleep(10)
    pyautogui.hotkey('win', ',')  # Release win + ,

# Function to listen for serial messages
def listen_serial():
    with serial.Serial(COM_PORT, BAUD_RATE) as ser:
        while True:
            # Read serial data
            data = ser.readline().decode().strip()
            if data == "done":
                # Start a thread to simulate keyboard actions
                threading.Thread(target=simulate_keyboard).start()

if __name__ == "__main__":
    # Start listening for serial messages
    listen_serial()
