# Execution Time Measurement

import time

def timer_count(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} took {end-start:.2f} seconds")
        return res
    return wrapper

@timer_count
def sleep_timer(t):
    print('Sleep timer starts')
    time.sleep(t)
    print('sleep timer off')

sleep_timer(3)

