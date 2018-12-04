

import threading

SECONDS = 0

def hello():
    global SECONDS

    SECONDS = SECONDS + 1
    print(str(SECONDS) + " Seconds")

    t = threading.Timer(1.0, hello)
    t.start()

t = threading.Timer(1.0, hello)
t.start()