import psutil
import time

UPDATE_DELAY = 1  # in seconds

def get_size(bits):
    """
    Returns size of bits in megabits
    """
    return f"{bits / (1024 * 1024):.2f}Mb"

# get the network I/O stats from psutil
io = psutil.net_io_counters()
# extract the total bytes sent and received
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

# Now let's enter the loop that gets the same stats but after a delay so we can calculate the download and upload speed:

while True:
    # sleep for `UPDATE_DELAY` seconds
    time.sleep(UPDATE_DELAY)
    # get the stats again
    io_2 = psutil.net_io_counters()
    # new - old stats gets us the speed in bytes per second
    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
    # Convert bytes per second to bits per second (1 byte = 8 bits)
    us_bits, ds_bits = us * 8, ds * 8
    # print the total download/upload along with current speeds
    print(f"Upload: {get_size(io_2.bytes_sent)}   "
          f", Download: {get_size(io_2.bytes_recv)}   "
          f", Upload Speed: {get_size(us_bits / UPDATE_DELAY)}/s   "
          f", Download Speed: {get_size(ds_bits / UPDATE_DELAY)}/s      ", end="\r")
    # update the bytes_sent and bytes_recv for next iteration
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
