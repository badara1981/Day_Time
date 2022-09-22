import time
from time import monotonic, perf_counter as my_timer
import os

if os.name == 'nt':
    def _win_perf_counter():
        if _win_perf_counter.frequency is None:
            _win_perf_counter.frequency = _time.QueryPerformanceFrequency()
        return _time.QueryPerformanceCounter() / _win_perf_counter.frequency
    _win_perf_counter.frequency = None

def perf_counter():
    if perf_counter.use_performance_counter:
        try:
            return _win_perf_counter()
        except OSError:
            # QueryPerformanceFrequency() fails if the installed
            # hardware does not support a high-resolution performance
            # counter
            perf_counter.use_performance_counter = False
    if perf_counter.use_monotonic:
        # The monotonic clock is preferred over the system time
        try:
            return time.monotonic()
        except OSError:
            perf_counter.use_monotonic = False
    return time.time()
perf_counter.use_performance_counter = (os.name == 'nt')
perf_counter.use_monotonic = hasattr(time, 'monotonic')

print(perf_counter)