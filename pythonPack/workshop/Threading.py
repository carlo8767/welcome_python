import threading
import time

class VerifyThread:

    def __init__(self):
        self.send_complete = threading.Event()


    def send(self):
        print("send")
        for _ in range(3):
            print("loop")
            time.sleep(1)
        # SET THE FLAG TO  TRUE
        self.send_complete.set()

    def response (self):
        while not self.send_complete.is_set():
            print("response")
            time.sleep(0.5)

if __name__ == "__main__":
    ns = [0,1,9,10,11]

    print(ns[1:3])
    empty_dictionary = {}
    if len(empty_dictionary) == 0:
        print("EMPTY!!")
    o = VerifyThread()
    # FLAG
    send_thread = threading.Thread(target=o.send)
    receive_thread = threading.Thread(target=o.response)
    send_thread.start()
    receive_thread.start()
    send_thread.join()
    # BLOCKED UNTIL HAS COMPLETED
    receive_thread.join()




