# from datetime import datetime
# import time
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
#
#
# # Get the current date and time
# now = datetime.now()
#
# # Convert the date and time to an integer using the timestamp() method
# timestamp = int(now.timestamp())
#
# # Print the integer value
# print(timestamp)
#
#
# now = datetime.now()
# date = now.strftime("%Y%m%d")
# date_int = int(date)
# print(date_int)
# #
# while True:
#     now = datetime.now()
#     date = now.strftime("%Y%m%d")
#     date_int = int(date)
#     d = 20240529
#     if d < date_int:
#         print('Run functions')
#         d = date_int
#     else:
#         time.sleep(3600)

"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler
#
#
def tick():
    print('Tick! The time is: %s' % datetime.now())
#
#
# if __name__ == '__main__':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(tick, 'interval', seconds=3)
#     scheduler.start()
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
#
#     try:
#         # This is here to simulate application activity (which keeps the main thread alive).
#         while True:
#             time.sleep(2)
#     except (KeyboardInterrupt, SystemExit):
#         # Not strictly necessary if daemonic mode is enabled but should be done if possible
#         scheduler.shutdown()




scheduler = BackgroundScheduler()
scheduler.add_job(tick, 'interval', seconds=3)
scheduler.start()



