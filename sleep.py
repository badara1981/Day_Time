#SLEEP 

#time.sleep()
#Suspend execution for the given number of seconds. The actual suspension time may be less than that requested because any caught signal will terminate the time.sleep() following execution of that signal’s catching routine. Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.

import sleep
import os
import time
try:
    import select
except ImportError:
    has_select = False
else:
    has_select = hasattr(select, "select")

if has_select:
    def sleep(seconds):
        return select.select([], [], [], seconds)

elif hasattr(time, "delay"):
    def sleep(seconds):
        milliseconds = int(seconds * 1000)
        time.delay(milliseconds)

elif os.name == "nt":
    def sleep(seconds):
        milliseconds = int(seconds * 1000)
        win32api.ResetEvent(hInterruptEvent);
        win32api.WaitForSingleObject(sleep.sigint_event, milliseconds)

    sleep.sigint_event = win32api.CreateEvent(NULL, TRUE, FALSE, FALSE)
    # SetEvent(sleep.sigint_event) will be called by the signal handler of SIGINT

elif os.name == "os2":
    def sleep(seconds):
        milliseconds = int(seconds * 1000)
        DosSleep(milliseconds)

else:
    def sleep(seconds):
        seconds = int(seconds)
        time.sleep(seconds)
print(sleep)

