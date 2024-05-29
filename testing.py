from datetime import datetime
import time
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


# Get the current date and time
now = datetime.now()

# Convert the date and time to an integer using the timestamp() method
timestamp = int(now.timestamp())

# Print the integer value
print(timestamp)


now = datetime.now()
date = now.strftime("%Y%m%d")
date_int = int(date)
print(date_int)
#
while True:
    now = datetime.now()
    date = now.strftime("%Y%m%d")
    date_int = int(date)
    d = 20240529
    if d < date_int:
        print('Run functions')
        d = date_int
    else:
        time.sleep(3600)


