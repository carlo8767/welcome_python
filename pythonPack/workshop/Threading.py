import threading
import time

class VerifyThread:

    def __init__(self):
        self.send_complete = threading.Event()


    def send(self):
        print("send")
        for _ in range(3):
            lock = threading.Lock
            print("loop")
            time.sleep(1)
        # SET THE FLAG TO  TRUE
        self.send_complete.set()

    def response (self):
        while not self.send_complete.is_set():
            print("response")
            time.sleep(0.5)

if __name__ == "__main__":

    strings  = ""
    if strings:
        print("ooo", strings)

    ts = threading.Lock
    o = VerifyThread()
    # FLAG
    send_thread = threading.Thread(target=o.send)
    receive_thread = threading.Thread(target=o.response)
    send_thread.start()
    receive_thread.start()
    send_thread.join()
    # BLOCKED UNTIL HAS COMPLETED
    receive_thread.join()




