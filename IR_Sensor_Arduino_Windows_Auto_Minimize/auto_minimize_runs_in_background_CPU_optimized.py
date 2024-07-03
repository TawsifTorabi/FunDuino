import serial
import threading
import time
import pyautogui
from queue import Queue

# Define the COM port and baud rate
COM_PORT = 'COM6'  # Change this to your COM port
BAUD_RATE = 9600  # Change this to your baud rate

MIN_INTERVAL = 5    # Minimum time interval between handling "done" messages (in seconds)
MAX_THREADS = 5     # Maximum number of concurrent threads
last_done_time = 0  # Variable Timestamp of the last processed "done" message

# Queue to manage threads
thread_queue = Queue(MAX_THREADS)

# Function to simulate keyboard press and release after 10 seconds
def simulate_keyboard():
    pyautogui.hotkey('win', ',')  # Press win + ,
    time.sleep(10)
    pyautogui.hotkey('win', ',')  # Release win + ,
    thread_queue.get()  # Remove thread from queue when done
    thread_queue.task_done()

# Function to listen for serial messages
def listen_serial():
    global last_done_time
    with serial.Serial(COM_PORT, BAUD_RATE) as ser:
        while True:
            # Read serial data
            data = ser.readline().decode().strip()
            if data == "done":
                current_time = time.time()
                if current_time - last_done_time >= MIN_INTERVAL and thread_queue.qsize() < MAX_THREADS:
                    last_done_time = current_time
                    # Add a new thread to the queue and start it
                    thread_queue.put(1)
                    threading.Thread(target=simulate_keyboard).start()

if __name__ == "__main__":
    # Start listening for serial messages
    listen_serial()
