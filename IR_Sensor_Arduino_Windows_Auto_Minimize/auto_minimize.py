#Only works when the python cli window is in focus.
#Uses the Start + Comma to hide all the window open.

import serial
import threading
import time
from pynput.keyboard import Key, Controller

# Define the COM port and baud rate
COM_PORT = 'COM6'  # Change this to your COM port
BAUD_RATE = 9600  # Change this to your baud rate

# Function to simulate keyboard press and release after 10 seconds
def simulate_keyboard():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(',')
    time.sleep(10)
    keyboard.release(Key.cmd)
    keyboard.release(',')

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
